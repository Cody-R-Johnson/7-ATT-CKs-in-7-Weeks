# ACME Week 7 Day 2 Logging, Telemetry, and Detection Surface Map

**Theme:** Understanding what defenders need to see before any evasion validation

**MITRE ATT&CK:** Defense Evasion — TA0005

**Date:** 2026-08-19

**Status:** Tabletop planning and defensive analysis only (non-operational)

---

## 1. Executive Summary

Telemetry is the evidence defenders use to understand what happened. Day 2 maps the host, process, file, network, identity, application, and security-control sources that would be required before any future evasion exercise. No events, tools, traffic, alerts, or detections were generated or tested today.

Because no Linux, Windows, AD, C2, EDR/AV, SIEM, or telemetry lab is confirmed, the detection surface map describes requirements rather than validated coverage. The safe Day 2 result is a documented readiness map and blind-spot register with a continued no-go decision for live evasion or telemetry validation.

---

## 2. Scope and Safety

### 2.1 Allowed Activities

- Telemetry inventory planning
- Detection-surface mapping
- Blind-spot analysis
- Simulated log-source tables
- Future validation requirements
- No-go readiness observations
- Documentation and knowledge review

### 2.2 Prohibited Activities

**No live telemetry validation is authorized.**

| Activity | Reason |
|---|---|
| Generating telemetry | No host telemetry lab is confirmed; live execution is out of scope |
| Running scripts or tools to create events | Creates live events and is prohibited today |
| Disabling logs | Prohibited; destroys evidence |
| Clearing logs | Prohibited; destroys forensic records |
| Modifying security tools | No lab-owned control or authorization is confirmed |
| Starting C2 | C2 and traffic generation are prohibited |
| Running payloads | Prohibited; creates harmful artifacts |
| Running LOLBin chains | Prohibited; no validated host telemetry lab exists |
| Process injection | Prohibited high-risk activity |
| Obfuscation tests | Prohibited; can become evasion optimization |
| Bypass testing | Prohibited; requires all authorization gates |
| Public, LAN, cloud, employer, school, or production testing | Excluded scope |

### 2.3 Day 2 Decision

```
No live evasion or telemetry validation is authorized.

Day 2 remains tabletop-only. No telemetry was generated.
```

---

## 3. Telemetry Concept Overview

### 3.1 What Is Telemetry?

Telemetry is the evidence defenders use to understand what happened, when it happened, which identity was involved, and how systems responded. Useful telemetry lets analysts reconstruct activity without relying on assumptions.

| Telemetry Type | What It Shows | Defensive Use |
|---|---|---|
| Process logs | What executed and parent/child process relationships | Reconstruct execution chains |
| Command-line logs | How a program was invoked | Interpret intent and arguments |
| File events | Creation, modification, deletion, and rename | Identify changed artifacts |
| Network flow | Source, destination, protocol, timing, and volume | Identify unexpected communications |
| DNS logs | Name resolution patterns | Identify unusual domains and lookup behavior |
| Authentication logs | Logon, logout, and failed attempts | Establish identity and access context |
| Script logs | Interpreter use and script content where safely captured | Review script activity |
| Security-control logs | AV/EDR alerts, policy changes, and tamper events | Determine whether controls observed or blocked behavior |
| System logs | Services, scheduled tasks, startup, and shutdown | Detect durable system changes |
| Application logs | Routes, errors, authentication, and administrative actions | Correlate endpoint behavior with app activity |

Without telemetry, defenders cannot validate whether an evasion attempt was detected or missed. A suspected detection gap must remain an unvalidated hypothesis until the relevant sources are enabled, complete, time-synchronized, preserved, centralized, and reviewed.

### 3.2 What Is a Detection Surface?

A detection surface is a source of observable evidence where activity can be recorded, correlated, and investigated. Detection surfaces span endpoints, networks, identities, applications, and security controls. A complete map identifies both what should be visible and what is currently unknown.

---

## 4. Current Telemetry Readiness

| Component | Status | Day 2 Meaning |
|---|---|---|
| Local ACME app logs | Not validated for Week 7 | Prior app evidence only |
| Linux host logs | Not confirmed | No Linux telemetry validation |
| Windows event logs | Not confirmed | No Windows telemetry validation |
| PowerShell/script logs | Not confirmed | No script telemetry validation |
| EDR/AV telemetry | Not confirmed | No control-bypass validation |
| SIEM/correlation | Not confirmed | No cross-source validation |
| DNS/proxy/firewall logs | Not confirmed | No network detection validation |
| AD/domain logs | Not confirmed | No identity/domain validation |
| C2 listener logs | Not confirmed | No C2 detection validation |
| DLP/CASB logs | Not confirmed | No data-movement validation |

