#!/usr/bin/env python3
"""Local-only ACME training target for the ATT&CK learning path."""

from __future__ import annotations

import html
import json
import mimetypes
import os
import secrets
import sqlite3
import time
from http import cookies
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

BASE_DIR = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
DATA_DIR = BASE_DIR / "data"
LOG_FILE = DATA_DIR / "access.log"
TICKETS_FILE = DATA_DIR / "support_tickets.jsonl"
DB_FILE = DATA_DIR / "acme.sqlite"
HOST = os.environ.get("ACME_HOST", "127.0.0.1")
PORT = int(os.environ.get("ACME_PORT", "8000"))

USERS = {
    "jane.doe": {"password": "Spring2026!", "role": "Employee", "team": "Operations"},
    "sam.admin": {"password": "ChangeMe123!", "role": "Administrator", "team": "Security"},
    "vendor.acme": {"password": "VendorPortal2026", "role": "Vendor", "team": "Logistics Partner"},
}

VENDOR_SEED = [
    (
        "northwind",
        "Northwind Freight",
        "Freight brokerage",
        "Northwest",
        "Renewal pending",
        "Regional LTL coverage for warehouse overflow routes.",
    ),
    (
        "contoso",
        "Contoso Sensors",
        "Telemetry hardware",
        "Midwest",
        "Active",
        "Approved supplier for smart crate sensor modules.",
    ),
    (
        "globex",
        "Globex Analytics",
        "Route intelligence",
        "West",
        "Pilot",
        "Data-sharing pilot for route delay forecasting.",
    ),
    (
        "initech",
        "Initech Mobile",
        "Field devices",
        "South",
        "Active",
        "Warehouse tablet refresh and scanner support partner.",
    ),
    (
        "umbrella",
        "Umbrella Cold Chain",
        "Temperature logistics",
        "Northeast",
        "Watchlist",
        "Cold-chain carrier under quarterly performance review.",
    ),
    (
        "stark",
        "Stark Packaging",
        "Rugged containers",
        "Central",
        "Active",
        "Backup supplier for impact-resistant crate shells.",
    ),
    (
        "wayne",
        "Wayne Yard Services",
        "Facility maintenance",
        "East",
        "Active",
        "Dock equipment and yard-light maintenance provider.",
    ),
    (
        "hooli",
        "Hooli Transit Labs",
        "Optimization research",
        "West",
        "Review required",
        "Experimental dispatch optimization proof of concept.",
    ),
]

SESSIONS: dict[str, str] = {}


def ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    LOG_FILE.touch(exist_ok=True)
    TICKETS_FILE.touch(exist_ok=True)


def init_database() -> None:
    ensure_data_dir()
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS vendors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                service TEXT NOT NULL,
                region TEXT NOT NULL,
                status TEXT NOT NULL,
                notes TEXT NOT NULL
            )
            """
        )
        count = conn.execute("SELECT COUNT(*) FROM vendors").fetchone()[0]
        if count == 0:
            conn.executemany(
                """
                INSERT INTO vendors (code, name, service, region, status, notes)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                VENDOR_SEED,
            )
        conn.commit()


def render_template(name: str, **context: Any) -> bytes:
    template = (TEMPLATE_DIR / name).read_text(encoding="utf-8")
    page = template.format(**{key: str(value) for key, value in context.items()})
    return page.encode("utf-8")


def page_shell(title: str, body: str, username: str | None = None) -> bytes:
    user_badge = f"Signed in as {html.escape(username)}" if username else "Guest"
    return render_template("layout.html", title=html.escape(title), body=body, user_badge=user_badge)


def form_value(params: dict[str, list[str]], key: str) -> str:
    return params.get(key, [""])[0].strip()


def db_rows(sql: str, params: tuple[str, ...] = ()) -> list[sqlite3.Row]:
    init_database()
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        return list(conn.execute(sql, params))


def search_vendors(query: str) -> list[sqlite3.Row]:
    cleaned = query.strip().lower()
    if not cleaned:
        return db_rows(
            """
            SELECT code, name, service, region, status, notes
            FROM vendors
            ORDER BY name
            """
        )
    pattern = f"%{cleaned}%"
    return db_rows(
        """
        SELECT code, name, service, region, status, notes
        FROM vendors
        WHERE lower(code) LIKE ?
           OR lower(name) LIKE ?
           OR lower(service) LIKE ?
           OR lower(region) LIKE ?
           OR lower(status) LIKE ?
           OR lower(notes) LIKE ?
        ORDER BY name
        """,
        (pattern, pattern, pattern, pattern, pattern, pattern),
    )


