# ACME Passive Subdomain Enumeration Report

## 1. Scope Confirmation

The authorized target is the local ACME lab at `127.0.0.1:8000` and fictional `acme-training.test` data only. I will not run Amass or enumeration tools against real domains or third-party systems.

The hostnames in this report came from earlier course notes, the provided fictional Amass-style output, and names inferred from local ACME routes. I did not resolve or connect to any of them.

## 2. Methodology

I reviewed the fictional Amass-style list, changed all names to lowercase, removed trailing dots, kept fully qualified names, sorted the results, removed duplicates, and separated ACME names from third-party names.

The supplied list contained:

- 15 unique names in total.
- 14 names under `acme-training.test`.
- 1 third-party name under `mailvendor.test`.

The supplied names were already lowercase and did not contain duplicates or trailing dots. I also compared them with the Day 2 DNS and certificate notes, Day 3 search OSINT, Day 4 exposure dataset, and visible routes in the local ACME site.

## 3. Normalized Subdomain Inventory

| Hostname | Source | Likely Purpose | Classification | Confidence | Scope Status |
|---|---|---|---|---|---|
| `api.acme-training.test` | Day 2 DNS and certificate; Amass-style | Application API | Application/API | High | Fictional ACME scope; passive only |
| `cratecloud.acme-training.test` | Amass-style; ACME product name | CrateCloud service | Product/service | Medium | Fictional ACME scope; unverified |
| `dev.acme-training.test` | Day 2 DNS; Amass-style | Development environment | Development | High | Fictional ACME scope; vendor-hosting boundary noted |
| `legacy-api.acme-training.test` | Day 2 certificate; Amass-style | Older API or migration system | Legacy | Medium | Fictional ACME scope; current use unverified |
| `mail.acme-training.test` | Day 2 MX record; Amass-style | ACME mail routing | Email | High | Fictional ACME scope; passive only |
| `portal.acme-training.test` | Day 2 DNS and certificate; Amass-style | User or partner portal | Application/API | High | Fictional ACME scope; passive only |
| `qa-api.acme-training.test` | Amass-style | QA API environment | Staging/QA | Medium | Fictional ACME scope; unverified |
| `routeops.acme-training.test` | Amass-style; ACME product name | RouteOps service | Product/service | Medium | Fictional ACME scope; unverified |
| `sso.acme-training.test` | Amass-style; Day 3 SSO term | Sign-in or identity service | Identity/access | Medium | Fictional ACME scope; unverified |
| `staging-portal.acme-training.test` | Day 2 certificate; Amass-style | Pre-production portal | Staging/QA | Medium | Fictional ACME scope; current use unverified |
| `status.acme-training.test` | Day 2 DNS; Amass-style | Hosted status page | Public website | High | Fictional ACME scope; third-party hosting boundary noted |
| `vendorlink.acme-training.test` | Amass-style; ACME product name | VendorLink service | Product/service | Medium | Fictional ACME scope; unverified |
| `vpn.acme-training.test` | Day 2 DNS and certificate; Amass-style | Remote access service | Remote access | High | Fictional ACME scope; passive only |
| `www.acme-training.test` | Day 2 DNS and certificate; Amass-style | Public website | Public website | High | Fictional ACME scope; passive only |

### Route-Derived Names

The following names were inferred from local ACME route names. They were not present in DNS, certificate, or Amass-style data and should not be described as confirmed subdomains.

| Inferred Hostname | Local Clue | Likely Purpose | Confidence | Status |
|---|---|---|---|---|
| `admin.acme-training.test` | `/admin` and admin routes | Administrative area | Low | Inferred only |
| `internal.acme-training.test` | `/internal/config` | Internal configuration service | Low | Inferred only |
| `shipments.acme-training.test` | `/shipments` | Shipment tracking | Low | Inferred only |
| `support.acme-training.test` | `/support` | Customer support | Low | Inferred only |
| `vendor.acme-training.test` | `/vendor` | Vendor directory | Low | Inferred only |