### 4.1 Readiness Assessment

No telemetry source listed above is confirmed for Week 7. The local ACME application has prior evidence, but that evidence does not establish current Week 7 endpoint, network, identity, or security-control coverage.

**No-go observation:** Do not claim telemetry coverage, detection coverage, or bypass resistance until the relevant sources are confirmed and validated in an isolated lab.

---

## 5. Detection Surface Map

Do not populate this matrix with live logs. The entries below define evidence that would be required for future authorized validation.

| Detection Surface | Example Evidence | Defender Question | Current Status |
|---|---|---|---|
| Process execution | Parent/child process events | What launched what? | Not confirmed |
| Command line | Full command arguments | Can analysts see invocation details? | Not confirmed |
| Script execution | Script-block or interpreter logs | What script ran and from where? | Not confirmed |
| File system | New, modified, deleted, or renamed files | What artifact changed? | Not confirmed |
| Registry / autoruns | Durable startup changes | Was persistence-like behavior created? | Not confirmed |
| Scheduled tasks / services | New task or service records | Was a durable execution path created? | Not confirmed |
| Network flow | Source, destination, timing, protocol, and volume | Did an endpoint communicate unexpectedly? | Not confirmed |
| DNS | Query name, source, and resolver | Were unusual domains queried? | Not confirmed |
| Proxy / web | URL, method, status, and headers | Was web-like traffic visible? | Not confirmed |
| Authentication | Logon, logout, and failure events | Which identity was involved? | Not confirmed |
| Security control | Alerts, policy changes, and tamper events | Did the control observe or block behavior? | Not confirmed |
| Application | Routes, errors, and administrative activity | Did app-level behavior appear? | Prior evidence only |

### 5.1 Required Correlations

Future validation would require correlation across:

- Process and command-line context
- Process and file activity
- Process and network activity
- Identity and endpoint activity
- Security-control alerts and policy changes
- Application requests and host events
- DNS, proxy, firewall, and endpoint network context

These correlations are planning requirements only. They were not exercised on Day 2.

---

## 6. Telemetry Quality Criteria

Telemetry is useful only when it meets all of these criteria:

| Criterion | Meaning |
|---|---|
| Enabled | The source is actually collecting events |
| Complete | Important fields are present, including identity, time, source, and context |
| Time-synchronized | Events can be correlated in the correct order |
| Protected | Logs cannot be easily modified by test users or subjects |
| Centralized | Evidence survives endpoint reset and is available for correlation |
| Searchable | Analysts can query and review the data efficiently |
| Scoped | Only authorized lab assets are included |
| Preserved | Logs are not cleared after testing |
| Understood | Analysts know what each source means and what it cannot prove |

A source that is merely enabled is not automatically sufficient. Coverage must also be complete, protected, centralized, searchable, time-synchronized, scoped, preserved, and understood.

---

## 7. Blind Spot Register

| Blind Spot | Why It Matters | Control |
|---|---|---|
| No process telemetry | Cannot see execution chains or parent/child relationships | Enable host/process logging in an isolated lab |
| No command-line capture | Cannot interpret invocation details or intent | Enable command-line auditing |
| No script logging | Cannot review interpreter activity or safely captured content | Enable appropriate script logging in the lab |
| No central logging | Endpoint reset can lose evidence | Forward to a lab SIEM or protected log store |
| No time synchronization | Events cannot be correlated reliably | Configure lab NTP and verify clock alignment |
| No security-control logs | Cannot know if AV/EDR observed or blocked behavior | Confirm lab-owned control logging |
| No DNS/proxy logs | Cannot review name-resolution or web traffic patterns | Add resolver and proxy telemetry |
| No firewall/network flow logs | Cannot establish connection context | Add scoped firewall and flow telemetry |
| No snapshot baseline | Cannot compare before and after state | Take and document a baseline snapshot |
| No analyst workflow | Alerts may not be triaged, assigned, or closed consistently | Define workflow and evidence owner |
| No identity/domain logs | Cannot attribute activity to a user or service account | Confirm authentication and domain-event collection |
| No DLP/CASB logs | Cannot assess data-movement visibility | Confirm lab-owned data-control telemetry if in scope |

---

## 8. Simulated Telemetry Cards

Use tabletop-only cards. No cards below represent actual events.