def search_vendors_sql_lab(query: str) -> tuple[list[sqlite3.Row], str, str]:
    cleaned = query.strip().lower()
    if cleaned:
        sql = f"""
        SELECT code, name, service, region, status, notes
        FROM vendors
        WHERE lower(code) LIKE '%{cleaned}%'
           OR lower(name) LIKE '%{cleaned}%'
           OR lower(service) LIKE '%{cleaned}%'
           OR lower(region) LIKE '%{cleaned}%'
           OR lower(status) LIKE '%{cleaned}%'
           OR lower(notes) LIKE '%{cleaned}%'
        ORDER BY name
        """
    else:
        sql = """
        SELECT code, name, service, region, status, notes
        FROM vendors
        ORDER BY name
        """
    try:
        return db_rows(sql), sql.strip(), ""
    except sqlite3.Error as error:
        return [], sql.strip(), str(error)


def render_vendor_table(rows: list[sqlite3.Row]) -> str:
    if not rows:
        return '<p class="empty-state">No matching vendors found.</p>'
    table_rows = []
    for row in rows:
        table_rows.append(
            """
            <tr>
              <td><code>{code}</code></td>
              <td>{name}</td>
              <td>{service}</td>
              <td>{region}</td>
              <td><span class="status-pill">{status}</span></td>
              <td>{notes}</td>
            </tr>
            """.format(
                code=html.escape(row["code"]),
                name=html.escape(row["name"]),
                service=html.escape(row["service"]),
                region=html.escape(row["region"]),
                status=html.escape(row["status"]),
                notes=html.escape(row["notes"]),
            )
        )
    return """
    <div class="table-wrap">
      <table class="vendor-table">
        <thead>
          <tr>
            <th>Code</th>
            <th>Vendor</th>
            <th>Service</th>
            <th>Region</th>
            <th>Status</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
    </div>
    """.format(rows="\n".join(table_rows))


def result_count_text(count: int) -> str:
    if count == 1:
        return "1 vendor found"
    return f"{count} vendors found"


