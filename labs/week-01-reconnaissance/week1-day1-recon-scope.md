# Week 1 Day 1 Recon Scope

## 1. Target Overview

The target for Day 1 is the fictional ACME Global Operations training site running locally at `http://127.0.0.1:8000`. ACME is a local-only logistics technology target built for the 7-week red-team learning course. For today, I want to understand the public-facing site, note visible business and technical clues, and define the recon scope before moving into deeper testing.

Primary in-scope assets:

- `http://127.0.0.1:8000/`
- Public ACME pages such as `/about`, `/products`, `/careers`, `/support`, `/vendor`, `/shipments`, `/lab-notes`, `/robots.txt`, and `/health`.
- Static assets served by the local ACME application.
- Repository documentation that describes the intended training environment.

## 2. Authorization Assumptions

This reconnaissance is authorized only for the local training environment in this repository. Testing is limited to services running on `127.0.0.1` that are part of the ACME lab. No real company, third-party service, public IP address, public domain, or external system is authorized unless separate written permission is provided.

Assumptions:

- I have permission to browse and document the local ACME site.
- I have permission to inspect local files in this course repository.
- I do not have permission to scan or test real ACME-like companies, domains, vendors, employees, or infrastructure.
- Any named tools must be configured for localhost or treated as study notes unless explicit authorization expands the scope.

## 3. Allowed Recon Methods

Allowed methods for Day 1:

- Manually browse public ACME pages.
- Review visible links, forms, page titles, text, image names, and navigation.
- Review `robots.txt`, `/lab-notes`, `/health`, and other intentionally exposed local pages.
- Inspect page source and browser developer tools for local assets and comments.
- Record observations in notes and save screenshots or command output under the relevant evidence folder.
- Use simple local commands such as `curl` against `127.0.0.1:8000`.
- Compare findings against the repository documentation and rules of engagement.

## 4. Disallowed Recon Methods

Disallowed methods for Day 1:

- Scanning public IP addresses, real domains, or third-party services.
- Password guessing, credential stuffing, phishing, or social engineering.
- Attempting to access real employee, vendor, or customer accounts.
- Sending payloads to systems outside the local lab.
- Collecting unnecessary personal data.
- Using noisy vulnerability scanners unless they are pointed only at the authorized local target and the exercise specifically calls for them.
- Attempting persistence, exploitation, denial of service, or destructive testing.

## 5. Passive Data Sources You Plan to Use

Planned passive sources:

- ACME public pages exposed by the local site.
- `robots.txt` and the deliberately exposed lab notes.
- Static files such as CSS, JavaScript, image names, and page metadata.
- Repository documentation in `README.md`, `docs/`, and Week 1 lab notes.
- Browser-visible clues such as page titles, forms, route names, and footer links.
- Fictional job postings on the local careers page.
- Public search or Shodan-style examples as study references only unless an explicitly authorized real target is provided later.

## 6. Risks You Expect to Investigate

Expected risks to investigate:

- Accidentally exposed internal routes or training notes.
- Sensitive-looking but fake configuration breadcrumbs.
- Public pages that reveal useful organizational, vendor, or technology context.
- Authentication and role clues visible before login.
- Overly informative health or status endpoints.
- Forms that may become useful in later testing, such as support search or ticket submission workflows.
- Differences between public, employee, vendor, and administrator views once authorized login testing begins.

## 7. Notes on Ethical Boundaries

Recon should stay scoped and documented. I should be able to explain what I looked at, why it was allowed, and what I found without touching unauthorized systems or collecting extra information. If a finding looks sensitive, I should document only what is needed to explain the exposure, avoid collecting more data, and report it through the authorized channel.

Ethical boundaries:

- Stay within the written scope.
- Minimize data collection.
- Do not target real people.
- Do not use discovered information outside the lab.
- Preserve evidence carefully without copying unnecessary sensitive content.
- Stop and ask for clarification if the scope is unclear.

## 8. Knowledge Check

### What is the difference between passive and active reconnaissance?

Passive reconnaissance gathers information without directly interacting with the target system in a way the target would observe, such as reviewing public pages, documentation, search results, or already-collected datasets. Active reconnaissance directly interacts with the target, such as sending requests, probing services, crawling aggressively, or running scans.

### Why is written authorization important?

Written authorization defines what is allowed, what is off-limits, who approved the work, and when the work can happen. It protects everyone involved because the testing has clear rules instead of relying on assumptions.

### Is Shodan passive or active from your perspective?

As a user of Shodan, I would treat it as passive because I am reviewing data Shodan has already collected. From the target side, Shodan's original collection involved active scanning by Shodan infrastructure. Seeing something in Shodan does not give me permission to scan or test that system myself.

### Why can job postings be useful during recon?

Job postings can reveal technologies, cloud providers, operating systems, business processes, team structure, locations, compliance needs, and security tooling. Those details help build a realistic target profile and can point to risks worth checking later.

### What should you do if you discover sensitive personal data during OSINT?

Document the existence of the exposure at a high level, avoid collecting unnecessary personal data, and report it through the proper authorized channel. The point is to reduce harm and keep only the minimum evidence needed to explain the issue.
