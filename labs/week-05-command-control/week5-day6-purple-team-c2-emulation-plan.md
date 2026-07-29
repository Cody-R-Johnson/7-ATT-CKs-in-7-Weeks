# ACME Week 5 Day 6 Purple-Team C2 Emulation Plan

## 1. Scope and Safety

This plan was prepared for the July 28, 2026 lab window, between 12:00 PM and 4:00 PM EDT.

Day 6 is planning, coordination, and detection mapping only. No C2 framework, listener, agent, implant, payload, callback, redirector, data transfer, synthetic traffic, tunnel, proxy, or port forward was created or used. No security control was disabled or bypassed.

The local ACME training application and approved repository artifacts are the only confirmed scope. Public infrastructure, real hosts, external networks, and unconfirmed virtual machines remain excluded.

## 2. Purple-Team Emulation Concept

Purple-team C2 emulation is a collaborative exercise where controlled offensive behaviors are modeled so defenders can observe, detect, investigate, and improve controls. The goal is not to avoid detection or "win." The goal is to establish whether defenders can identify the host, process, destination, timing, relevant telemetry, and safe response actions.

Day 6 produces a written tabletop plan only.

## 3. Current Readiness

| Component | Status | Day 6 Meaning |
|---|---|---|
| Source/operator host | Not confirmed | No execution |
| Target VM | Not confirmed | No agent or test process |
| C2 server | Not confirmed | No listener |
| Redirector | Not deployed | No forwarding |
| Protocol | Not authorized | No traffic |
| Logging stack | Not confirmed | No telemetry validation |
| Synthetic dataset | Simulation only | No data transfer |
| Detection rules | Planned only | Not tested |
| Written hands-on authorization | Not confirmed | No exercise window scheduled |

Decision: no hands-on C2 emulation will occur until source, target, C2 server, protocol, logging, authorization, stop condition, and cleanup are confirmed.

## 4. Roles and Responsibilities

| Role | Responsibility | Assigned? |
|---|---|---|
| Exercise owner | Authorizes scope, schedule, assets, techniques, and stop conditions | Placeholder only |
| Red-team operator | Performs only explicitly approved future lab actions | Placeholder only |
| Blue-team analyst | Monitors alerts, logs, and telemetry; records detection outcome | Placeholder only |
| Detection engineer | Creates or tunes future detection logic from agreed evidence | Placeholder only |
| System owner | Confirms lab stability, snapshots, and cleanup approval | Placeholder only |
| Scribe | Records timeline, decisions, artifacts, and lessons learned | Placeholder only |

No real people are assigned by this planning document.

## 5. Simulated Event Cards

**All cards are tabletop-only. No event was generated.**

| Event ID | Simulated Behavior | Expected Defender Question |
|---|---|---|
| C2-SIM-01 | Hypothetical listener starts on a future lab C2 server | Which process opened the port? |
| C2-SIM-02 | Hypothetical target check-in repeats periodically | Is the timing regular or unexpected for the host? |
| C2-SIM-03 | Hypothetical activity change follows a check-in | Did byte volume, endpoint process activity, or related telemetry change? |
| C2-SIM-04 | Hypothetical redirector forwards lab traffic | Do edge and backend records correlate? |
| C2-SIM-05 | Hypothetical synthetic-data pattern is discussed | Would DLP, proxy, firewall, or EDR show the expected simulated indicators? |
| C2-SIM-06 | Hypothetical cleanup action occurs | Did the listener close and were temporary artifacts removed while logs remained? |

## 6. Detection Mapping

| Simulated Behavior | Data Sources | Detection Goal |
|---|---|---|
| Listener start | Process logs, socket state, firewall state | Identify a new listening service |
| Agent launch | EDR, process tree, file-creation events | Identify an unexpected process and parent relationship |
| Beacon-like timing | Firewall, proxy, DNS, and flow records | Identify periodic communication for triage |
| Activity change after check-in | Network flow and endpoint command/process evidence | Correlate timing, volume, and host context |
| Redirector forwarding | Redirector records, backend records, and flow records | Match edge and backend traffic within the lab |
| Synthetic-data pattern | DLP, proxy, EDR, firewall, and SIEM | Identify a data-movement pattern without moving real data |
| Cleanup | File deletion, process termination, and snapshot records | Verify recovery and artifact removal |

## 7. Communications Plan

| Item | Plan |
|---|---|
| Exercise window | Future date/time only after written authorization and lab confirmation |
| Notification channel | Approved lab-only coordination channel |
| Start message | `Exercise start: C2 simulation only` |
| Stop word | `ACME-STOP` |
| Escalation contact | Named exercise owner after assignment |
| Evidence location | Approved lab report directory |
| Status cadence | At each approved phase transition |
| Emergency stop | Any participant may call `ACME-STOP` |
| Closeout message | Confirm stop, cleanup status, evidence preservation, and lessons-capture start |

No live exercise window is scheduled by this plan.

## 8. Success Criteria

Day 6 success is documentation quality and a correctly enforced no-go decision.

Future hands-on success criteria, after authorization, could be:

