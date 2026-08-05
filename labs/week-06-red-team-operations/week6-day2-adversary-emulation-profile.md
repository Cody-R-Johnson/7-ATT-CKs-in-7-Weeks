# ACME Week 6 Day 2 Threat Model and Adversary-Emulation Profile

**Theme:** Building an emulation profile without performing new activity
**MITRE ATT&CK context:** Resource Development (TA0042), Reconnaissance (TA0043), and Initial Access planning
**Mode:** Tabletop planning only

## 1. Executive Summary

This document defines `ACME-SIM-ADV-01`, a fictional, evidence-bound adversary-emulation profile for the local ACME training lab. It organizes the confirmed findings and no-go decisions from Weeks 1–5 into a restrained campaign narrative so defenders can assess visibility, controls, and response readiness.

No new technical activity was performed for this profile. It does not authorize or include scanning, exploitation replay, credential testing, payload creation, command-and-control (C2), host activity, lateral movement, persistence, evasion, or public-facing activity.

## 2. Profile Summary

| Field | Profile |
|---|---|
| Name | ACME-SIM-ADV-01 |
| Type | Fictional tabletop adversary |
| Motivation | Demonstrate how prior lab findings could be organized into a campaign narrative |
| Primary objective | Access exposed training functionality and test defender visibility |
| Secondary objective | Identify readiness gaps for host, AD, C2, and response validation |
| Scope | Local ACME app and prior reports only |
| Exclusions | Public systems, real organizations, real users, and production infrastructure |
| Operational mode | Tabletop only |

## 3. Scope and Safety

The profile is limited to the local ACME application, this repository, and the evidence already documented in the training program. The Week 6 Day 1 tabletop operation plan and the repository Rules of Engagement remain the controlling scope and stop-condition references.

No live emulation is authorized by this document. Any future execution requires explicit authorization, isolated infrastructure, defined targets, safe test procedures, appropriate telemetry, and confirmed stop conditions.

## 4. Confirmed Evidence Available

| Evidence Area | Confirmed Source | Use in Profile |
|---|---|---|
| Recon context | Week 1 reports | Review prior passive recon and application mapping only |
| Vulnerability context | Week 2 reports | Review previously documented routes and controls only |
| Exploitation context | Week 3 controlled SQLi and stored-XSS findings | Support a controlled initial-access hypothesis; do not replay findings |
| Post-exploitation gaps | Week 4 no-go reports | Explain why host and domain activity are deferred |
| C2 gaps | Week 5 no-go reports | Explain why operational C2 is deferred |
| Current operation boundary | Week 6 Day 1 operation plan | Maintain tabletop-only scope and safety controls |

Confirmed evidence is prior, documented lab evidence. The profile introduces no new hosts, accounts, domains, vulnerabilities, or observed telemetry.

## 5. Campaign Narrative

ACME-SIM-ADV-01 is a fictional tabletop adversary used to organize prior ACME training evidence into an emulation profile. The profile begins with previously collected passive recon and web-application mapping, then references the controlled SQLi and stored-XSS findings validated in the local lab. The profile does not extend to host access, AD activity, C2 deployment, or data exfiltration because the required isolated lab infrastructure and authorization are not confirmed.

## 6. Technique Mapping

| Campaign Phase | ATT&CK Context | Evidence Basis | Status |
|---|---|---|---|
| Recon review | TA0043 | Week 1 passive recon | Confirmed prior evidence |
| Vulnerability review | TA0043 | Week 2 assessment | Confirmed prior evidence |
| Initial-access hypothesis | TA0001 | Week 3 SQLi/XSS lab findings | Controlled lab evidence |
| Post-exploitation planning | TA0008 | Week 4 no-go decisions | Deferred |
| C2 planning | TA0011 | Week 5 no-go decisions | Deferred |
| Reporting and coordination | TA0042 | Week 6 Day 1 plan | Confirmed planning |

These are high-level tactic contexts, not claims that specific real-world procedures were performed. A hypothetical behavior is a future consideration only; it is neither confirmed nor approved for execution.

## 7. Allowed Emulated Behaviors

Allowed behaviors are written descriptions only:

- Review prior passive-recon findings.
- Review previously documented routes and controls.
- Reference the previously validated, controlled SQLi and stored-XSS lab findings.
- Describe why host and domain activity are deferred.
- Describe why operational C2 is deferred.
- Map expected defender questions.
- Summarize risks, limitations, and future validation needs.

## 8. Prohibited Behaviors

The following are prohibited for Day 2:

- New reconnaissance or public OSINT collection.
- Scanning, vulnerability probing, credential guessing, phishing, or social engineering.
- Payload creation or exploit replay.
- C2 deployment, listener startup, redirector deployment, or beacon traffic.
- Data movement, lateral movement, persistence, evasion, or control bypass.
- Claims of real threat-group impersonation or attribution.

## 9. Detection Questions by Phase

