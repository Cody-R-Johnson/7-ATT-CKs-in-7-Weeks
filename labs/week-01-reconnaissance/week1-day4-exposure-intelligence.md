# ACME Internet-Exposure Intelligence Report

## 1. Scope Confirmation

This Day 4 work stays inside the authorized ACME lab and the fictional exposure dataset from the course notes. I did not connect to any of the listed documentation IP addresses, and I did not test real public systems.

The local ACME app is running at `127.0.0.1:8000`. That means the service is intended for use from this machine only, not the public internet.

## 2. Local Service Observation

### Listening Configuration

- Address: `127.0.0.1`
- Port: `8000`
- Protocol: TCP
- Exposure: Loopback only, not directly internet reachable
- Confidence: Confirmed

The listening check showed:

```text
Python 89993 codyjohnson 4u IPv4 ... TCP 127.0.0.1:8000 (LISTEN)
```

This is the expected safer binding for the local lab. If the service were bound to `0.0.0.0:8000`, it would be listening on all IPv4 interfaces, which would need more review.

### HTTP Identity

- Status: `HTTP/1.0 200 OK`
- Server banner: `ACMETrainingHTTP/1.0 Python/3.14.5`
- Content type: `text/html; charset=utf-8`
- Relevant headers:
  - `Date: Wed, 17 Jun 2026 15:10:31 GMT`
  - `Cache-Control: no-store`

The page title was:

```text
ACME Global Operations | ACME
```

The server banner reveals that this is the ACME training HTTP server and that it is running on Python. That is useful recon information, but it does not prove the service is vulnerable. A reverse proxy or custom banner could also change what is reported.

## 3. Fictional Exposure Dataset

| Record | Hostname | Port | Product | Observed | Freshness | Confidence |
|---|---|---:|---|---|---|---|
| A | `portal.acme-training.test` | 443 | nginx 1.24.0 | 2026-06-10 | Recent | Probable |
| B | `vpn.acme-training.test` | 443 | Unknown SSL VPN | 2026-04-02 | Aging | Possible |
| C | `dev.acme-training.test` | 22 | OpenSSH 9.3 | 2025-11-18 | Stale | Possible |
| D | `staging-portal.acme-training.test` | 8080 | Python HTTP Server | 2024-09-14 | Stale | Possible |
| E | `api.acme-training.test` | 443 | envoy | 2026-06-15 | Recent | Probable |

Record E is the most recent. Records C and D are stale enough that I would not describe them as current exposure without fresh authorized validation.

## 4. Cross-Source Correlation

| Hostname | DNS | Certificate | Search OSINT | Exposure Dataset | Assessment |
|---|---|---|---|---|---|
| `portal.acme-training.test` | Present | Present | Portal naming appeared in earlier recon | Record A present | Strong evidence the name existed and was associated with a portal. Current reachability is still unverified. |
| `api.acme-training.test` | Present | Present | API naming appeared in earlier recon | Record E present | Strong evidence the API name existed. Record E is recent, but still passive data. |
| `dev.acme-training.test` | Present as CNAME | Not listed in the certificate exercise | Development naming appeared in earlier recon | Record C present | The hostname likely existed, but the exposure record is stale and points to vendor hosting. |
| `vpn.acme-training.test` | Present | Present | VPN naming appeared in earlier recon | Record B present | The hostname suggests remote access, but the observation is aging and should be verified carefully before reporting current exposure. |
| `legacy-api.acme-training.test` | Absent from DNS | Present | Legacy naming appeared in earlier recon | Present as a TLS name in Record E | The name appeared in certificate data, but no current DNS record was provided. It may be retired or only a certificate leftover. |
| `staging-portal.acme-training.test` | Absent from DNS | Present | Staging naming appeared in earlier recon | Record D present | The name appeared in certificate and exposure data, but the exposure record is old. Treat as a historical clue unless verified. |

Multiple sources make a hostname more interesting, but they do not prove the service is currently reachable or vulnerable.

## 5. Findings

### Finding 1