| Card ID | Simulated Telemetry Gap | Defender Question |
|---|---|---|
| **TEL-SIM-01** | Process event is missing its parent process | Can we understand the execution chain? |
| **TEL-SIM-02** | Command line is truncated | Can intent be reconstructed from available evidence? |
| **TEL-SIM-03** | Script execution is visible but content is absent | Is the evidence enough for triage? |
| **TEL-SIM-04** | Endpoint log exists but no SIEM copy is present | Will evidence survive rollback? |
| **TEL-SIM-05** | Network flow exists but has no process context | Can network and endpoint evidence correlate? |
| **TEL-SIM-06** | An alert fired but no analyst workflow exists | Who owns triage and closeout? |
| **TEL-SIM-07** | Logs have different timestamps | Can events be ordered correctly? |

Clearly state:

```
These cards are simulated. No telemetry was generated.
No logs, alerts, events, traffic, or detection tests were created on Day 2.
```

---

## 9. Rejected Actions

| Rejected Action | Reason |
|---|---|
| Generate test process events | No host telemetry lab is confirmed |
| Run scripts to create logs | Live execution is prohibited |
| Disable or clear logs | Prohibited; destroys evidence |
| Modify AV/EDR policy | No lab-owned control or authorization is confirmed |
| Test tamper protection | Control-bypass testing is prohibited |
| Generate encoded commands | Obfuscation testing is prohibited |
| Start network callbacks | C2 and traffic generation are prohibited |
| Use production logs | Production systems are excluded |
| Claim telemetry coverage | No sources were validated today |
| Run LOLBin chains | Live tool execution is prohibited; no telemetry lab is confirmed |
| Generate payloads or injection events | Prohibited high-risk activity |

---

## 10. Findings and Observations

### W7-O02: Telemetry Validation Deferred Because Detection Sources Are Not Confirmed

- **Classification:** Planning control
- **Severity:** Not applicable
- **Confidence:** Confirmed
- **Evidence:**
  - Week 7 Day 1 found no confirmed Linux, Windows, AD, C2, EDR/AV, or telemetry lab.
  - No process, command-line, file, script, DNS, proxy, firewall, SIEM, or security-control telemetry source is confirmed for Week 7.
  - No written evasion authorization exists.
  - No telemetry, events, alerts, traffic, or logs were generated on Day 2.
- **Impact:**
  - The team can map required detection surfaces and telemetry dependencies.
  - The team cannot claim evasion detection coverage, telemetry coverage, or bypass resistance.
- **Limitation:**
  - No logs, alerts, telemetry, or response workflows were generated or tested.
  - No source completeness, time synchronization, centralization, preservation, or analyst workflow was validated.
- **Recommendation:**
  - Confirm isolated hosts, lab-owned controls, telemetry sources, centralized logging, time synchronization, written authorization, stop conditions, and cleanup before any hands-on validation.
  - Keep Day 2 tabletop-only until every future-validation readiness item is satisfied.

---

## 11. Future Validation Readiness Checklist

Before any future hands-on evasion or telemetry validation, require all of the following:

- [ ] Confirmed isolated Linux or Windows VM
- [ ] Host-only or internal network proof with no public, production, or shared LAN access
- [ ] Baseline snapshot documented
- [ ] Lab-owned security control or training detector
- [ ] Process execution telemetry
- [ ] Command-line logging
- [ ] File event logging
- [ ] Script/interpreter logging where applicable
- [ ] Network, DNS, and firewall telemetry
- [ ] Security-control alert and tamper logs
- [ ] Centralized log collection
- [ ] Time synchronization
- [ ] Written authorization naming behavior and limits
- [ ] Stop condition and ACME-STOP escalation
- [ ] Cleanup and snapshot recovery plan
- [ ] Evidence owner and analyst triage workflow

**Current decision:** No item is treated as validated by this tabletop document. No hands-on telemetry validation is authorized.

---

## 12. Cleanup and Evidence Handling

### 12.1 Day 2 Cleanup

Day 2 generated no live events or artifacts:

- No systems were accessed for testing
- No tools or scripts were run to create telemetry
- No logs were modified or cleared
- No alerts, network traffic, or callbacks were generated
- No security controls were changed

Cleanup consists of preserving this plan, recording the no-go decision, and labeling all cards and mappings as simulated or unvalidated.

### 12.2 Future Authorized Exercise Cleanup

If future hands-on validation is separately authorized:

