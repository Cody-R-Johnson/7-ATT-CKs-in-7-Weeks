# ACME Search-Engine OSINT Report

## 1. Scope Confirmation

This report is limited to the local ACME lab at `http://127.0.0.1:8000` and the fictional search examples from the course notes. I did not use a real public company, public domain, or third-party website for this exercise.

The goal was to think like a search-engine OSINT analyst while staying inside the local lab. Since the ACME site is local, I used known local routes, saved page content, keyword searches, `robots.txt`, public JavaScript, and simulated search queries.

## 2. Methodology

I reviewed the known public ACME routes and recorded status codes, page titles, visible purpose, and useful clues. I also reviewed `robots.txt`, downloaded selected public page content to a temporary folder, searched that content for useful terms, checked the public JavaScript file, and reviewed the careers page for technology and organization clues.

I did not brute force directories, scan ports, test real sites, or use any discovered-looking value as a credential.

## 3. Public Route Inventory

| Route | Status | Purpose | Observed Clues | Confidence |
|---|---:|---|---|---|
| `/about` | 200 | Company and team overview | Mentions warehouses, vendors, field teams, dispatchers, warehouse leads, and vendor coordinators. | Confirmed |
| `/products` | 200 | Product overview | Mentions CrateCloud, RouteOps, VendorLink, smart crate telemetry, route control, and vendor onboarding. | Confirmed |
| `/careers` | 200 | Job postings | Mentions SIEM, SSO, Python, REST APIs, SQL, Linux, MDM, MFA, scanners, tablets, and vendor access reviews. | Confirmed |
| `/support` | 200 | Support request form | Mentions login issues, vendor questions, shipment exceptions, and security concerns. | Confirmed |
| `/vendor` | 200 | Vendor lookup | Shows a SQLite-backed vendor table and a local SQL training lab. | Confirmed |
| `/shipments` | 200 | Shipment lookup | Shows shipment records, vendor codes, route details, access-control notes, and IDOR lab hints. | Confirmed |
| `/portal` | 303 | Login-protected portal | Redirects unauthenticated visitors to `/login`. | Confirmed |
| `/lab-notes` | 200 | Training notes | Lists lab clues, accounts, admin routes, activity logs, and `/internal/config`. | Confirmed |
| `/health` | 200 | Health endpoint | Returns service health data with no page title. | Confirmed |
| `/robots.txt` | 200 | Crawler guidance | Lists `/lab-notes`, `/portal`, `/admin`, and `/internal/config`. | Confirmed |

## 4. robots.txt Findings

`robots.txt` returned:

```text
User-agent: *
Disallow: /lab-notes
Disallow: /portal
Disallow: /admin
Disallow: /internal/config
```

The listed routes reveal useful names, especially `/admin` and `/internal/config`. This is not access control. It only tells cooperative crawlers what not to index.

Some routes are protected or partially protected. `/portal` redirects to `/login` when not signed in. `/admin` paths require an administrator. `/internal/config` is intentionally visible in the lab and contains fake training values.

## 5. JavaScript and Static Asset Findings

The public JavaScript file at `/static/js/site.js` includes these lab-only values:

- `intranet.acme.local`
- `/internal/config`
- `FAKE_ACME_DEMO_KEY_DO_NOT_USE`
- `warehouse-lab`

The values are visible without logging in. The demo token is clearly fake, but it is still useful as practice for telling the difference between a real secret and a training clue.

## 6. Careers and Organizational Intelligence

The careers page now gives useful OSINT practice material.

| Job Role | Technology Clue | Organizational Clue | Security Relevance | Confidence |
|---|---|---|---|---|
| Security Analyst | SIEM, SSO logs, scanner and tablet workflows | Warehouse Technology team | Suggests log review and device-heavy operations. | Confirmed |
| Platform Engineer | Python, REST APIs, SQL reporting, Linux | RouteOps team | Suggests backend services, integrations, and reporting systems. | Confirmed |
| Vendor Risk Coordinator | Partner SSO, support escalations, vendor evidence | VendorLink team | Suggests vendor access reviews and third-party process risk. | Confirmed |
| Endpoint Systems Specialist | MDM, tablets, handheld scanners, patch rollouts | Field Operations team | Suggests managed endpoint devices across warehouses. | Confirmed |
| Data Operations Analyst | SQL, CSV exports, dashboards | Logistics Reporting team | Suggests report exports and data-quality concerns. | Confirmed |
| Identity Operations Lead | MFA, SSO onboarding, least-privilege reviews | Access Programs team | Suggests identity lifecycle and access-control work. | Confirmed |

These clues do not prove exactly what is running in production. They are leads for later review.

## 7. Simulated Search Queries

