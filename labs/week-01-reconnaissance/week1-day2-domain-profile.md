# ACME Domain and DNS Profile

## 1. Scope Confirmation

This Day 2 recon work is limited to the local ACME lab at `127.0.0.1:8000` and the fictional records provided in the course notes. Real companies, public domains, public IPs, and third-party systems are out of scope.

Since `127.0.0.1` is a local loopback address, public WHOIS, public DNS, and real certificate searches are not expected to have useful records for it. Any outside-looking names in this report are fictional or lab notes unless clearly marked otherwise.

## 2. Local Resolution Findings

Local resolution checks showed that `localhost` maps to both IPv4 and IPv6 loopback addresses:

- `127.0.0.1`
- `::1`

The local hosts file contains localhost entries. No `acme.test` entry was found during this check, so I did not treat `acme.test` as a working local name. I also did not edit the hosts file for this deliverable.

Public DNS was not needed for `localhost`. That is expected because localhost is handled locally.

## 3. HTTP Identity Findings

The ACME site was reachable at `http://127.0.0.1:8000/`.

Observed response details:

- Status: `HTTP/1.0 200 OK`
- Server header: `ACMETrainingHTTP/1.0 Python/3.14.5`
- Content type: `text/html; charset=utf-8`
- Cache behavior: `Cache-Control: no-store`
- Page title: `ACME Global Operations | ACME`
- Main routes visible in navigation: `/about`, `/products`, `/careers`, `/support`, `/vendor`, `/shipments`, and `/portal`
- Footer links include `/lab-notes`, `/health`, and `/robots.txt`

The app did not support a `HEAD` request during testing and returned `501 Unsupported method ('HEAD')`. That is just an observation, not a security issue by itself.

Using an `acme.test:8000` Host header against `127.0.0.1` returned the same basic headers as the direct IP request. I did not see different behavior from that header check.

The JavaScript file at `/static/js/site.js` includes lab-only clues:

- `environment`: `warehouse-lab`
- `internalHost`: `intranet.acme.local`
- `legacyConfigPath`: `/internal/config`
- `demoToken`: `FAKE_ACME_DEMO_KEY_DO_NOT_USE`

These look intentional for the lab and should not be treated as real secrets.

## 4. Fictional DNS Record Inventory

| Hostname | Record Type | Value | Likely Purpose | Confidence |
|---|---|---|---|---|
| `acme-training.test` | NS | `ns1.acme-training.test` | Name server for the fictional domain | Confirmed |
| `acme-training.test` | NS | `ns2.acme-training.test` | Backup name server for the fictional domain | Confirmed |
| `acme-training.test` | MX | `mail.acme-training.test` | Mail routing for the fictional domain | Confirmed |
| `acme-training.test` | TXT | `v=spf1 include:mailvendor.test -all` | Mail sender policy using a mail vendor | Confirmed |
| `www.acme-training.test` | A | `192.0.2.10` | Public website | Probable |
| `portal.acme-training.test` | A | `192.0.2.20` | Login or user portal | Probable |
| `api.acme-training.test` | A | `192.0.2.30` | Application API | Probable |
| `dev.acme-training.test` | CNAME | `dev-platform.vendor.test` | Development system hosted by a vendor | Possible |
| `vpn.acme-training.test` | A | `192.0.2.40` | Remote access service | Possible |
| `status.acme-training.test` | CNAME | `status-provider.test` | Hosted status page | Probable |

The `192.0.2.0/24` addresses are documentation addresses from the course material, not live targets.

## 5. Certificate Transparency Analysis

The fictional certificate names were:

- `www.acme-training.test`
- `portal.acme-training.test`
- `api.acme-training.test`
- `legacy-api.acme-training.test`
- `staging-portal.acme-training.test`
- `vpn.acme-training.test`

Names present in the certificate list but absent from the current fictional DNS list:

- `legacy-api.acme-training.test`
- `staging-portal.acme-training.test`

Those names could point to old systems, hidden systems, retired systems, or certificates that outlived the DNS records. They should not be reported as active systems without more proof.

The names also reveal useful context. `legacy-api` suggests an older API, and `staging-portal` suggests a non-production portal. Those may deserve review, but only within an approved scope.

## 6. Third-Party Dependencies

The fictional records suggest these outside dependencies:

- `mailvendor.test` from the SPF record.
- `dev-platform.vendor.test` from the `dev` CNAME.
- `status-provider.test` from the `status` CNAME.

These are useful to note, but they are not automatically in scope. Anything pointing to a vendor or provider would need separate authorization before testing.

## 7. Potential Risks

Potential risks to investigate later:

- Descriptive names such as `dev`, `vpn`, `legacy-api`, and `staging-portal` reveal how the environment may be organized.
- Certificate logs may show names that are no longer in DNS.
- Third-party CNAME records may create dependency risk.
- Public portal, API, VPN, and status names may attract attention.
- JavaScript in the local ACME site exposes lab-only config clues.
- Health, status, and lab notes pages may reveal more than intended.

These are leads, not confirmed vulnerabilities.

## 8. Alternative Explanations

Not every clue means there is a problem.

- `legacy-api` could be an old certificate entry for a system that no longer exists.
- `staging-portal` could be protected, retired, or never publicly reachable.
- `dev-platform.vendor.test` could be normal vendor-hosted infrastructure.
- `status-provider.test` could be a standard hosted status page.
- The fake token in JavaScript is part of the training lab.
- The missing `acme.test` hosts entry only means it was not configured locally during this check.

## 9. Defensive Recommendations

Recommended defensive actions:

- Keep a current list of public hostnames.
- Remove stale DNS records.
- Review certificate logs for old or unexpected names.
- Avoid public names that reveal too much, when possible.
- Protect development, staging, VPN, and admin systems carefully.
- Review third-party DNS and mail dependencies.
- Use mail protections such as SPF, DKIM, and DMARC.
- Keep health and status endpoints simple and low-detail.
- Treat certificate and DNS findings as leads until confirmed.

## 10. Evidence Log

| Date and Time | Command or Check | Result | Interpretation |
|---|---|---|---|
| 2026-06-17 08:31:09 EDT | Check local hosts entries for localhost and acme.test | `localhost` entries found for `127.0.0.1` and `::1`; no `acme.test` entry found | Localhost is mapped locally. `acme.test` was not configured at the time of review. |
| 2026-06-17 08:31:09 EDT | Resolve `localhost` locally | Returned `::1` and `127.0.0.1` | Public DNS was not needed for localhost. |
| 2026-06-17 08:36:26 EDT | `GET http://127.0.0.1:8000/` headers | Returned `HTTP/1.0 200 OK` with `ACMETrainingHTTP/1.0 Python/3.14.5` | The local ACME web service was reachable and identified itself as the training server. |
| 2026-06-17 08:34:42 EDT | `HEAD http://127.0.0.1:8000/` | Returned `501 Unsupported method ('HEAD')` | The local server does not support HEAD requests. |
| 2026-06-17 08:36:24 EDT | `GET /` with `Host: acme.test:8000` | Returned the same basic headers as the direct IP request | No obvious Host-based difference was seen in this simple check. |
| 2026-06-17 08:36:26 EDT | Review homepage HTML | Found title, navigation routes, static files, and footer links | The public page gives useful route and application clues. |
| 2026-06-17 08:36:26 EDT | Review `/static/js/site.js` | Found lab-only config values and fake demo token | These are intentional training clues, not real secrets. |
