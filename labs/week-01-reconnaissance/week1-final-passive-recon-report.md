# ACME Week 1 Passive Reconnaissance Report

## 1. Executive Summary

During Week 1, I reviewed the local ACME training site and fictional ACME records to learn how passive reconnaissance works. I found public route names, a few clues in JavaScript, descriptive hostnames, possible development and staging names, identity and remote-access leads, and signs of third-party services.

I did not scan public systems, test real domains, guess passwords, exploit the site, or connect to any fictional hostname. Most findings are informational because they came from passive or fictional data. Even so, the findings show how defenders can improve their asset list, remove unnecessary public details, and pay closer attention to portals, APIs, VPNs, and non-production systems.

## 2. Scope and Authorization

The authorized target for Week 1 was the ACME training site at `http://127.0.0.1:8000` and the fictional `acme-training.test` records supplied in the course.

Allowed work included:

- Browsing public pages on the local ACME site.
- Reviewing page source, JavaScript, `robots.txt`, and visible routes.
- Sending simple requests to `127.0.0.1:8000`.
- Reviewing fictional DNS, certificate, Shodan-style, and Amass-style data.
- Organizing findings and giving defensive recommendations.

The following work was not authorized:

- Scanning real domains, public IP addresses, or third-party systems.
- Password guessing, phishing, credential testing, or exploitation.
- Connecting to the fictional hostnames in the course data.
- Testing vendor systems without separate written permission.

## 3. Methodology

I completed the assessment in stages:

1. Defined the local target, allowed methods, and ethical limits.
2. Reviewed the local site's pages, headers, routes, and public files.
3. Studied the supplied DNS and certificate records.
4. Used local content and simulated search queries for search-engine OSINT practice.
5. Reviewed fictional internet-exposure records and their observation dates.
6. Normalized and classified the fictional Amass-style hostname list.
7. Grouped the results by purpose, confidence, priority, and scope.

This was mainly passive work. Direct requests were limited to the authorized local ACME site.

## 4. Key Findings Summary

| ID | Finding | Severity | Priority | Confidence |
|---|---|---|---|---|
| F-01 | Public JavaScript contains internal-looking lab clues | Low | P4 | Confirmed |
| F-02 | `robots.txt` reveals sensitive-looking route names | Informational | P4 | Confirmed |
| F-03 | Passive sources reveal non-production hostnames | Informational | P3 | Probable |
| F-04 | Passive sources identify identity and remote-access leads | Informational | P2/P3 | Probable |
| F-05 | A legacy API name appears in passive records | Informational | P3 | Probable |
| F-06 | Third-party dependency names appear in passive records | Informational | P4 | Probable |
| F-07 | The local ACME server provides detailed banner information | Informational | P4 | Confirmed |

No P1 finding was identified. The work did not confirm a sensitive live exposure or a working vulnerability.

## 5. Asset Summary

| Asset or Group | Category | Evidence | Confidence | Scope Status |
|---|---|---|---|---|
| `127.0.0.1:8000` | Local ACME site | Direct local requests and listener check | Confirmed | In scope |
| `www` and `status` | Public web | DNS, certificate, and Amass-style records | Probable | Passive only |
| `portal`, `vendorlink`, `routeops`, and `cratecloud` | Applications | DNS, certificate, exposure, product, and Amass-style clues | Probable or possible | Passive only |
| `api`, `legacy-api`, and `qa-api` | APIs | DNS, certificate, exposure, and Amass-style clues | Probable or possible | Passive or historical |
| `sso` and `vpn` | Identity and remote access | DNS, certificate, exposure, careers, and Amass-style clues | Probable or possible | Passive only |
| `dev`, `qa-api`, and `staging-portal` | Non-production | DNS, certificate, stale exposure, and Amass-style clues | Probable or possible | Passive or historical |
| `mail.acme-training.test` | Email | MX and Amass-style records | Probable | Passive only |
| `mx1.mailvendor.test`, `status-provider.test`, and `dev-platform.vendor.test` | Third-party services | SPF, CNAME, and Amass-style records | Probable or possible | Out of scope |
| Route-based names such as `admin` and `internal` | Inferred leads | Local ACME route names | Inferred | Unknown |