| Query | Objective | Expected Finding Type |
|---|---|---|
| `site:acme-training.test` | List indexed ACME pages. | Public page inventory |
| `site:acme-training.test intitle:"login"` | Find login pages. | Portal or sign-in pages |
| `site:acme-training.test inurl:portal` | Find portal routes. | User or employee portal |
| `site:acme-training.test inurl:admin` | Find admin-looking paths. | Admin route names |
| `site:acme-training.test "internal use only"` | Look for sensitive wording. | Public documents or notes |
| `site:acme-training.test "acme.local"` | Find internal hostname references. | Internal naming clues |
| `site:acme-training.test filetype:pdf` | Look for indexed documents. | Public PDFs |
| `site:acme-training.test filetype:xlsx OR filetype:csv` | Look for spreadsheets or exports. | Public data files |
| `site:acme-training.test inurl:staging OR inurl:dev` | Find environment names. | Development or staging routes |
| `site:acme-training.test "vendor"` | Find partner or vendor references. | Vendor process clues |

These are planning examples only. They are not meant to be run against a real organization.

## 8. Findings

### Finding 1

- Title: Internal Hostname and Config Path Exposed in Public JavaScript
- Evidence: `/static/js/site.js` includes `intranet.acme.local`, `/internal/config`, `warehouse-lab`, and `FAKE_ACME_DEMO_KEY_DO_NOT_USE`.
- Confidence: Confirmed
- Severity: Low
- Impact: The file gives a visitor useful environment and naming clues. In a real site, this could help someone understand internal naming patterns or find exposed configuration routes.
- Limitations: The token is fake and intentionally placed for training. The internal hostname does not prove that any internal system is reachable.
- Recommendation: Keep client-side JavaScript free of internal hostnames, config paths, and token-looking values unless they are truly needed.

### Finding 2

- Title: robots.txt Reveals Sensitive-Looking Route Names
- Evidence: `/robots.txt` lists `/lab-notes`, `/portal`, `/admin`, and `/internal/config`.
- Confidence: Confirmed
- Severity: Informational
- Impact: The file helps visitors find routes that may be interesting. `/admin` and `/internal/config` are especially useful names for recon.
- Limitations: `robots.txt` is not supposed to be access control, and some routes are protected or intentionally included for the lab.
- Recommendation: Do not rely on `robots.txt` to hide sensitive routes. Use real access control and avoid listing paths that do not need to be advertised.

### Finding 3

- Title: Careers Page Reveals Technology and Team Clues
- Evidence: `/careers` mentions SIEM, SSO, Python, REST APIs, SQL, Linux, MDM, MFA, scanners, tablets, vendor access reviews, and logistics reporting.
- Confidence: Confirmed
- Severity: Informational
- Impact: The postings help build a picture of ACME teams, tools, and likely workflows. This can guide later testing and reporting.
- Limitations: Job postings do not prove a technology is deployed in production.
- Recommendation: Review public job postings for unnecessary detail while still keeping them useful for hiring.

## 9. False Positives and Benign Explanations

- The fake token in JavaScript is a training clue, not a real credential.
- `/internal/config` is intentionally visible for the lab.
- `/portal` redirecting to `/login` is normal behavior for a protected page.
- Technology terms on `/careers` may describe desired experience, not current production systems.
- `robots.txt` can list routes for crawler guidance without meaning the routes are vulnerable.
- A keyword match for `admin`, `token`, or `internal` is only a lead until reviewed in context.

## 10. Defensive Recommendations

- Review public JavaScript for internal names, paths, and token-looking values.
- Keep `robots.txt` simple and avoid listing paths that reveal too much.
- Use access controls for private areas instead of relying on route obscurity.
- Review job postings for unnecessary technology detail.
- Keep public health and status endpoints low-detail.
- Retire old public pages and stale training notes.
- Treat search results as leads, then verify them before reporting.
- Include benign explanations in reports so findings stay fair and accurate.

## 11. Evidence Log

| Date and Time | Source | Search or Command | Result | Interpretation |
|---|---|---|---|---|
| 2026-06-17 09:15 EDT | Public routes | `curl -s -o ... -w "%{http_code}" http://127.0.0.1:8000/<route>` | Known routes returned expected statuses. `/portal` returned `303`. | Public route inventory was collected from the local lab. |
| 2026-06-17 09:15 EDT | `/robots.txt` | `curl -s http://127.0.0.1:8000/robots.txt` | Listed `/lab-notes`, `/portal`, `/admin`, and `/internal/config`. | robots.txt exposes useful route names but is not access control. |
| 2026-06-17 09:15 EDT | Public pages | `grep -RniE "admin|token|password|secret|legacy|staging|vendor|employee|internal|SSO|Python|SQL|MFA|MDM" /tmp/acme-day3-pages` | Found hits across vendor, lab notes, careers, shipments, robots, and site.js. | Keyword search found useful leads that still need context. |
| 2026-06-17 09:15 EDT | `/static/js/site.js` | `grep -RniE "token|key|secret|internal|config|api|admin" /tmp/acme-day3-pages/site.js` | Found `intranet.acme.local`, `/internal/config`, and `FAKE_ACME_DEMO_KEY_DO_NOT_USE`. | Public JavaScript exposes lab-only config clues. |
| 2026-06-17 09:15 EDT | `/careers` | `grep -niE "Python|SQL|SSO|MFA|MDM|SIEM|REST|Linux|vendor|tablet|scanner" /tmp/acme-day3-pages/careers.txt` | Found role, technology, identity, device, and reporting clues. | Careers content is useful for OSINT but does not prove production deployment. |
