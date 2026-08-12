# ACME Week 6 Day 6 Final Campaign Tabletop

## 1. Executive Summary

This document captures the Week 6 Day 6 final tabletop campaign review for ACME. The exercise walks through the campaign from authorization through closeout using only prior evidence, fictional emulation context, and disciplined no-go decisions.

The objective is not to execute a live operation. The objective is to validate campaign sequencing, evidence handling, decision gating, and defender-planning questions while preserving scope, safety, and evidence control.

## 2. Scope and Safety

Scope:
- Prior ACME evidence only.
- Tabletop execution only.
- Simulated decisions and evidence review.
- Month-level Week 6 campaign review.

Safety:
- No new recon, scanning, or exploitation replay.
- No credential testing, session testing, or payload generation.
- No C2 deployment, listener startup, or traffic generation.
- No real data movement or public infrastructure activity.
- Stop word remains `ACME-STOP`.

## 3. Tabletop Campaign Flow

| Phase | Activity | Expected Decision |
|---|---|---|
| 0. Authorization Review | Confirm ROE, stop word, and scope | Go for tabletop only |
| 1. Evidence Brief | Review Weeks 1–5 evidence | Go for evidence synthesis |
| 2. Emulation Profile | Review `ACME-SIM-ADV-01` | Go for fictional profile only |
| 3. Attack Path Walkthrough | Review SQLi, XSS, post-exploitation, and C2 paths | Go for planning only |
| 4. Detection Validation | Review simulated detection cards | Go for tabletop only |
| 5. Risk Review | Confirm no-go conditions | No-go for live testing |
| 6. Closeout | Summarize decisions and lessons | Complete |

## 4. Phase 0: Authorization Review

Questions:
- Is this tabletop-only? Yes.
- Is `ACME-STOP` active? Yes.
- Are public systems excluded? Yes.
- Are live techniques prohibited? Yes.
- Are credentials and secrets excluded? Yes.

Decision:

```
Go for tabletop planning only. No live testing authorized.
```

## 5. Phase 1: Evidence Brief

Evidence areas reviewed:

| Evidence Area | Campaign Use |
|---|---|
| Week 1 recon | Local app exposure context |
| Week 2 assessment | Control and route review |
| Week 3 exploitation | Controlled SQLi and stored-XSS evidence |
| Week 4 post-exploitation | Host/domain readiness gaps |
| Week 5 C2 | C2 readiness gaps |
| Week 6 Days 1–5 | Operation plan, profile, paths, timeline, detection plan |

Decision:

```
Go for evidence synthesis. No replay or expansion.
```

## 6. Phase 2: Emulation Profile Review

The fictional profile is:

```
ACME-SIM-ADV-01 is fictional, tabletop-only, and evidence-bound.
```

The profile supports campaign planning, not attribution or real-world action.

Decision:

```
Go for fictional profile use only. No real actor attribution.
```

## 7. Phase 3: Attack Path Walkthrough

| Path | Tabletop Result |
|---|---|
| Path A: Web exposure to SQLi | Supports controlled application-layer SQLi finding only |
| Path B: Support form to stored XSS | Supports controlled stored-XSS finding only |
| Path C: Web finding to post-exploitation | Deferred; no host/domain lab |
| Path D: C2 readiness path | Deferred; no C2 lab |

Decision:

```
Go for attack-path discussion only. No execution.
```

## 8. Phase 4: Detection Validation Review

Simulated detection cards reviewed:

| Card | Tabletop Outcome |
|---|---|
| DET-SIM-01 | SQLi visibility question defined |
| DET-SIM-02 | XSS submission visibility question defined |
| DET-SIM-03 | Unsafe rendering visibility question defined |
| DET-SIM-04 | Authorization monitoring question defined |
| DET-SIM-05 | Fake secret classification question defined |
| DET-SIM-06 | C2 no-go gate validated |
| DET-SIM-07 | Public infrastructure escalation validated |

Decision:

```
Go for simulated detection planning only. No alerts triggered.
```

## 9. Phase 5: Risk Review

| Risk | Tabletop Decision |
|---|---|
| Scope creep | Controlled by ROE and `ACME-STOP` |
| Unsupported claims | Controlled by evidence labels |
| Credential exposure | Controlled by no-value-retention rule |
| C2 exposure | No-go because lab missing |
| Host/domain overreach | No-go because hosts missing |
| Data exposure | No-go because real data movement prohibited |
| Detection overclaiming | Controlled by simulated/observed distinction |