| Phase | Defender Question |
|---|---|
| Recon review | What public or local evidence would identify exposed training routes? |
| Vulnerability review | Which routes and controls showed positive or negative security signals? |
| Exploitation reference | Which prior lab requests demonstrated SQLi/XSS safely? |
| Post-exploitation readiness | What missing lab conditions block host/domain validation? |
| C2 readiness | What missing infrastructure blocks listener, beacon, redirector, or exfiltration validation? |
| Reporting | Are claims tied to evidence and limitations? |

## 10. Control Mapping

| Control Area | Relevance |
|---|---|
| Input validation | SQLi and XSS findings |
| Output encoding | Stored-XSS safe table versus unsafe preview |
| Authentication | Portal login and logout handling |
| Authorization | Role and protected-route behavior |
| Credential handling | No live credential exposure confirmed |
| Network containment | Blocks unsafe host/C2 activity |
| Logging and telemetry | Required for future validation |
| Evidence handling | Prevents overclaiming and secret retention |

## 11. Findings and Observations

### W6-O02: Fictional Adversary Profile Limited to Prior Evidence

- Classification: Planning control
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - Week 6 Day 1 established tabletop-only scope.
  - Confirmed evidence exists from Weeks 1–5.
  - Host, AD, C2, and public infrastructure remain unconfirmed or excluded.
- Impact: The emulation profile can support campaign planning and detection questions without creating unauthorized activity.
- Limitation: No new technique execution or detection validation occurred.
- Recommendation: Keep `ACME-SIM-ADV-01` fictional and evidence-bound until isolated infrastructure, authorization, and telemetry are confirmed.

## 12. Risk Register Additions

| Risk | Cause | Control |
|---|---|---|
| Threat-profile overreach | Claiming real actor behavior without evidence | Use a fictional profile only |
| Technique overmapping | Mapping untested techniques as confirmed | Separate confirmed, deferred, and hypothetical behaviors |
| Scope expansion | Turning narrative into live testing | Apply the Day 1 ROE and ACME-STOP |
| Misleading defenders | Simulated events treated as observed telemetry | Label all tabletop events clearly |
| Unsafe public attribution | Naming real groups without sources or authorization | Avoid real actor names |

## 13. Cleanup and Evidence Handling

No tools were run and no technical artifacts were created, so no operational cleanup is required. Retain this document as planning evidence only. Keep future evidence sanitized, tied to its source, and free of real credentials, secrets, customer data, or unverified claims.

## 14. Evidence Log

| Item | Source | Status | Notes |
|---|---|---|---|
| Passive recon and application mapping | Week 1 reports | Confirmed prior evidence | Reviewed as prior evidence only |
| Routes and security controls | Week 2 reports | Confirmed prior evidence | No new assessment activity |
| Controlled SQLi and stored-XSS findings | Week 3 reports | Controlled lab evidence | Referenced; not replayed |
| Host/domain activity decision | Week 4 no-go reports | Deferred | Required conditions remain unavailable or unconfirmed |
| Operational C2 decision | Week 5 no-go reports | Deferred | No listener, beacon, redirector, or exfiltration activity |
| Tabletop boundary | Week 6 Day 1 operation plan | Confirmed planning | Governs Day 2 scope |

## 15. Knowledge Check

1. **What is adversary emulation?** Modeling an adversary's behavior so defenders can evaluate visibility, controls, and response.
2. **Why is this profile fictional?** It is a lab-only planning exercise and does not have sourced intelligence or authorization to represent a real actor.
3. **Why should real threat groups not be named here?** Naming them without reliable sources and authorization creates misleading attribution claims.
4. **What confirmed evidence supports the profile?** The Week 1–5 reports, including the controlled Week 3 SQLi/XSS findings and the Week 4–5 no-go decisions, plus the Week 6 Day 1 plan.
5. **What is the difference between confirmed, deferred, and hypothetical behavior?** Confirmed is documented prior evidence; deferred is intentionally not performed because conditions are missing; hypothetical is a future possibility that is neither observed nor authorized.
6. **Why is SQLi/XSS included but host access excluded?** SQLi/XSS was controlled and validated in the local lab; host access requires infrastructure and authorization that are not confirmed.
7. **Why is C2 excluded from execution?** The isolated infrastructure and authorization needed for operational C2 are not confirmed.
8. **Why should detection questions be evidence-bound?** They should test visibility against known facts, not create unsupported assumptions or claims.
9. **What does technique overmapping mean?** Representing untested ATT&CK techniques as though they were confirmed behaviors.
10. **Why is public attribution risky?** It can falsely associate real people or groups with activity and encourage unsupported conclusions.
11. **Why is no new recon allowed today?** Day 2 is a tabletop planning exercise limited to prior evidence.
12. **Why should simulated events be labeled clearly?** To prevent them from being mistaken for observed telemetry or real incidents.
13. **What controls relate to the Week 3 findings?** Input validation, output encoding, authentication, authorization, logging, telemetry, and evidence handling.
14. **What conditions must change before this profile can support live emulation?** Explicit authorization, isolated lab infrastructure, defined safe procedures, adequate telemetry, and confirmed stop conditions.
15. **What is the safe Day 2 result?** A fictional, evidence-bound tabletop emulation profile with no new technical activity.