1. Preserve endpoint, process, command-line, file, network, identity, application, and security-control logs.
2. Export logs to the protected lab evidence store before rollback.
3. Record test-host identity, snapshot identifiers, timestamps, and scope.
4. Remove all approved test artifacts and verify that no persistence remains.
5. Restore the baseline snapshot.
6. Verify the host and controls match the pre-exercise state.
7. Preserve the evidence and obtain exercise-owner sign-off.

Logs must never be cleared as part of cleanup.

---

## 13. Evidence Log

| Evidence | Source | Status | Location |
|---|---|---|---|
| Week 7 Day 2 telemetry detection surface map | Tabletop planning | Complete | This file |
| Current telemetry readiness assessment | Component checklist | Complete | Section 4 |
| Detection surface map | Defensive analysis | Complete | Section 5 |
| Telemetry quality criteria | Planning control | Complete | Section 6 |
| Blind spot register | Gap analysis | Complete | Section 7 |
| Simulated telemetry cards | Tabletop exercise | Complete | Section 8 |
| Rejected actions register | Scope enforcement | Complete | Section 9 |
| Finding W7-O02 | Planning observation | Complete | Section 10 |
| Future validation checklist | Readiness planning | Complete | Section 11 |

**Evidence limitation:** No live logs, alerts, events, traffic, or telemetry are available because no technical activity was performed.

---

## 14. Knowledge Check

1. **What is telemetry?**  
   Telemetry is the evidence defenders use to understand what happened, when it happened, which identity was involved, and how systems responded.

2. **What is a detection surface?**  
   A detection surface is a source of observable evidence where activity can be recorded, correlated, and investigated, such as process, file, network, identity, application, or security-control logs.

3. **Why is telemetry required before evasion validation?**  
   Without telemetry, defenders cannot determine whether behavior was observed, blocked, missed, or simply not recorded. Any detection conclusion would be unsupported.

4. **Why is Day 2 tabletop-only?**  
   Required hosts, controls, telemetry sources, centralized logging, and written authorization are not confirmed. Live execution would violate the current no-go boundary.

5. **Why should logs never be disabled or cleared?**  
   Disabling or clearing logs destroys evidence, breaks the detection chain, prevents forensic analysis, and invalidates future conclusions.

6. **Why is command-line capture important?**  
   It shows how a process was invoked and can provide the arguments needed to interpret intent and correlate activity.

7. **Why is process parent/child context important?**  
   It shows what launched what, helping defenders distinguish expected administration from suspicious execution chains.

8. **Why is time synchronization important?**  
   Synchronized timestamps let analysts order events accurately and correlate records across hosts and telemetry sources.

9. **Why is central logging important?**  
   Centralized protected copies preserve evidence through endpoint reset and enable cross-source searching and correlation.

10. **Why are security-control logs required?**  
    They show whether AV/EDR or another control observed, blocked, alerted on, or experienced a policy or tamper event.

11. **Why are DNS/proxy/firewall logs useful?**  
    They provide network context such as queried names, destinations, methods, timing, and traffic decisions that can be correlated with endpoint activity.

12. **Why should production logs not be used?**  
    Production systems are outside the authorized training scope and may contain sensitive data; using them creates legal, privacy, operational, and security risk.

13. **Why are simulated telemetry cards labeled clearly?**  
    Clear labels prevent hypothetical scenarios from being mistaken for real events and keep the exercise safely non-operational.

14. **What must be confirmed before telemetry validation?**  
    An isolated VM, baseline snapshot, lab-owned control, required endpoint and network sources, centralized protected logging, time synchronization, written authorization, stop conditions, cleanup, and evidence ownership.

15. **What is the safe Day 2 result?**  
    A documented telemetry readiness and detection-surface map with blind spots and future requirements, while generating no logs, alerts, events, traffic, or live validation.

---

## 15. Day 2 Completion Checklist

- [x] Created `week7-day2-telemetry-detection-surface-map.md`
- [x] Performed no new technical activity
- [x] Generated no logs, alerts, events, traffic, or telemetry
- [x] Built a telemetry readiness map
- [x] Built a detection surface map
- [x] Listed telemetry quality criteria
- [x] Created a blind spot register
- [x] Created simulated telemetry cards
- [x] Listed rejected actions
- [x] Included W7-O02
- [x] Answered the knowledge check
- [x] Documented future validation requirements
- [x] Documented cleanup and evidence handling

---

**Document completed by:** Cody R Johnson  
**Date:** 2026-08-19  
**Review status:** Ready for Day 3 preparation  
**Approval:** [Exercise owner sign-off required before any hands-on work]
