# ACME Target Site Guide

## Launch

```bash
./scripts/run_acme.sh
```

The helper starts the app from `target-site/acme/app/server.py` and binds it to `127.0.0.1:8000` by default.

Optional environment variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `ACME_HOST` | `127.0.0.1` | Bind address |
| `ACME_PORT` | `8000` | TCP port |

Example:

```bash
ACME_PORT=8080 ./scripts/run_acme.sh
```

## Pages to Explore

| Path | Purpose | Useful Weeks |
| --- | --- | --- |
| `/` | Public homepage | 1, 2 |
| `/about` | Company profile | 1, 6 |
| `/products` | Product details | 1, 6 |
| `/careers` | Hiring page | 1, 6 |
| `/support` | Support request form | 2, 3 |
| `/login` | Staff and vendor login | 2, 3, 4 |
| `/portal` | Authenticated user portal | 4, 6 |
| `/vendor` | SQLite-backed vendor lookup and SQL training lab | 2, 3, 6 |
| `/lab-notes` | Deliberately exposed training hints | 1, 7 |
| `/health` | JSON health endpoint | 2 |

## Local Data

The app stores request logs, support tickets, and the generated SQLite database under `target-site/acme/data/`. These files are useful for evidence collection and blue-team reflection throughout the 7-week course.

## Vendor SQLite Lab

The vendor page seeds a local SQLite database with fictional supplier records the first time the app starts. The standard vendor search uses parameterized SQL. The same page also includes a clearly labeled SQL training lab panel that intentionally builds a vulnerable query for local-only injection testing and comparison.

Do not point SQL tooling or payloads at systems outside this local lab.
