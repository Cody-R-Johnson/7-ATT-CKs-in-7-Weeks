# ACME Week 6 Day 5 Purple-Team Validation and Detection Plan

## 1. Executive Summary

This document defines the Day 5 purple-team validation plan for Week 6. It translates prior ACME evidence, attack-path assumptions, and known readiness gaps into defender-focused validation objectives without generating telemetry or conducting live testing.

The purpose of Day 5 is to define what defenders should be able to detect in a future authorized lab, not to claim that those detections have already occurred. The plan remains evidence-bound, simulated, and limited to tabletop activity only.

## 2. Scope and Safety

Scope:
- Prior Week 1–Week 6 evidence only.
- Approved game rules, emulation profile, and attack-path control map.
- Defender validation planning only.

Safety:
- No SQLi replay, XSS replay, or scanning.
- No credential testing or secret handling.
- No listeners, payloads, beacon traffic, or C2 activity.
- No public systems or production activity.
- No claims of observed detection coverage without telemetry.
- Stop word: `ACME-STOP`.

## 3. Detection Validation Inputs

| Input | Source | Use |
|---|---|---|
| Recon and route mapping | Week 1 | Identify exposed routes and expected service surfaces |
| Detection questions for exposed routes | Week 1 | Define defender questions tied to app surfaces |
| Vulnerability assessment | Week 2 | Map likely validation needs for app controls |
| Control and logging review | Week 2 | Identify logging coverage gaps |
| SQLi finding | Week 3 | Model future request-validation alert scenario |
| Stored-XSS finding | Week 3 | Model future content-rendering alert scenario |
| Post-exploitation no-go decisions | Week 4 | Document host and AD readiness limits |
| C2 no-go decisions | Week 5 | Capture C2 telemetry readiness gaps |
| Week 6 profile and attack paths | Days 1–4 | Scope detection mapping and no-go boundaries |
| Campaign-level detection plan | Week 6 | Establish purple-team design and validation criteria |

## 4. Detection Mapping

| Campaign Element | Simulated Behavior | Required Telemetry | Defender Question |
|---|---|---|---|
| Route discovery | Review exposed local routes | Web access logs, app route inventory | Are exposed routes expected? |
| Vendor query input | Prior SQLi lab pattern | App logs, request logs, validation errors | Are unusual query patterns visible? |
| Support ticket submission | Prior stored-XSS lab payload | App logs, form-submission records, moderation queue | Are script-like submissions detected? |
| Ticket rendering | Unsafe preview behavior | Admin access logs, render-path logs, browser telemetry in future lab | Is untrusted content encoded consistently? |
| Authentication | Login/logout flow | Auth logs, session events | Are login, logout, and invalidated-session events visible? |
| Authorization | 403/303 behavior | Web logs, access-control events | Are denied and redirected requests monitored? |
| Credential handling | Fake token/contextual values | Secret-scanning logs, review records | Are fake and real secrets clearly distinguished? |
| Host/domain path | Deferred host/AD testing | EDR, Windows/Linux logs, AD telemetry | What telemetry is missing before validation? |
| C2 path | Deferred listener/beaconing | Firewall, DNS, proxy, endpoint logs | What logging stack is needed before C2 validation? |
| Exfil path | Deferred data movement | DLP, proxy, CASB, firewall, EDR | What controls are needed before synthetic exfil testing? |

## 5. Simulated Detection Cards

These cards are simulated. No detections were triggered.

| Card ID | Scenario | Expected Defender Outcome |
|---|---|---|
| DET-SIM-01 | Prior vendor SQLi pattern appears in request logs | Analyst identifies suspicious input and route |
| DET-SIM-02 | Prior support-ticket script-like content appears | Analyst identifies untrusted content submission |
| DET-SIM-03 | Admin preview renders untrusted content | Analyst checks output encoding and admin path exposure |
| DET-SIM-04 | Repeated denied route access occurs | Analyst reviews authorization controls |
| DET-SIM-05 | Fake config marker appears in review | Analyst classifies it as fake training data |
| DET-SIM-06 | C2 listener proposal appears in planning | Analyst applies no-go gate |
| DET-SIM-07 | Public infrastructure proposal appears | Analyst escalates and rejects scope expansion |

## 6. Detection Success Criteria

| Area | Success Criteria |
|---|---|
| Evidence quality | Detection tied to prior evidence |
| Scope control | No unsupported or live claims |
| Analyst triage | Analyst identifies route, input, user/context, and limitation |
| Correlation | Web, auth, and app evidence can be linked conceptually |
| False positives | Benign or fake lab values are separated from real findings |
| Readiness gaps | Missing host, AD, C2, and DLP telemetry are documented |
| Response | Escalation and `ACME-STOP` are understood |
| Reporting | Simulated events are labeled clearly |

## 7. False Positive Considerations

| Signal | Possible False Positive |
|---|---|
| SQL-like text in request | Training input, search strings, documentation |
| Script-like content | Markdown examples, code snippets, help tickets |
| Denied route access | Normal unauthenticated browsing |
| Fake config marker | Explicit training marker |
| Periodic traffic | Updaters, monitoring, EDR, sync tools |
| Data movement alert | Backup, cloud sync, admin transfer |
| Credential-like word | Field name or documentation label |