## 4. Third-Party Names

| Hostname | Source | Likely Purpose | Classification | Confidence | Scope Status |
|---|---|---|---|---|---|
| `mx1.mailvendor.test` | Amass-style; related Day 2 mail-vendor clue | Vendor mail server | Vendor/third-party | Medium | Out of scope |

The name suggests a mail-provider relationship, but it is not under the fictional ACME domain. It must remain separate from ACME-owned names and must not be tested without its own written authorization.

## 5. Hostname Pattern Analysis

- `cratecloud`, `routeops`, and `vendorlink` match product names shown on the ACME site. This suggests that product names may also be used in hostnames.
- `dev`, `qa`, and `staging` suggest non-production environments. The names do not prove those systems are active or less secure.
- `vpn`, `sso`, and `portal` suggest remote access, identity, or login services.
- `legacy-api` suggests an older service or a system involved in a migration.
- `mailvendor.test` suggests a third-party dependency and a clear scope boundary.
- The local route names suggest other possible naming patterns, but route names are not proof that matching subdomains exist.

## 6. Cross-Source Correlation

| Hostname | DNS | Certificate | Search OSINT | Exposure Dataset | Amass-Style | Assessment |
|---|---|---|---|---|---|---|
| `api.acme-training.test` | Yes | Yes | API terms | Yes | Yes | Strong historical evidence for the name; current reachability is unverified. |
| `portal.acme-training.test` | Yes | Yes | Portal route and terms | Yes | Yes | Strong historical evidence for a portal name; this does not prove a weakness. |
| `dev.acme-training.test` | Yes | No | Development terms | Yes, stale | Yes | Likely historical name with a vendor-hosting clue; current status is unclear. |
| `legacy-api.acme-training.test` | No | Yes | Legacy and API terms | TLS name | Yes | Interesting legacy clue, but no current DNS record was provided. |
| `staging-portal.acme-training.test` | No | Yes | Staging and portal terms | Yes, stale | Yes | Multiple historical clues exist, but the old exposure record needs careful wording. |
| `sso.acme-training.test` | No | No | Careers page mentions SSO | No | Yes | New identity lead from one hostname source supported only by a general SSO clue. |
| `vendorlink.acme-training.test` | No | No | VendorLink product name | No | Yes | The name matches a public ACME product, but the hostname is unverified. |
| `mx1.mailvendor.test` | Related vendor only | No | No | No | Yes | Third-party mail clue that remains out of scope. |

Correlation helps rank the names, but even a name found in several passive sources does not prove that a service is live or vulnerable.

## 7. Findings

### Finding 1

- Title: Passive Sources Reveal Non-Production Hostnames
- Evidence: The fictional Amass-style output includes `dev.acme-training.test`, `qa-api.acme-training.test`, and `staging-portal.acme-training.test`.
- Confidence: Probable
- Severity: Informational
- Impact: These names reveal likely development, QA, and staging environments. In a real assessment, those systems would be useful leads for an authorized review.
- Limitations: The names do not prove the systems are active, reachable, or vulnerable. The Day 4 records for development and staging were stale.
- Recommendation: Review public DNS and certificate records for non-production names, protect those systems to the same standard as production, and remove retired records.

### Finding 2

- Title: Third-Party Mail Vendor Appears in Enumeration
- Evidence: The fictional Amass-style output includes `mx1.mailvendor.test`, while Day 2 also identified `mailvendor.test` in the fictional SPF record.
- Confidence: Probable
- Severity: Informational
- Impact: The records suggest a mail-provider relationship or email-routing dependency. That relationship matters when documenting assets and scope.
- Limitations: The hostname is outside the ACME domain, and the data does not prove who owns or operates the system.
- Recommendation: Keep third-party services in a separate inventory, confirm security responsibilities, and obtain separate written authorization before any testing.

### Finding 3