- Title: Local ACME Service Exposes a Detailed Server Banner
- Evidence: `curl -s -D - http://127.0.0.1:8000/ -o /dev/null` returned `Server: ACMETrainingHTTP/1.0 Python/3.14.5`.
- Confidence: Confirmed
- Severity: Informational
- Impact: The banner reveals the training server name and Python version. In a real environment, this could help someone profile the stack.
- Limitations: The service is bound to `127.0.0.1`, so it is not directly internet reachable from this evidence. A banner also does not prove a vulnerability.
- Recommendation: For public services, reduce unnecessary version detail in headers and keep patching/asset inventory current.

### Finding 2

- Title: Fictional API Record Contains Multiple TLS Names
- Evidence: Record E lists `api.acme-training.test` and `legacy-api.acme-training.test` in the TLS names, observed on 2026-06-15.
- Confidence: Probable
- Severity: Low
- Impact: The certificate data suggests the API and legacy API names were related at some point. The legacy name may reveal older architecture or migration history.
- Limitations: This is passive dataset evidence. It does not prove the legacy API is active, reachable, or vulnerable.
- Recommendation: Review certificate issuance, remove retired names when possible, and verify whether legacy names still map to active services.

### Finding 3

- Title: Stale Staging Exposure Record Needs Careful Wording
- Evidence: Record D lists `staging-portal.acme-training.test` on port `8080/tcp` with product `Python HTTP Server`, observed on 2024-09-14.
- Confidence: Possible
- Severity: Informational
- Impact: If current, a public staging service could increase risk. The name also reveals a non-production environment.
- Limitations: The record is old. It should not be described as current exposure without fresh authorized validation.
- Recommendation: Compare passive findings against an approved asset inventory and remove stale DNS/certificate records when systems are retired.

## 6. Stale or Conflicting Data

Records C and D are stale:

- Record C was observed on 2025-11-18.
- Record D was observed on 2024-09-14.

These records may point to systems that moved, closed, changed ownership, or were never meant to be long-lived. They should be written as historical observations, not current facts.

The `legacy-api` and `staging-portal` names were present in certificate data but absent from the fictional DNS list. That could mean the names were retired, hidden, replaced, or only left behind in certificate history.

## 7. Third-Party Scope Boundaries

Some records mention outside providers:

- Record A: `Example Cloud Provider`
- Record B: `Example Colocation Services`
- Record C: `Vendor Platform Hosting`
- Record D: `Example Cloud Provider`
- Record E: `Example Cloud Provider`

The strongest third-party boundary is Record C because `dev.acme-training.test` also matched the earlier CNAME-style vendor-hosting pattern. Anything operated by a vendor or hosting provider needs separate written authorization before testing.

For this report, I only analyzed the provided records. I did not connect to any listed host.

## 8. Defensive Recommendations

- Keep an approved external asset inventory.
- Review internet-exposure search results as leads, not proof.
- Track observation dates and prioritize recent findings.
- Reduce unnecessary product and version banners on public services.
- Monitor certificates for old, legacy, or staging names.
- Remove stale DNS and certificate references when systems are retired.
- Confirm development and staging systems are not publicly exposed.
- Treat vendor-operated infrastructure as separate scope until authorization is clear.
- Compare passive findings against internal inventories before reporting current exposure.

## 9. Evidence Log

| Date and Time | Source | Command or Record | Result | Interpretation |
|---|---|---|---|---|
| 2026-06-17 11:09:29 EDT | Local listener | `lsof -nP -iTCP:8000 -sTCP:LISTEN` | `TCP 127.0.0.1:8000 (LISTEN)` | ACME is bound to loopback only. |
| 2026-06-17 11:10:31 EDT | Local HTTP headers | `curl -s -D - http://127.0.0.1:8000/ -o /dev/null` | `HTTP/1.0 200 OK`, `Server: ACMETrainingHTTP/1.0 Python/3.14.5`, `Cache-Control: no-store` | The local service exposes a banner and normal HTML response. |
| 2026-06-17 11:10 EDT | Local homepage | `curl -s http://127.0.0.1:8000/` | Page title `ACME Global Operations | ACME` | The service is the expected ACME training site. |
| 2026-06-17 11:10 EDT | Local listener fallback | `netstat -anv -p tcp | grep '.8000'` | Blocked by macOS permissions | `lsof` was used as the listening-scope evidence instead. |
| 2026-06-17 11:10 EDT | Fictional dataset | Records A-E from Day 4 notes | Five exposure records reviewed | Records were analyzed without connecting to the listed IPs. |
