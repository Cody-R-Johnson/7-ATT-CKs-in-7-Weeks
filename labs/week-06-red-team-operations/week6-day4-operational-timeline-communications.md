# ACME Week 6 Day 4 Operational Timeline and Communications Plan

## 1. Executive Summary

This document captures the Day 4 tabletop operational timeline, phase gates, communications templates, escalation triggers, and evidence-bound safety controls for Week 6 red-team planning. It is built only from prior ACME evidence and approved reports, with no live testing or technical execution authorized.

## 2. Scope and Safety

Scope:
- Local ACME application evidence only.
- Prior approved reports and Day 1–Day 3 findings.
- Tabletop planning only, with no new data collection or live system activity.

Safety:
- No recon, scanning, credential testing, payloads, C2 deployment, traffic generation, or lateral movement.
- No production or public infrastructure activity.
- All discussion remains fictional and evidence-bound.
- Stop word: `ACME-STOP`.

## 3. Operational Timeline

| Phase | Purpose | Allowed Activity | Output |
|---|---|---|---|
| Phase 0: Authorization Review | Confirm tabletop scope | Review ROE, scope, stop word | Go/no-go decision |
| Phase 1: Evidence Review | Organize Weeks 1–5 evidence | Summarize prior evidence only | Evidence brief |
| Phase 2: Emulation Profile Review | Validate `ACME-SIM-ADV-01` | Confirm fictional/evidence-bound profile | Profile approval |
| Phase 3: Attack-Path Review | Review Day 3 paths | Confirm labels and rejected chains | Attack-path brief |
| Phase 4: Detection Planning | Map defender questions | Simulate telemetry and detection questions only | Detection-plan notes |
| Phase 5: Risk and Safety Review | Reconfirm constraints | Check no-go gates and controls | Safety register update |
| Phase 6: Closeout | Preserve evidence | Summarize decisions, next steps, and cleanup needs | Timeline and closeout notes |

## 4. Go/No-Go Criteria

| Gate | Go Criteria | No-Go Criteria |
|---|---|---|
| Scope gate | Local ACME/prior evidence only | Any new target or public system |
| Evidence gate | Prior report supports claim | Unsupported or invented claim |
| Technique gate | Tabletop discussion only | Any live technique execution |
| Credential gate | No secret values handled | Credential/token/session appears |
| C2 gate | No infrastructure deployed | Listener, agent, redirector, callback, traffic |
| Data gate | Sanitized/synthetic discussion only | Any real data collection or transfer |
| Host/domain gate | No host/domain execution | Linux, Windows, AD target required |
| Detection gate | Simulated questions only | Claims of observed telemetry without evidence |
| Stop gate | `ACME-STOP` honored immediately | Continued activity after stop |

## 5. Communications Templates

### Start Notice

```
Week 6 tabletop planning started.
Scope: local ACME app evidence and approved reports only.
Mode: no live testing.
Stop word: ACME-STOP.
```

### Phase Transition

```
Phase transition: [PHASE NAME]
Status: tabletop-only
Evidence used: [REPORT OR PRIOR FINDING]
Go/no-go decision: [GO / NO-GO]
Notes: [LIMITATIONS]
```

### Stop Notice

```
ACME-STOP called.
All tabletop activity paused.
No live testing is authorized.
Record reason, time, participants, and next decision.
```

### Closeout Notice

```
Week 6 Day 4 tabletop timeline closed.
No technical activity occurred.
Evidence preserved in approved report directory.
Open items: future lab infrastructure, telemetry, authorization, and cleanup requirements.
```

## 6. Role Coordination

| Role | Day 4 Responsibility | Assigned |
|---|---|---|
| Exercise owner | Approves timeline and phase gates | [TBD] |
| Red-team lead | Confirms claims remain evidence-bound | [TBD] |
| Blue-team lead | Reviews detection questions | [TBD] |
| Detection engineer | Maps future telemetry needs | [TBD] |
| System owner | Confirms no system change occurred | [TBD] |
| Scribe | Records timeline, go/no-go decisions, and closeout | [TBD] |

## 7. Decision Log