class AcmeHandler(BaseHTTPRequestHandler):
    server_version = "ACMETrainingHTTP/1.0"

    def log_message(self, format: str, *args: Any) -> None:  # noqa: A002 - inherited API name
        ensure_data_dir()
        entry = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "client": self.client_address[0],
            "method": self.command,
            "path": self.path,
            "message": format % args,
        }
        with LOG_FILE.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry) + "\n")

    def current_user(self) -> str | None:
        raw_cookie = self.headers.get("Cookie", "")
        jar = cookies.SimpleCookie(raw_cookie)
        session = jar.get("acme_session")
        if not session:
            return None
        return SESSIONS.get(session.value)

    def send_html(self, content: bytes, status: int = 200, headers: dict[str, str] | None = None) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(content)

    def redirect(self, location: str, headers: dict[str, str] | None = None) -> None:
        self.send_response(303)
        self.send_header("Location", location)
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()

    def read_post(self) -> dict[str, list[str]]:
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8")
        return parse_qs(body)

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        parsed = urlparse(self.path)
        path = parsed.path
        user = self.current_user()

        if path.startswith("/static/"):
            return self.serve_static(path)
        if path == "/":
            return self.page_home(user)
        if path == "/about":
            return self.simple_page("About ACME", "about.html", user)
        if path == "/products":
            return self.simple_page("Products", "products.html", user)
        if path == "/careers":
            return self.simple_page("Careers", "careers.html", user)
        if path == "/support":
            return self.page_support(user)
        if path == "/login":
            return self.page_login(user=user)
        if path == "/logout":
            return self.logout()
        if path == "/portal":
            return self.page_portal(user)
        if path == "/vendor":
            params = parse_qs(parsed.query)
            query = form_value(params, "q")
            mode = form_value(params, "mode")
            return self.page_vendor(user, query, mode)
        if path == "/lab-notes":
            return self.simple_page("Lab Notes", "lab-notes.html", user)
        if path == "/robots.txt":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"User-agent: *\nDisallow: /lab-notes\nDisallow: /portal\n")
            return None
        if path == "/health":
            payload = {"status": "ok", "service": "acme-training-target", "local_only": True}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode("utf-8"))
            return None
        return self.not_found(user)

    def do_POST(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        parsed = urlparse(self.path)
        if parsed.path == "/login":
            return self.handle_login()
        if parsed.path == "/support":
            return self.handle_support()
        return self.not_found(self.current_user())

    def serve_static(self, path: str) -> None:
        relative = path.removeprefix("/static/")
        target = (STATIC_DIR / relative).resolve()
        if not str(target).startswith(str(STATIC_DIR.resolve())) or not target.is_file():
            return self.not_found(self.current_user())
        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(target.read_bytes())
        return None

    def page_home(self, user: str | None) -> None:
        body = (TEMPLATE_DIR / "home.html").read_text(encoding="utf-8")
        self.send_html(page_shell("ACME Global Operations", body, user))

    def simple_page(self, title: str, template: str, user: str | None) -> None:
        body = (TEMPLATE_DIR / template).read_text(encoding="utf-8")
        self.send_html(page_shell(title, body, user))

    def page_support(self, user: str | None, message: str = "") -> None:
        body = render_template("support.html", message=message).decode("utf-8")
        self.send_html(page_shell("Support", body, user))

    def page_login(self, error: str = "", user: str | None = None) -> None:
        body = render_template("login.html", error=error).decode("utf-8")
        self.send_html(page_shell("Login", body, user))

    def page_portal(self, user: str | None) -> None:
        if not user:
            return self.redirect("/login")
        profile = USERS[user]
        admin_panel = ""
        if profile["role"] == "Administrator":
            admin_panel = """
            <section class=\"panel warning\">
              <h2>Admin Operations</h2>
              <p>Open change tickets: firewall review, vendor SSO cleanup, warehouse tablet patch cycle.</p>
              <p class=\"hint\">Training hint: compare what admin and non-admin users can see.</p>
            </section>
            """
        body = render_template(
            "portal.html",
            username=html.escape(user),
            role=html.escape(profile["role"]),
            team=html.escape(profile["team"]),
            admin_panel=admin_panel,
        ).decode("utf-8")
        self.send_html(page_shell("Portal", body, user))

    def page_vendor(self, user: str | None, query: str, mode: str = "") -> None:
        is_lab = mode == "lab"
        safe_query = "" if is_lab else query
        lab_query = query if is_lab else ""

        safe_results = search_vendors(safe_query)
        lab_results: list[sqlite3.Row] = []
        lab_sql = "Submit a lab search to see the intentionally vulnerable SQL statement."
        lab_error = ""
        if is_lab:
            lab_results, lab_sql, lab_error = search_vendors_sql_lab(lab_query)

        lab_error_html = ""
        if lab_error:
            lab_error_html = f'<p class="error">SQLite error: {html.escape(lab_error)}</p>'

        body = render_template(
            "vendor.html",
            safe_query=html.escape(safe_query),
            safe_result_count=html.escape(result_count_text(len(safe_results))),
            safe_results=render_vendor_table(safe_results),
            lab_query=html.escape(lab_query),
            lab_result_count=html.escape(result_count_text(len(lab_results))) if is_lab else "No lab query run",
            lab_results=render_vendor_table(lab_results) if is_lab else '<p class="empty-state">Run a lab search to populate this table.</p>',
            lab_sql=html.escape(lab_sql),
            lab_error=lab_error_html,
        ).decode("utf-8")
        self.send_html(page_shell("Vendor Lookup", body, user))

    def handle_login(self) -> None:
        params = self.read_post()
        username = form_value(params, "username")
        password = form_value(params, "password")
        if username in USERS and secrets.compare_digest(USERS[username]["password"], password):
            token = secrets.token_urlsafe(24)
            SESSIONS[token] = username
            morsel = cookies.SimpleCookie()
            morsel["acme_session"] = token
            morsel["acme_session"]["httponly"] = True
            morsel["acme_session"]["samesite"] = "Lax"
            morsel["acme_session"]["path"] = "/"
            return self.redirect("/portal", {"Set-Cookie": morsel.output(header="")})
        self.page_login("Invalid username or password. Try a documented lab account.")

    def handle_support(self) -> None:
        ensure_data_dir()
        params = self.read_post()
        ticket = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "name": form_value(params, "name"),
            "email": form_value(params, "email"),
            "category": form_value(params, "category"),
            "message": form_value(params, "message"),
        }
        with TICKETS_FILE.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(ticket) + "\n")
        self.page_support(self.current_user(), "Support ticket saved locally for lab review.")

    def logout(self) -> None:
        raw_cookie = self.headers.get("Cookie", "")
        jar = cookies.SimpleCookie(raw_cookie)
        session = jar.get("acme_session")
        if session:
            SESSIONS.pop(session.value, None)
        expired = "acme_session=deleted; Path=/; Max-Age=0; HttpOnly; SameSite=Lax"
        self.redirect("/", {"Set-Cookie": expired})

    def not_found(self, user: str | None) -> None:
        self.send_html(page_shell("Not Found", "<h1>404</h1><p>That ACME resource does not exist.</p>", user), 404)


def main() -> None:
    ensure_data_dir()
    init_database()
    server = ThreadingHTTPServer((HOST, PORT), AcmeHandler)
    print(f"ACME training target running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping ACME training target.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
