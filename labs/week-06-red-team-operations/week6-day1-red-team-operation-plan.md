# ACME Week 6 Day 1 Red Team Operation Plan

## 1. Executive Summary

This plan was prepared for the July 31, 2026 tabletop planning window, between 1:00 PM and 5:00 PM EDT.

The Week 6 operation organizes previously collected ACME training evidence into a safe red-team campaign plan. The confirmed scope remains the local ACME training application and approved repository artifacts. Linux, Windows, Active Directory, C2, redirector, target-VM, public-infrastructure, and production contexts remain unconfirmed or excluded.

No exploitation, scanning, credential testing, C2 deployment, payload creation, listener, lateral movement, persistence, evasion, or new technical testing occurred. The operation is therefore tabletop-only and evaluates readiness, evidence quality, safeguards, and future validation requirements.

## 2. Operation Objective

Evaluate how prior ACME lab findings, positive controls, no-go decisions, and defensive observations can be organized into a safe red-team campaign plan without expanding scope or performing new technical actions.

A future operation objective, after lab confirmation, would assess whether the ACME local training environment is ready for a controlled red-team tabletop covering reconnaissance, vulnerability-assessment context, exploitation evidence, post-exploitation readiness gaps, C2 readiness gaps, and purple-team detection planning.

## 3. Scope and Authorization

| Scope Item | Status | Notes |
|---|---|---|
| Local ACME application at `http://127.0.0.1:8000` | Confirmed | Tabletop and prior-evidence context only |
| Approved repository artifacts | Confirmed | Sanitized reports and lab artifacts only |
| Course reports from Weeks 1–5 | Confirmed | Evidence may be synthesized without replaying activity |
| Fictional ACME data | Confirmed | May be discussed only; no collection or transfer |
| Documented lab accounts | Limited | Use only when already required by prior approved evidence; no guessing or validation today |
| Linux VM | Not confirmed | No privilege testing |
| Windows VM | Not confirmed | No service, token, or host testing |
| AD lab | Not confirmed | No domain queries or relationship collection |
| C2 lab | Not confirmed | No listener, agent, redirector, or traffic |
| Public infrastructure | Excluded | No VPS, cloud, public DNS, CDN, or domain-fronting use |
| Production systems | Excluded | No production or unknown target activity |

## 4. Rules of Engagement

| Rule | Requirement |
|---|---|
| Systems | Local ACME application and approved repository artifacts only |
| Accounts | Documented lab accounts only when prior evidence requires them; no credential guessing |
| Timing | July 31 planning window only |
| Data | Fictional or sanitized evidence only |
| Traffic | No new network traffic except ordinary local app access if separately required; none is required for Day 1 |
| Payloads | None |
| C2 | None |
| Persistence | None |
| Lateral movement | None |
| Evasion | None |
| Evidence | Sanitized, minimal, and free of secret values |
| Logs | Do not clear logs or shell history |
| Stop condition | Stop for unclear authorization, real credential material, external route, unexpected state change, or `ACME-STOP` |

## 5. Stakeholders and Roles

| Role | Responsibility | Assigned |
|---|---|---|
| Exercise owner | Approves scope, timing, systems, and stop conditions | Placeholder |
| Red-team lead | Maintains rules of engagement and evidence quality | Placeholder |
| Operator | Performs only authorized future actions | Placeholder |
| Blue-team lead | Reviews detection opportunities and response questions | Placeholder |
| Detection engineer | Maps telemetry and future analytics | Placeholder |
| System owner | Confirms application state, lab readiness, and cleanup | Placeholder |
| Scribe | Maintains timeline, decisions, evidence, and lessons learned | Placeholder |

No real people are assigned by this plan.

## 6. Communications Plan

| Item | Plan |
|---|---|
| Start notice | `Week 6 tabletop planning started` |
| Stop word | `ACME-STOP` |
| Status cadence | At each candidate phase boundary |
| Escalation | Exercise owner after assignment |
| Evidence location | Approved lab report directory |
| Closeout | Confirm no live testing occurred and summarize decisions |
| Emergency stop | Any participant may call `ACME-STOP` |

## 7. Evidence Handling Rules

Evidence may include finding identifiers, dates, approved routes or artifacts, sanitized proof, impact and limitations, positive controls, no-go decisions, rejected paths, and cleanup status.

Evidence must not include passwords, live cookies, tokens, private keys, real personal data, public-target data, full sensitive response bodies, unnecessary screenshots, or payload/exploit content beyond previously approved minimal lab strings. Record metadata and classification rather than secret values.

## 8. Operational Constraints

| Constraint | Impact |
|---|---|
| No Linux VM | No Linux privilege testing |
| No Windows VM | No Windows service or token testing |
| No AD lab | No domain queries, BloodHound, or relationship mapping |
| No C2 server | No listener or beaconing |
| No target VM | No agent or payload testing |
| No logging stack | No live detection validation |
| No synthetic-data movement authorization | No data staging or transfer |
| Local-only application | Campaign remains tabletop and local |

These constraints define the operation boundary; they are not security findings or failures.

## 9. Candidate Operation Phases