| Time | Phase | Decision | Basis | State Changed? |
|---|---|---|---|---|
| 12:05 | Authorization Review | Go for tabletop only | ROE confirmed | No |
| 12:40 | Evidence Review | Go | Prior reports available | No |
| 1:15 | Emulation Profile Review | Go | Fictional profile confirmed | No |
| 1:50 | Attack-Path Review | Go | Paths labeled correctly | No |
| 2:10 | Detection Planning | Go | Simulated questions only | No |
| 2:35 | Safety Review | No-go for live testing | Infrastructure absent | No |
| 2:55 | Closeout | Complete | No technical activity | No |

## 8. Escalation Triggers

Escalate immediately if:

- A new target appears.
- Public infrastructure is proposed.
- A real credential, token, key, cookie, or session appears.
- Someone proposes replaying SQLi or XSS.
- Someone proposes C2, payloads, callbacks, or traffic generation.
- Someone proposes data movement.
- A claim is unsupported by prior evidence.
- Logs or shell history would be cleared.
- Any participant calls `ACME-STOP`.

## 9. Findings and Observations

### W6-O04: Operation Timeline Preserves Tabletop-Only Execution Discipline
- Classification: Planning control
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - Week 6 Day 1 established tabletop-only rules of engagement.
  - Week 6 Day 2 established a fictional, evidence-bound emulation profile.
  - Week 6 Day 3 limited attack paths to prior evidence and readiness gaps.
  - Day 4 phase gates prohibit live technique execution.
- Impact:
  - The operation can proceed through coordinated planning phases without expanding scope or generating unauthorized activity.
- Limitation:
  - No live detection, response workflow, or technical control was tested.
- Recommendation:
  - Keep phase gates and communications templates in place until isolated infrastructure, authorization, telemetry, and cleanup are confirmed.

## 10. Cleanup and Evidence Handling

- Preserve all Day 4 notes and decisions in the approved report directory.
- Do not create or modify live infrastructure.
- Capture all evidence references as citations to prior Week 1–Week 5 reports.
- Maintain the tabletop-only safety record and stop-word log.

## 11. Evidence Log

- Prior evidence: Week 6 Day 1 tabletop rules, Week 6 Day 2 emulation profile, Week 6 Day 3 attack path control map.
- Report references: Week 6 Day 1, Day 2, Day 3 deliverables and approved ACME documentation.
- No new technical evidence was created.

## 12. Knowledge Check

1. What is an operational timeline?
   - A schedule of planning phases, decisions, and outputs used to organize a tabletop operation.

2. Why is Day 4 tabletop-only?
   - Because it focuses on planning, decision points, and controls without live technical activity.

3. What is a phase gate?
   - A decision point that approves or rejects progression to the next planning phase.

4. What is a go/no-go decision?
   - A choice to continue or stop based on safety, evidence, and authorization.

5. Why are communication templates useful?
   - They standardize messages, keep the team aligned, and document phase transitions.

6. What does the stop word do?
   - It pauses all activity immediately and triggers a review before continuing.

7. Why should unsupported claims trigger escalation?
   - Because they can expand scope, introduce risk, or break the evidence-bound plan.

8. Why should SQLi/XSS replay be rejected today?
   - Because live technique replay is not allowed during tabletop-only planning.

9. Why should C2 proposals trigger no-go?
   - Because they require real infrastructure, traffic, and execution outside the approved tabletop scope.

10. Why should real credentials trigger escalation?
   - Because they are sensitive, out of scope, and violate the safe planning boundary.

11. Why is detection planning simulated only?
   - Because no telemetry or response systems are being tested during tabletop planning.

12. What should the scribe record?
   - Timeline, go/no-go decisions, evidence references, stop-word calls, and closeout notes.

13. Why is closeout important?
   - It preserves evidence, confirms no technical activity occurred, and identifies follow-up requirements.

14. What evidence supports W6-O04?
   - Prior Week 6 deliverables and the Day 4 phase gate design that prevents live execution.

15. What is the safe Day 4 result?
   - A completed tabletop timeline and communications plan with no new technical activity.