| Area | Success Criteria |
|---|---|
| Scope | All hosts, accounts, protocol, and allowed actions are confirmed |
| Containment | No public or non-lab route is exposed |
| Visibility | Defenders identify source, destination, process, and timing |
| Correlation | Endpoint and network evidence align with the tabletop event card |
| Response | Stop condition is honored immediately and evidence is preserved |
| Cleanup | Listener is closed, temporary artifacts removed, and snapshots recovered when needed |
| Reporting | Findings and lessons are documented without secrets or unsupported claims |

## 9. Stop Conditions

Stop immediately if:

- A system, account, protocol, route, or asset is unconfirmed.
- Traffic would leave the isolated lab.
- A public IP address or external domain appears.
- A credential, token, key, or session value appears.
- A payload or agent would persist unexpectedly.
- A control would need to be disabled or logs would need to be cleared.
- The exercise produces unexpected network volume or unstable host behavior.
- Any participant says `ACME-STOP`.

## 10. Findings and Observations

### W5-O06: Hands-On Purple-Team C2 Emulation Deferred

- Classification: No-go readiness observation
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - No source host, target VM, C2 server, redirector, approved protocol, or logging stack is confirmed.
  - Days 1–5 deferred deployment, listener, redirector, beaconing, and data movement.
  - No defensive telemetry-validation environment is available.
- Impact: Running an emulation without these prerequisites could create unauthorized traffic, uncontrolled artifacts, or misleading detection results.
- Limitation: No detection rule or response workflow was tested.
- Recommendation: Conduct tabletop planning only until an isolated lab, written authorization, agreed telemetry sources, stop conditions, cleanup procedures, and assigned participants are confirmed.

## 11. Rejected Activities

| Rejected Activity | Reason |
|---|---|
| Start a listener | No C2 server or lab-only bind interface |
| Launch an agent | No target VM or payload authorization |
| Generate callbacks | No listener, route, or logging stack |
| Test redirector | No redirector or backend |
| Simulate exfiltration with real data | Real data movement is prohibited |
| Use public endpoint | Public infrastructure is excluded |
| Tune detection through stealth testing | Evasion optimization is prohibited |
| Disable EDR or logging | Security-control disabling is prohibited |

## 12. Cleanup and Recovery

No cleanup was required because Day 6 created no operational C2 component, data artifact, network flow, process, or configuration.

Future authorized cleanup must verify the exercise has stopped, listener is closed, agent terminated, payload removed, redirector rule removed, synthetic artifacts removed, logs preserved, snapshots restored when needed, no public route was exposed, and the final timeline is complete. Logs and shell history must not be cleared.

## 13. Evidence Log

| Date/Time | Location | Action | Purpose | Result | State Changed? | Cleanup |
|---|---|---|---|---|---|---|
| 2026-07-28 12:09 PM EDT | Week 5 Days 1–5 plans | Readiness review | Confirm whether a hands-on emulation can proceed | Source, target, C2 server, protocol, logging, and authorization remain unconfirmed | No | None |
| 2026-07-28 12:47 PM EDT | Day 6 plan | Role and communications design | Define safe future coordination | Placeholder roles, stop word, escalation, and cadence recorded | No | None |
| 2026-07-28 1:36 PM EDT | Day 6 plan | Tabletop event-card design | Model observable behaviors without generating them | Six fictional event cards recorded | No | None |
| 2026-07-28 2:24 PM EDT | Day 6 plan | Detection and success-criteria mapping | Define future defensive evaluation | Data-source and success mappings recorded | No | None |
| 2026-07-28 3:11 PM EDT | Day 6 plan | Stop-condition and cleanup review | Preserve safe no-go boundary | No operational activity or artifacts created | No | None |

## 14. Knowledge Check

1. **What is purple-team C2 emulation?** A collaborative exercise that models controlled behaviors so defenders can observe, detect, investigate, and improve controls.
2. **Why is the goal detection improvement rather than stealth?** The exercise measures visibility, correlation, response, and safe recovery rather than adversary success.
3. **What does the exercise owner authorize?** Scope, schedule, systems, techniques, and stop conditions.
4. **What does the blue team monitor?** Alerts, logs, network evidence, endpoint telemetry, and response actions.
5. **Why are simulated event cards useful?** They provide a safe, repeatable way to discuss expected evidence and defender questions without generating activity.
6. **Why is a communications plan required?** To coordinate authorization, phase transitions, escalation, evidence handling, and emergency stops.
7. **What is a stop word?** A clear shared signal that immediately ends the exercise; this plan uses `ACME-STOP`.
8. **Why should any participant be able to stop the exercise?** Safety, scope, and system stability override exercise progress.
9. **What evidence is required before launching an agent?** A confirmed isolated target, written authorization, approved payload controls, logging, stop condition, and cleanup plan.
10. **What evidence is required before starting a listener?** A confirmed C2 server, lab-only interface, approved protocol, logging, containment, stop condition, and cleanup plan.
11. **Why is a logging stack required before hands-on testing?** So defenders can validate visibility and correlate endpoint, network, and server evidence.
12. **Why is public infrastructure excluded?** It expands the exercise outside the controlled lab boundary.
13. **Why is real data movement prohibited?** It can expose sensitive information and create unauthorized external traffic.
14. **What must cleanup verify?** Terminated components, removed temporary artifacts, preserved logs, restored snapshots where needed, no public exposure, and a complete timeline.
15. **What is the safe Day 6 result?** A tabletop-only purple-team plan with a confirmed no-go for hands-on emulation.