Decision:

```
No-go for live testing. Continue documentation only.
```

## 10. Phase 6: Closeout

Closeout statement:

```
Week 6 Day 6 tabletop campaign completed. No live technical activity occurred. The campaign successfully walked through authorization, evidence review, fictional adversary profile, attack-path planning, detection validation, risk review, and closeout while preserving scope and safety boundaries.
```

## 11. Findings and Observations

### W6-O06: Final Campaign Tabletop Completed Without Live Execution
- Classification: Planning control
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - Week 6 Day 1 established tabletop-only ROE.
  - Week 6 Day 2 defined a fictional adversary profile.
  - Week 6 Day 3 mapped attack paths without execution.
  - Week 6 Day 4 defined phase gates and communications.
  - Week 6 Day 5 defined simulated detection validation.
- Impact:
  - The team can rehearse campaign decision-making, evidence discipline, and defensive questions without creating unauthorized activity.
- Limitation:
  - No live control, telemetry, response workflow, or technical path was validated.
- Recommendation:
  - Use the tabletop results to define future isolated-lab requirements before any hands-on campaign execution.

## 12. Decisions and No-Go Gates

| Decision Point | Outcome | Basis |
|---|---|---|
| Tabletop authorization | Go | ROE confirmed |
| Live testing | No-go | Infrastructure and authorization missing |
| SQLi/XSS replay | No-go | Replay prohibited |
| Host/domain activity | No-go | Linux, Windows, AD labs missing |
| C2 activity | No-go | C2 server, target, protocol, logging missing |
| Data movement | No-go | Real data movement prohibited |
| Detection validation | Tabletop only | No telemetry stack confirmed |
| Public infrastructure | No-go | Excluded scope |

## 13. Lessons Learned

- Evidence labels prevent overclaiming.
- No-go decisions are operational controls.
- SQLi/XSS findings remain application-layer only.
- Host/domain work needs isolated infrastructure.
- C2 work needs stronger containment and telemetry.
- Detection plans must distinguish simulated from observed.
- Communications templates and `ACME-STOP` preserve safety.

## 14. Cleanup and Evidence Handling

- Preserve this final tabletop report and all prior Week 6 artifacts.
- Maintain the evidence-bound decision trail.
- Record all no-go decisions and scope limits.
- Do not create new technical activity.
- Keep the stop word active for any future campaign work.

## 15. Evidence Log

- Week 6 Day 1 operations plan and ROE.
- Week 6 Day 2 adversary-emulation profile.
- Week 6 Day 3 attack-path control map.
- Week 6 Day 4 operational timeline and communications plan.
- Week 6 Day 5 purple-team detection validation plan.
- Day 6 final tabletop review.

## 16. Knowledge Check

1. What is a campaign tabletop?
   - A structured operational walkthrough using prior evidence and decision gates without live execution.

2. Why is Day 6 not a live exercise?
   - Because the plan is limited to evidence review, simulated decisions, and no-go controls.

3. What does Phase 0 confirm?
   - Scope, ROE, stop-word status, and the prohibition on live testing.

4. Why is evidence review a separate phase?
   - Because prior evidence must be confirmed before any campaign assumptions are accepted.

5. Why does `ACME-SIM-ADV-01` remain fictional?
   - Because it is a training profile derived from prior documented evidence, not a real-world actor attribution.

6. Why are SQLi and XSS discussed but not replayed?
   - Because the campaign is limited to evidence review and planning, not technique execution.

7. Why are host/domain paths no-go?
   - Because the required isolated host and AD infrastructure is not confirmed.

8. Why are C2 paths no-go?
   - Because a live C2 lab, listener, protocol, and telemetry stack are not available.

9. Why is detection validation tabletop-only?
   - Because no telemetry stack or authorized test environment was confirmed.

10. What is the role of `ACME-STOP`?
   - It halts activity immediately and preserves safety and scope control.

11. Why are no-go gates useful?
   - They stop scope creep, unsupported claims, and risky activity before execution begins.

12. Why should lessons learned include limitations?
   - Because limitations explain what remains unvalidated and what must be confirmed before live work.

13. What does closeout confirm?
   - That the campaign ended without live technical activity and that all decisions were documented.

14. What must change before a live campaign?
   - Isolated lab infrastructure, authorization, telemetry, evidence preservation, and cleanup processes.

15. What is the safe Day 6 result?
   - A completed tabletop campaign that stays within scope, documents decisions, and preserves safety without executing any technique or generating telemetry.