A detection candidate is not a confirmed incident without context.

## 8. Findings and Observations

### W6-O05: Detection Validation Limited to Tabletop Scenarios
- Classification: Planning control
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - Week 6 Day 4 established phase gates and tabletop-only communications.
  - Week 6 Day 3 limited attack paths to prior evidence and readiness gaps.
  - No live telemetry stack, target VM, C2 lab, host lab, AD lab, or DLP test environment is confirmed.
- Impact:
  - The team can define detection objectives and success criteria, but cannot claim validated detection coverage.
- Limitation:
  - No alerts, logs, telemetry, or response workflows were triggered or tested today.
- Recommendation:
  - Keep detection validation simulated until isolated infrastructure, telemetry sources, written authorization, stop conditions, and cleanup procedures are confirmed.

## 9. Rejected Validation Actions

| Rejected Action | Reason |
|---|---|
| Replay SQLi request | Live technique execution prohibited today |
| Replay XSS payload | Live technique execution prohibited today |
| Generate fake attacks in logs | No telemetry test environment confirmed |
| Create C2 beacon traffic | C2 lab remains unconfirmed |
| Trigger DLP with real data | Real data movement prohibited |
| Use public endpoints | Public infrastructure excluded |
| Disable alerting to test response | Security-control disabling prohibited |
| Tune detections around stealth | Evasion optimization prohibited |
| Claim detections were observed | No telemetry was generated |

## 10. Future Validation Requirements

| Validation Area | Requirement Before Testing |
|---|---|
| SQLi detection | Written authorization, local route, logging, strict request limits |
| XSS detection | Safe browser context, logging, no session/token capture |
| Auth detection | Documented lab accounts, app logs, no credential guessing |
| Host telemetry | Isolated Linux/Windows VM, EDR/logging, snapshot |
| AD telemetry | Isolated AD lab, DC/member host, domain user, logging |
| C2 telemetry | Isolated C2 server/target, listener rules, DNS/proxy/firewall logs |
| Exfil/DLP | Synthetic dataset, DLP/logging stack, no external path |
| Response workflow | Named participants, stop word, escalation, closeout process |

## 11. Cleanup and Evidence Handling

Since Day 5 is tabletop-only:

```
No cleanup required.
```

Future validation cleanup must verify:

- Test requests stopped.
- Alerts preserved.
- Logs preserved.
- Temporary files removed.
- Sessions closed.
- Listeners closed.
- Synthetic data removed.
- Snapshots restored if state changed.
- No external systems contacted.
- Final timeline completed.

## 12. Evidence Log

- Prior evidence: Week 1 route mapping, Week 2 control and logging review, Week 3 SQLi and stored-XSS findings, Week 4 no-go decisions, Week 5 C2 readiness gaps, Week 6 emulation profile and attack-path controls.
- Day 4 artifacts: phase gates, communications templates, no-go decision record.
- No new technical log, alert, or telemetry generation occurred.

## 13. Knowledge Check

1. What is purple-team validation?
   - It is a collaborative process where red-team behaviors are mapped to blue-team visibility and response capability.

2. Why is Day 5 tabletop-only?
   - Because the goal is to define detection objectives and readiness gaps without generating any live telemetry.

3. What is the difference between simulated detection and observed detection?
   - Simulated detection is a planned scenario used for validation design; observed detection is based on actual generated telemetry and logs.

4. Why should SQLi replay be rejected today?
   - Because live technique execution is prohibited and no safe validation environment is confirmed.

5. Why should XSS replay be rejected today?
   - Because it would involve live browser or app behavior outside the approved tabletop scope.

6. What telemetry would support SQLi detection?
   - App logs, request logs, validation errors, web access logs, and route activity records.

7. What telemetry would support XSS detection?
   - Form-submission logs, render-path logs, content moderation records, browser telemetry, and admin access logs.

8. Why are false positives important?
   - Because benign or training data can look malicious without context, leading to incorrect response decisions.

9. Why is fake config not a real secret alert?
   - Because it is clearly labeled training data and not a genuine credential, token, or secret exposure.

10. Why are host and AD detections deferred?
   - Because isolated host and AD telemetry stacks are not confirmed and require explicit future validation setup.

11. Why are C2 detections deferred?
   - Because C2 validation requires a controlled environment, listener rules, network telemetry, and authorized infrastructure.

12. Why is DLP validation deferred?
   - Because it requires synthetic or approved data movement, observation pipelines, and data-loss controls not yet confirmed.

13. Why should alerts not be claimed as observed today?
   - Because no telemetry was generated and no detections were actually triggered.

14. What must be confirmed before future validation?
   - Infrastructure isolation, telemetry availability, authorization, stop conditions, and evidence-handling procedures.

15. What is the safe Day 5 result?
   - A completed detection validation plan that defines defender objectives, success criteria, and no-go boundaries without executing any technical activity.