| Phase | Allowed Activity | Output |
|---|---|---|
| Recon review | Summarize Week 1 evidence | Recon context |
| Vulnerability review | Summarize Week 2 findings and positive controls | Assessment context |
| Exploitation review | Summarize Week 3 controlled validation | Validated-lab evidence |
| Post-exploitation readiness | Summarize Week 4 no-go decisions | Host/domain gap analysis |
| C2 readiness | Summarize Week 5 no-go decisions | C2 gap analysis |
| Purple-team planning | Map detection questions from existing reports | Future validation plan |
| Reporting | Consolidate decisions, limitations, and risks | Campaign charter |

## 10. Risk and Safety Register

| Risk | Cause | Control |
|---|---|---|
| Scope creep | Moving from tabletop planning to live testing | Written rules of engagement and stop word |
| Credential exposure | Copying lab secrets into reports | Redaction and no-value-retention rule |
| External contact | Unconfirmed network or public infrastructure | No traffic-generation rule |
| Unsupported claims | Treating no-go gaps as validated findings | Evidence classification and limitations |
| Data exposure | Moving real files or application records | Synthetic-only and no-data-movement rule |
| C2 exposure | Opening infrastructure without isolated lab | C2 no-go gate |
| Misleading detection results | No logging stack or confirmed telemetry | Mark detection models as simulated |

## 11. Findings and Observations

### W6-O01: Red-Team Operation Limited to Tabletop Planning

- Classification: Planning control
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - Confirmed scope is limited to the local ACME application and approved repository artifacts.
  - Week 4 found no confirmed Linux, Windows, or AD lab.
  - Week 5 found no confirmed C2 server, target VM, redirector, protocol, logging stack, or hands-on authorization.
- Impact: The operation can safely synthesize evidence and plan future validation but cannot ethically proceed to host, domain, C2, or lateral-movement execution.
- Limitation: No new technical security control is tested on Day 1.
- Recommendation: Maintain a tabletop campaign until isolated lab infrastructure, written authorization, telemetry, and cleanup procedures are confirmed.

## 12. Cleanup and Evidence Handling

No cleanup was required because no technical action, temporary file, network traffic, credential use, configuration change, or operational artifact was created.

For a future authorized campaign, preserve required logs and evidence, remove only temporary lab artifacts, terminate authorized test components, restore snapshots when appropriate, verify that no external route was exposed, and document the final timeline. Never clear logs or shell history.

## 13. Evidence Log

| Date/Time | Location | Action | Purpose | Result | State Changed? | Cleanup |
|---|---|---|---|---|---|---|
| 2026-07-31 1:08 PM EDT | Weeks 1–5 reports | Evidence-set review | Confirm confirmed targets and constraints | Local app/repository scope retained; host, domain, and C2 gaps confirmed | No | None |
| 2026-07-31 1:47 PM EDT | Day 1 plan | Objective and scope design | Define safe campaign purpose and boundary | Tabletop objective and exclusions recorded | No | None |
| 2026-07-31 2:31 PM EDT | Day 1 plan | Rules and communications design | Establish stop condition and evidence standards | Rules of engagement, stop word, and coordination plan recorded | No | None |
| 2026-07-31 3:18 PM EDT | Day 1 plan | Phase and risk planning | Organize prior evidence without new testing | Candidate phases and safety register recorded | No | None |
| 2026-07-31 4:09 PM EDT | Day 1 plan | No-go and cleanup review | Confirm no operational action is authorized | Tabletop limitation confirmed; no cleanup required | No | None |

## 14. Knowledge Check

1. **What is a red-team operation?** A planned, authorized assessment that evaluates security controls, detection, response, and organizational readiness.
2. **Why is an operation broader than a single vulnerability test?** It coordinates objectives, scope, rules, communications, evidence, safety, and debrief across multiple assessment phases.
3. **What are rules of engagement?** The documented operational boundaries, allowed systems/actions, constraints, stop conditions, and safety requirements for an exercise.
4. **Why is scope control important?** It prevents unauthorized contact, harmful state change, and unsupported conclusions.
5. **Why is Week 6 currently tabletop-only?** The confirmed scope contains only the local application and repository evidence; host, domain, C2, network, and logging prerequisites are absent.
6. **What confirmed evidence can the operation use?** Approved reports and lab artifacts from Weeks 1–5, the local ACME application context, fictional ACME data, positive controls, and no-go decisions.
7. **What systems remain unconfirmed?** Linux, Windows, AD, C2 server, redirector, target VM, isolated network, and public infrastructure.
8. **Why should no new technical actions occur today?** Day 1 is a planning exercise and the required authorization and isolated infrastructure are not confirmed.
9. **Why are no-go decisions useful in an operation plan?** They document due diligence, preserve safety boundaries, and identify exactly what must change before future testing.
10. **What is a stop word?** A clear shared signal that immediately ends the exercise; this plan uses `ACME-STOP`.
11. **Why should evidence be sanitized?** To avoid spreading credentials, tokens, sessions, private data, or unnecessary sensitive content.
12. **Why should unsupported claims be rejected?** Conclusions must remain tied to observed, authorized evidence rather than speculation.
13. **What risks come from opening C2 infrastructure without readiness?** Unauthorized callbacks, exposed listening services, uncontrolled artifacts, external contact, and misleading detection results.
14. **What must be confirmed before future hands-on operation phases?** Isolated assets, written scope, named accounts, approved techniques/protocols, containment, telemetry, stop conditions, cleanup, and rollback controls.
15. **What is the safe Day 1 result?** A documented tabletop operation plan that organizes evidence and preserves the no-go boundary without new technical activity.