Except for the local ACME site, these entries were not checked to see if they were live.

## 6. Detailed Findings

### F-01: Public JavaScript Contains Internal-Looking Lab Clues

- Severity: Low
- Priority: P4
- Confidence: Confirmed
- Evidence: `/static/js/site.js` includes `intranet.acme.local`, `/internal/config`, `warehouse-lab`, and `FAKE_ACME_DEMO_KEY_DO_NOT_USE`.
- Impact: In a real site, details like these could help someone understand internal naming and locate interesting paths.
- Limitations: The token is fake and was intentionally added for training. The internal hostname does not prove that an internal service is reachable.
- Recommendation: Review public JavaScript before release and remove internal names, unused configuration values, and token-looking strings.

### F-02: robots.txt Reveals Sensitive-Looking Route Names

- Severity: Informational
- Priority: P4
- Confidence: Confirmed
- Evidence: `/robots.txt` lists `/lab-notes`, `/portal`, `/admin`, and `/internal/config`.
- Impact: These names point visitors toward areas that may look important.
- Limitations: `robots.txt` is meant to guide search engines. It is not supposed to protect private pages, and some listed routes have access controls.
- Recommendation: Use real access controls for private areas and avoid listing routes that do not need to be advertised.

### F-03: Passive Sources Reveal Non-Production Hostnames

- Severity: Informational
- Priority: P3
- Confidence: Probable
- Evidence: The fictional records include `dev.acme-training.test`, `qa-api.acme-training.test`, and `staging-portal.acme-training.test`.
- Impact: The names suggest development, QA, and staging systems. Defenders should make sure those systems receive strong access controls and monitoring if they exist.
- Limitations: The names do not prove that the systems are live or weak. The Day 4 development and staging records were stale.
- Recommendation: Compare the names with the approved asset list and remove old DNS or certificate records when systems are retired.

### F-04: Passive Sources Identify Identity and Remote-Access Leads

- Severity: Informational
- Priority: P2/P3
- Confidence: Probable
- Evidence: `portal.acme-training.test`, `vpn.acme-training.test`, and `sso.acme-training.test` suggest portal, VPN, and sign-in functions.
- Impact: If active, these services could control access to several other systems, so defenders should review them early.
- Limitations: The SSO name has limited evidence, the VPN record is aging, and no login or remote-access service was tested.
- Recommendation: Confirm the assets, require MFA where possible, review login logging, and make sure public access is intentional.

### F-05: A Legacy API Name Appears in Passive Records

- Severity: Informational
- Priority: P3
- Confidence: Probable
- Evidence: `legacy-api.acme-training.test` appears in certificate, TLS-name, and Amass-style data, but not in the current fictional DNS list.
- Impact: An old service name may point to a retired system, migration, or asset that no longer has a clear owner.
- Limitations: The name may only remain in certificate history. It does not prove that a legacy API is active.
- Recommendation: Check ownership and retirement status, then remove old DNS and certificate references when they are no longer needed.

### F-06: Third-Party Dependency Names Appear in Passive Records

- Severity: Informational
- Priority: P4
- Confidence: Probable
- Evidence: The records include `mx1.mailvendor.test`, `status-provider.test`, and `dev-platform.vendor.test`.
- Impact: These names suggest that ACME may depend on outside providers for mail, status, or development services.
- Limitations: The course data does not prove who owns the systems or whether they are still used.
- Recommendation: Keep vendor services in a separate inventory and record ownership, support contacts, and shared security responsibilities.

### F-07: The Local ACME Server Provides Detailed Banner Information