- Title: Product Names May Reveal Application Hostnames
- Evidence: `cratecloud.acme-training.test`, `routeops.acme-training.test`, and `vendorlink.acme-training.test` match product names shown on the public ACME site.
- Confidence: Possible
- Severity: Informational
- Impact: Matching product and hostname names can help someone map business functions to possible applications.
- Limitations: The product-name match does not prove that any of the hostnames resolve or host those products.
- Recommendation: Keep an approved inventory of product-related hostnames and avoid exposing unnecessary system details in public material.

## 8. False Positives and Assumptions

- All Amass-style results are fictional passive data, not live query results.
- A certificate name may remain visible after a service is retired.
- A DNS record may point to a hosted provider rather than an ACME-owned system.
- `sso` may be a planned or old name, even though the careers page mentions SSO.
- Product-name matches may be naming coincidences.
- Route-derived names are guesses based on paths and are not confirmed DNS names.
- Descriptive names such as `staging` and `legacy` do not prove weak security.
- No hostname in this report was resolved, probed, or tested.

## 9. Defensive Recommendations

- Maintain one approved inventory of public subdomains.
- Monitor certificate records for new or unexpected names.
- Review DNS records regularly and remove stale entries.
- Protect development, QA, and staging systems as carefully as production systems.
- Track identity, VPN, mail, and vendor services separately because they may have different owners.
- Keep third-party services clearly marked so testing does not cross scope boundaries.
- Compare passive findings with internal asset records before calling a system active.
- Avoid exposing environment labels when they are not needed.
- Record the source and date for every hostname finding.

## 10. Evidence Log

| Date | Source or Check | Result | Interpretation |
|---|---|---|---|
| 2026-06-22 | Day 5 fictional Amass-style output | 15 unique normalized names | The list contained 14 fictional ACME names and 1 third-party name. |
| 2026-06-22 | Day 2 DNS and certificate report | DNS, certificate, mail, vendor, legacy, and staging clues reviewed | Earlier records helped raise or lower confidence without proving current activity. |
| 2026-06-22 | Day 3 search OSINT report | Product, route, identity, development, and API terms reviewed | Public content helped explain likely purpose but did not confirm hostnames. |
| 2026-06-22 | Day 4 exposure report | Recent, aging, and stale passive records reviewed | Observation age was considered before describing a name as current. |
| 2026-06-22 | Local ACME route review | `/admin`, `/internal/config`, `/vendor`, `/shipments`, and `/support` reviewed | Matching hostname ideas were labeled as inferred, not confirmed DNS. |

## 11. Knowledge Check

### What is subdomain enumeration?

Subdomain enumeration is the process of finding hostnames that belong under a main domain.

### Why is passive enumeration safer than active enumeration?

Passive enumeration uses information that has already been collected by other sources. It avoids directly probing the target, which lowers the chance of causing problems or crossing an authorization boundary.

### What Amass flag helps keep enumeration passive?

The `-passive` flag, as used in `amass enum -passive -d example.test`.

### Why should third-party names be separated from first-party names?

Third-party systems may have a different owner and are not automatically included in ACME's testing scope.

### Does a discovered hostname prove a service is live?

No. The name may be old, inactive, incorrectly collected, or left behind in certificate history.

### What is the risk of descriptive names like staging, dev, or legacy?

They can reveal how an organization names environments and can point attention toward systems that may deserve further authorized review.

### Why is deduplication important?

It prevents the same name from being counted more than once and makes the final inventory easier to review.

### What is the difference between a confirmed hostname and an inferred hostname?

A confirmed hostname has supporting evidence from an approved source. An inferred hostname is a reasonable guess based on clues such as route names or product names, but it has not been confirmed.

### Why should findings include limitations?

Limitations show what the evidence does not prove. This keeps the report accurate and prevents a lead from being presented as a confirmed problem.

### What defensive process helps reduce stale subdomain exposure?

Keeping an approved asset inventory and regularly reviewing DNS and certificate records helps teams find and remove stale names.
