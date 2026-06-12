# Program Plan

## Mission

**7 ATT&CKs in 7 Weeks** is a **7-week red-team learning course** built around a fictional company, ACME. The goal is to practice disciplined offensive security workflows in a safe, local environment while documenting observations like a professional assessment.

## Design Goals

1. **Local first:** the target runs on `127.0.0.1` with no external dependencies.
2. **Repeatable:** each week has a consistent plan, evidence folder, and reporting prompt.
3. **ATT&CK aligned:** exercises are mapped to high-level MITRE ATT&CK tactics without encouraging unauthorized activity.
4. **Tool-aware but safe:** named tools are treated as learning aids and must be pointed only at local or explicitly authorized systems.
5. **Documentation heavy:** the win condition is not just finding issues; it is explaining risk, impact, and remediation.

## 7-Week Learning Course

| Week | Focus Area | Core Skills | Primary Tools | Outcome |
| --- | --- | --- | --- | --- |
| 1 | Reconnaissance | OSINT, domain research, infrastructure mapping | Amass, Shodan, WHOIS, Google dorking | Build a target profile ethically |
| 2 | Vulnerability Assessment | Network/web scanning, false-positive review | Nmap, OWASP ZAP, Nikto | Identify and validate weaknesses |
| 3 | Exploitation | Lab exploitation, chaining vulnerabilities | Metasploit, Burp Suite | Exploit controlled lab targets safely |
| 4 | Post-Exploitation | Privilege escalation, lateral movement concepts | BloodHound, Mimikatz, LinPEAS/WinPEAS | Understand impact after compromise |
| 5 | Command & Control | C2 architecture, covert channels, detection awareness | Empire, Mythic | Learn C2 concepts in a lab |
| 6 | Red Team Operations | Campaign planning, adversary emulation | ATT&CK, Atomic Red Team | Run a structured red-team simulation |
| 7 | Advanced Evasion | Defense evasion concepts, LOLBins, detection engineering | Sysinternals, LOLBins, custom scripts | Understand evasion and blue-team detection |

## Suggested Weekly Cadence

1. Read the weekly objective.
2. Start the ACME site with `./scripts/run_acme.sh`.
3. Confirm the local-only scope before running any tool.
4. Perform local-only discovery, testing, or analysis.
5. Save screenshots, command output, and notes under the week's `evidence/` folder.
6. Write a short finding or after-action review.

## Deliverables Per Week

- Scope statement.
- Tool plan and target list.
- Attack or assessment narrative.
- Evidence list.
- Findings with severity, impact, and remediation.
- Lessons learned.

## Target Overview

ACME is a fictional technology and logistics company. The local site includes:

- Public marketing pages.
- Careers and press content.
- A login page for staff.
- A support request form.
- A vendor lookup portal.
- A deliberately exposed lab notes page.
- Application logs that can be inspected locally.

## Known Lab Accounts

These are fictional and intentionally documented for training:

| Username | Password | Role |
| --- | --- | --- |
| `jane.doe` | `Spring2026!` | Employee |
| `sam.admin` | `ChangeMe123!` | Administrator |
| `vendor.acme` | `VendorPortal2026` | Vendor |

## Important Boundaries

Do not modify this lab to target real third-party services. If you add tooling later, keep it configured for localhost unless you have explicit written authorization for another environment.