- Severity: Informational
- Priority: P4
- Confidence: Confirmed
- Evidence: The local response included `Server: ACMETrainingHTTP/1.0 Python/3.14.5`.
- Impact: A detailed banner can help someone identify the server type and software version.
- Limitations: The service is bound to `127.0.0.1`, so this evidence does not show public internet exposure. A banner also does not prove a vulnerability.
- Recommendation: Public services should avoid showing unnecessary version details and should still be kept patched and inventoried.

## 7. Infrastructure Map

### Public Web

- `www.acme-training.test`: Probable, passive only.
- `status.acme-training.test`: Probable, passive only, with a third-party hosting clue.

### Applications

- `portal.acme-training.test`: Probable, passive only.
- `vendorlink.acme-training.test`: Possible, passive only.
- `routeops.acme-training.test`: Possible, passive only.
- `cratecloud.acme-training.test`: Possible, passive only.

### APIs

- `api.acme-training.test`: Probable, passive only.
- `legacy-api.acme-training.test`: Probable, historical.
- `qa-api.acme-training.test`: Possible, non-production.

### Identity and Access

- `sso.acme-training.test`: Possible, passive only.
- `vpn.acme-training.test`: Probable, passive only.
- `portal.acme-training.test`: Probable, passive only.

### Non-Production

- `dev.acme-training.test`: Probable, with a vendor boundary.
- `qa-api.acme-training.test`: Possible, passive only.
- `staging-portal.acme-training.test`: Probable, historical.

### Email and Third Party

- `mail.acme-training.test`: Probable, passive only.
- `mx1.mailvendor.test`: Probable, third-party and out of scope.
- `status-provider.test`: Possible, third-party and out of scope.
- `dev-platform.vendor.test`: Possible, third-party and out of scope.

This map groups names by their likely purpose. It does not show confirmed network connections.

## 8. Third-Party and Scope Boundaries

The mail vendor, hosted status provider, and vendor development platform are useful parts of the overall picture, but they are not automatically part of ACME's testing scope. Written permission from the correct owner would be needed before testing any of them.

The same rule applies to fictional ACME hostnames. They can be discussed as course evidence, but they should not be treated as live targets. The only directly tested service during Week 1 was the authorized local site at `127.0.0.1:8000`.

## 9. False Positives and Assumptions

- The domain, DNS, certificate, exposure, and Amass-style records were fictional course data.
- A hostname in several sources may still be inactive.
- Old certificate names can remain visible after a system is retired.
- Stale Shodan-style records do not prove current exposure.
- Product and route names can suggest a hostname without proving it exists.
- Technology terms in a job posting do not prove production use.
- The JavaScript token is an intentional fake training value.
- A vendor record does not prove ACME owns the vendor system.
- Names such as `dev`, `staging`, and `legacy` do not prove weak security.
- No fictional hostname or third-party service was resolved, scanned, or tested.

## 10. Defensive Recommendations

### Asset Inventory

- Keep one approved list of public websites, APIs, portals, VPNs, and vendor services.
- Record each asset's owner, purpose, confidence, and retirement status.
- Compare passive findings with internal records before calling an asset active.

### Public Content

- Review public JavaScript, `robots.txt`, headers, health pages, and job postings.
- Remove internal names, unnecessary technical detail, and token-looking values.
- Use access controls instead of trying to hide private routes.

### Identity and Remote Access

- Review portal, SSO, and VPN assets first because they may control wider access.
- Require MFA where possible.
- Monitor failed logins and unusual access attempts.
- Confirm that public exposure is necessary.

### Non-Production and Legacy Systems

- Review development, QA, staging, and legacy names.
- Remove stale DNS and certificate references.
- Use strong authentication, patching, and monitoring on any system that remains active.

### Third-Party Services

- Keep vendor systems separate from ACME-owned assets.
- Record vendor contacts and shared security responsibilities.
- Review mail protections such as SPF, DKIM, and DMARC.
- Do not test vendor systems without written authorization.

## 11. Evidence Log

| Source | Main Evidence Used | Result |
|---|---|---|
| [Day 1 scope](week1-day1-recon-scope.md) | Authorized local target and ethical limits | Set the boundaries for all Week 1 work |
| [Day 2 domain profile](week1-day2-domain-profile.md) | Local HTTP identity, fictional DNS, certificates, and vendor records | Identified public, legacy, staging, mail, and vendor clues |
| [Day 3 search OSINT](week1-day3-search-osint.md) | Public routes, `robots.txt`, JavaScript, careers, and product names | Identified public content and organization clues |
| [Day 4 exposure intelligence](week1-day4-exposure-intelligence.md) | Five fictional service records and observation dates | Separated recent, aging, and stale passive data |
| [Day 5 subdomain enumeration](week1-day5-subdomain-enumeration.md) | Normalized hostname inventory and source comparison | Separated ACME, third-party, and inferred names |
| [Day 6 infrastructure map](week1-day6-infrastructure-map.md) | Asset groups, priorities, scope, and defensive checks | Created the base for this final report |

## 12. Week 1 Reflection

This week taught me that passive reconnaissance is more than collecting names. The useful part is comparing sources, understanding what a clue may mean, and keeping track of what the evidence does not prove. The most useful clues were the route names, JavaScript values, certificate names, exposure dates, and repeated hostnames across several reports.

The hardest part was using careful wording for old or fictional data. A name such as `staging-portal` sounds important, but it does not mean the service is live or vulnerable. This process would help a defender find missing assets, stale records, and public details that should be reviewed. Before moving into active testing, I would need written authorization that lists the exact systems, methods, accounts, time window, and actions that are allowed.

## 13. Knowledge Check

### Technical Questions

#### What is the difference between passive and active reconnaissance?

Passive reconnaissance reviews information that already exists, such as public pages, search results, certificates, or collected datasets. Active reconnaissance directly sends traffic to a target, such as scanning, probing, or crawling it.

#### Why does scope matter during recon?

Scope explains what I have permission to review and what is off-limits. It helps prevent accidental testing of real people, vendors, or systems.

#### Why is robots.txt not access control?

It only gives instructions to search engines. Anyone can read it, and it does not block access to a listed route.

#### What does Certificate Transparency help reveal?

It can reveal names that appeared on public certificates, including old, staging, or legacy names that may no longer appear in current DNS.

#### Why can Shodan-style data be stale?

It records what was seen at a certain time. A service may move, close, or change after that observation.

#### What is the difference between a confirmed hostname and an inferred hostname?

A confirmed hostname has direct supporting evidence. An inferred hostname is a guess based on a route, product name, or pattern.

#### Why should third-party names be separated from first-party names?

They may have different owners and are not automatically covered by ACME's authorization.

#### Why are dev, qa, staging, and legacy names useful leads?

They may point to non-production or older systems that defenders should check for ownership, strong access controls, and current monitoring.

#### Why does a banner not prove a vulnerability?

A banner only reports information about a service. More evidence would be needed to show that the software has a real, working security problem.

#### Why should recon findings include limitations?

Limitations explain what the evidence does not prove and keep the report from overstating a lead.

### Professional Questions

#### Which finding would you prioritize first for a defender, and why?

I would start with the identity and remote-access leads because a portal, SSO service, or VPN may control access to several other systems. I would first confirm which names are real and whether their exposure is intentional.

#### Which finding had the weakest evidence?

The route-based hostname guesses had the weakest evidence. A route such as `/admin` does not prove that `admin.acme-training.test` exists.

#### Which finding had the clearest scope boundary?

The third-party dependency finding had the clearest boundary because `mailvendor.test`, `status-provider.test`, and `vendor.test` are outside the fictional ACME domain.

#### Where did you avoid overclaiming?

I did not describe stale exposure records as current, did not call a hostname vulnerable because of its name, and did not treat route-based guesses as confirmed DNS records.

#### What would you ask for before moving into Week 2 vulnerability assessment?

I would ask for written rules that name the exact local routes and accounts I can test, the tools and payloads I can use, when testing is allowed, what data I can keep, and which actions must remain off-limits.
