# ACME Week 7 Day 4 Process and Memory Behavior Detection Plan

**Theme:** Understanding process and memory risk without process injection or payload execution

**MITRE ATT&CK:** Defense Evasion — TA0005

**Date:** 2026-08-21

**Time:** 12:00 PM–3:00 PM

**Status:** Tabletop defensive analysis only (non-operational)

---

## 1. Executive Summary

Day 4 examines process behavior, memory-related risk, and the telemetry defenders need to identify suspicious execution patterns. Defenders often detect evasion through behavior rather than file names alone. Parent/child process relationships, command-line context, executable paths, memory-access observations, file changes, network activity, and security-control interactions can provide the evidence needed to reconstruct an event.

This session is strictly non-operational. No process injection, shellcode testing, payload loading, malware execution, memory dumping, credential dumping, debugger attachment, LOLBin execution, security-control tampering, C2, persistence, or bypass testing was performed. The deliverable provides a conceptual behavior map, high-level memory discussion, normal-versus-suspicious comparisons, simulated tabletop cards, future validation requirements, and a no-go observation.

---

## 2. Scope and Safety

### 2.1 Allowed Activities

- Process-behavior mapping
- High-level memory-risk concept discussion
- Telemetry requirement mapping
- False-positive analysis
- Simulated event cards
- Future validation requirements
- No-go readiness observation
- Documentation and knowledge review

### 2.2 Prohibited Activities

**No live process, memory, injection, or payload testing is authorized.**

| Activity | Reason |
|---|---|
| Process injection | High-risk; no host or EDR lab is confirmed |
| Shellcode | Creates harmful artifact risk |
| Payload loading | Prohibited and requires separate authorization |
| Malware execution | Prohibited; harmful artifacts and uncontrolled behavior |
| Memory dumping | Can expose secrets and credentials |
| Credential dumping | High-risk and prohibited |
| Debugging or attaching to sensitive processes | No host or control authorization |
| Security-control tampering | Prohibited; undermines detection and defense |
| Obfuscation testing | Can become evasion optimization |
| LOLBin execution | Live execution is prohibited |
| C2 or persistence | No authorized lab or scope exists |
| Running commands to generate process events | No telemetry lab is confirmed |
| Public, LAN, cloud, employer, school, or production testing | Excluded scope |

### 2.3 Day 4 Decision

```
No live process, memory, injection, or payload testing is authorized.

Day 4 remains tabletop-only. No process, memory, script, file, network,
or security-control events were generated.
```

---

## 3. Process and Memory Concept Overview

### 3.1 Why Process Behavior Matters

Process behavior provides context that a filename alone cannot. A trusted executable may be normal in one workflow and suspicious in another. Defenders assess the relationship between:

- Parent and child processes
- User and logon session
- Executable path and file provenance
- Command-line arguments
- Timing and execution frequency
- File, registry, task, or service changes
- Network destinations and protocol context
- Security-control observations
- Approved administrative or change records

A process-behavior detection plan should identify what evidence would be visible, what baseline would be expected, and what remains unvalidated when telemetry is absent.

### 3.2 Important Process Behavior Categories

| Category | Defensive Concern | Safe Defensive Question |
|---|---|---|
| Unusual parent/child process chains | Unexpected execution flow | What launched the child, and does the relationship match a known workflow? |
| Unusual command-line arguments | Hidden intent or suspicious invocation | Are the complete arguments visible and interpretable? |
| Script/interpreter use | Automation or script-driven behavior | Is the interpreter used by an approved user, parent, path, and task? |
| Unsigned or unusual binaries | Untrusted execution path | Is the binary expected, verified, and located in an approved path? |
| Short-lived processes | Activity difficult to reconstruct | Are process start and exit events captured with sufficient fidelity? |
| Sensitive process access | Possible credential, memory, or control interaction | Which process accessed which target, and was there an approved reason? |
| Unexpected network-capable process | Process communicating outside its normal baseline | Is the destination expected for this process and identity? |
| Durable execution changes | Tasks, services, autoruns, or startup behavior | Is there an approved change record? |
| Security-control interaction | Attempts to query, change, or weaken controls | Was the interaction authorized and logged? |

### 3.3 Memory Risk at a Defensive Level

Memory-related activity can expose sensitive data, alter execution state, or interact with protected processes. Day 4 does not reproduce or test any of those behaviors. The safe defensive focus is on what a lab-owned defensive tool might record and what authorization, privacy protection, and evidence handling would be required before any future review.

No injection steps, code, API sequences, shellcode, payload instructions, debugger commands, or memory-dumping procedures are included.

---

## 4. Current Readiness

| Component | Status | Day 4 Meaning |
|---|---|---|
| Windows/Linux host | Not confirmed | No process or memory testing |
| Process telemetry | Not confirmed | No execution-chain validation |
| Command-line logging | Not confirmed | No invocation validation |
| Memory telemetry | Not confirmed | No memory-behavior validation |
| Security-control logs | Not confirmed | No alert or block validation |
| EDR/AV lab | Not confirmed | No control-response validation |
| SIEM/workflow | Not confirmed | No triage validation |
| Baseline snapshot | Not confirmed | No before/after comparison |
| Written authorization | Not confirmed | No hands-on process testing |

### 4.1 Readiness Decision

No Windows or Linux host, process telemetry, command-line logging, memory telemetry, security-control logging, EDR/AV lab, SIEM workflow, baseline snapshot, or written authorization is confirmed for Day 4.

**No-go observation:** No live process, memory, injection, or payload testing is authorized. Detection coverage, process-level visibility, and bypass resistance must not be claimed.

---

## 5. Process Behavior Map

| Behavior Category | Defensive Signal | Required Telemetry |
|---|---|---|
| Unexpected parent process | Child launched from an unusual parent | Process and parent/child telemetry |
| Suspicious command line | Rare flags, hidden windows, or encoded-looking arguments | Full command-line capture |
| Interpreter execution | Script engine used outside an expected workflow | Process, command-line, and script logs |
| Short-lived process | Process starts and exits quickly | High-fidelity process start and exit telemetry |
| Unusual binary path | Execution from a temporary, download, or user-writable path | Process path, file provenance, and file telemetry |
| Sensitive process access | Access to a privileged or protected process | EDR/security-control telemetry and process context |
| Process-network correlation | Process communicates with an unusual destination | Process, DNS, proxy, firewall, and network logs |
| Durable execution path | Service, task, autorun, or startup entry created | System, service, task, registry, and file logs |
| Security-control interaction | Control queried, changed, stopped, or errored | Security-control logs and process telemetry |
| Unusual execution frequency | Repeated starts outside a known workflow | Process timing, identity, host baseline, and command line |
| Unexpected privilege context | Process runs with a token or identity not expected for the task | Authentication, token, process, and authorization records |

### 5.1 Process Correlation Questions

For any suspected process behavior pattern, analysts should ask:

1. What process started, and what launched it?
2. Which user, logon session, and privilege context were involved?
3. What were the complete command-line arguments?
4. Was the executable in an expected and approved path?
5. Were files, registry entries, tasks, or services changed?
6. Did the process access another process or protected resource?
7. Did it communicate with a known destination?
8. Did a security control observe, block, or report the behavior?
9. Does the sequence match an approved workflow or change record?

These questions are planning requirements only. No live process events were generated or analyzed.

---

## 6. Memory Behavior Discussion

Keep this discussion high-level and defensive. No memory operations were performed.

| Memory-Related Concern | Defensive Question | Required Defensive Evidence |
|---|---|---|
| Unusual access to another process | Which process accessed which target, and why? | Lab-owned EDR or defensive memory telemetry with process identity and authorization context |
| Unexpected module or library load | Is the loaded module expected for that process? | Module-load records, file provenance, signer or hash context where appropriate |
| Memory protection changes | Did a process change memory permissions unusually? | Defensive control telemetry describing the observation, process, target, and time |
| Unbacked or unusual executable memory | Does memory contain executable regions not backed by normal files? | High-level defensive memory assessment from a lab-owned tool; no manual extraction or dumping |
| Credential-sensitive process access | Was a sensitive process accessed without an approved reason? | Process-access alert, identity context, approved monitoring record, and control logs |
| Security-tool process interaction | Was a security-control process queried or modified? | Security-control telemetry, process relationship, authorization, and change record |
| Unexpected memory-resident behavior | Does observed activity lack a normal file-backed explanation? | Defensive alert context, process lineage, file telemetry, and analyst workflow |

### 6.1 Memory-Safety Boundaries

The following remain explicitly out of scope:

- Process injection or hollowing
- Shellcode or executable memory creation
- Payload loading
- Memory dumping or credential extraction
- Debugger attachment to sensitive processes
- Manual memory inspection instructions
- API or code sequences for altering or accessing memory
- Security-control bypass or tampering

Future work, if ever authorized, must use a benign simulator or lab-owned defensive control and must preserve privacy, secrets, logs, snapshots, and evidence.

---

## 7. Normal vs Suspicious Process Behavior

| Scenario | More Likely Benign When | More Suspicious When |
|---|---|---|
| Script interpreter launched | Approved admin script, expected parent, known path, and maintenance window | Unknown parent, encoded-looking arguments, unusual time, or unexpected user |
| Process from temporary path | Approved installer or update with a known source and change record | Unknown user, rare hash, unusual parent, or network activity |
| Short-lived process | Known updater or scheduled task with an established baseline | Many rapid executions after unexplained application activity |
| Administrative shell | Ticketed maintenance by an authorized administrator | Spawned unexpectedly from a browser, office application, or unrelated service |
| Sensitive process access | Approved debugging or monitoring activity by a named owner | Non-admin process, unusual parent, no ticket, or unexplained target |
| New service or task | Approved deployment with expected path and change record | Odd binary path, unexpected user, unusual trigger, or no change record |
| Process network activity | Known application behavior to an expected destination | Rare destination, unusual protocol, unexpected identity, or no baseline |
| Security-control interaction | Authorized health check or maintenance activity | Unapproved query, configuration change, service action, or repeated access |
| Module or library load | Signed, expected module from an approved path and known application | Unusual location, missing provenance, unexpected parent, or rare process context |

### 7.1 False-Positive Handling

Administrative and security tools can produce legitimate process and memory observations. Analysts should avoid deciding from a single indicator. Record the expected user, host, parent, path, timing, destination, arguments, change ticket, and business purpose. If the evidence is incomplete, classify the observation as unvalidated and request additional telemetry instead of asserting either compromise or benign behavior.

---

## 8. Simulated Process Cards

Use tabletop-only cards. No process or memory events were generated.

| Card ID | Simulated Scenario | Defender Question |
|---|---|---|
| **PROC-SIM-01** | Unexpected parent launches a script interpreter | What launched it and why? |
| **PROC-SIM-02** | Short-lived process appears after application activity | Can the sequence be reconstructed? |
| **PROC-SIM-03** | Process runs from a user-writable path | Is this approved software or suspicious execution? |
| **PROC-SIM-04** | Process accesses sensitive process memory | Is there an approved monitoring or debugging reason? |
| **PROC-SIM-05** | Process communicates with a rare destination | Is this expected for that process and user? |
| **PROC-SIM-06** | New task or service appears | Is there an approved change record? |
| **PROC-SIM-07** | Security-control process interaction occurs | Was this authorized and logged? |

Clearly state:

```
These cards are simulated. No process or memory events were generated.
No injection, shellcode, payload, memory dump, malware, or bypass activity occurred.
```

### 8.1 Tabletop Discussion Prompts

For each card, discuss only:

- What evidence would be required?
- Which telemetry source owns that evidence?
- What benign explanation should be checked?
- What additional context would raise or lower concern?
- Who owns triage and escalation?
- What remains unvalidated because the lab is not confirmed?
- What cleanup and evidence-preservation requirements would apply to a future authorized exercise?

---

## 9. Rejected Actions

| Rejected Action | Reason |
|---|---|
| Process injection | High-risk and no host or EDR lab is confirmed |
| Shellcode testing | Creates harmful artifact risk |
| Payload loading | Prohibited and not authorized |
| Malware execution | Prohibited; uncontrolled behavior and harmful artifact risk |
| Memory dumping | Can expose secrets and credentials |
| Credential dumping | High-risk and prohibited |
| Attaching a debugger to a sensitive process | No host or security-control authorization |
| Generating process events | No telemetry lab is confirmed |
| Running LOLBins or scripts | Live execution is prohibited |
| Modifying security controls | Tampering is prohibited |
| Obfuscation testing | Can become evasion optimization |
| Starting C2 or network callbacks | No authorized C2 lab or traffic testing |
| Creating persistence | Durable changes are prohibited |
| Claiming detection coverage | No telemetry or controls were generated or validated |
| Testing public, LAN, cloud, employer, school, or production systems | Excluded scope |

---

## 10. Findings and Observations

### W7-O04: Process and Memory Behavior Validation Deferred

- **Classification:** Planning control
- **Severity:** Not applicable
- **Confidence:** Confirmed
- **Evidence:**
  - Week 7 Day 1 established no hands-on evasion testing.
  - Week 7 Day 2 found no confirmed host, telemetry, security-control, SIEM, or written authorization.
  - Week 7 Day 3 rejected live LOLBin, script, command, payload, and bypass testing.
  - No Windows/Linux host, memory telemetry, EDR/AV lab, baseline snapshot, or written authorization is confirmed.
  - No process, memory, script, file, network, or security-control events were generated on Day 4.
- **Impact:**
  - The team can map process and memory detection requirements.
  - The team cannot claim control coverage, bypass resistance, or process-level visibility.
- **Limitation:**
  - No process, memory, script, file, network, security-control, or response telemetry was generated or tested.
  - No baseline comparison, memory observation, analyst workflow, or control response was validated.
- **Recommendation:**
  - Keep process and memory work tabletop-only until isolated hosts, snapshots, telemetry, lab-owned controls, written authorization, stop conditions, evidence ownership, and cleanup are confirmed.
  - Explicitly prohibit credential dumping, shellcode, malware, payload loading, injection, persistence, and security-control tampering.

---

## 11. Future Validation Requirements

Before future hands-on process or memory validation, require all of the following:

- [ ] Confirmed isolated Windows or Linux host
- [ ] Host-only or internal network proof with no public, production, or shared LAN access
- [ ] Baseline snapshot
- [ ] Written authorization naming the exact benign behavior class and limits
- [ ] Process and parent/child telemetry
- [ ] Full command-line capture
- [ ] File event telemetry
- [ ] Script/interpreter telemetry where applicable
- [ ] Memory-related telemetry from a lab-owned defensive tool
- [ ] Security-control logs
- [ ] Network, DNS, proxy, and firewall telemetry where relevant
- [ ] Centralized protected log storage
- [ ] Time synchronization
- [ ] Stop condition and `ACME-STOP`
- [ ] Cleanup and snapshot restore plan
- [ ] Evidence owner and analyst workflow
- [ ] Explicit prohibition on credential dumping, shellcode, malware, payloads, injection, persistence, and security-control tampering
- [ ] Privacy and secret-handling plan for any sensitive process observation

**Current decision:** No item is treated as validated by this tabletop document. No hands-on process or memory validation is authorized.

---

## 12. Cleanup and Evidence Handling

### 12.1 Day 4 Cleanup

Day 4 generated no live events or artifacts:

- No systems were accessed for testing
- No processes, scripts, shells, LOLBins, or commands were run
- No process injection, shellcode, payload loading, malware execution, or memory dumping occurred
- No debugger was attached to a sensitive process
- No files, tasks, services, registry entries, or persistence were created
- No logs, alerts, telemetry, or network traffic were generated
- No security controls were changed

Cleanup consists of preserving this plan, recording the no-go decision, and labeling all cards and behavior maps as simulated or unvalidated.

### 12.2 Future Authorized Exercise Cleanup

If future hands-on validation is separately authorized:

1. Preserve endpoint, process, command-line, file, memory-related, network, identity, application, and security-control logs.
2. Export logs to the protected lab evidence store before rollback.
3. Record host identity, snapshot identifier, timestamps, approved behavior class, scope, and evidence owner.
4. Verify no credential material, secrets, payloads, shellcode, malware, or persistence remain.
5. Remove all approved test artifacts and restore the baseline snapshot.
6. Verify the host and security controls match the pre-exercise state.
7. Preserve the evidence without clearing logs and obtain exercise-owner sign-off.

Logs must never be cleared as part of cleanup.

---

## 13. Evidence Log

| Evidence | Source | Status | Location |
|---|---|---|---|
| Week 7 Day 4 process and memory behavior detection plan | Tabletop planning | Complete | This file |
| Current readiness assessment | Component checklist | Complete | Section 4 |
| Process behavior map | Defensive analysis | Complete | Section 5 |
| Memory behavior discussion | High-level defensive analysis | Complete | Section 6 |
| Normal vs suspicious process comparison | False-positive analysis | Complete | Section 7 |
| Simulated process cards | Tabletop exercise | Complete | Section 8 |
| Rejected actions register | Scope enforcement | Complete | Section 9 |
| Finding W7-O04 | Planning observation | Complete | Section 10 |
| Future validation requirements | Readiness planning | Complete | Section 11 |

**Evidence limitation:** No live process, memory, script, file, network, security-control, alert, or response evidence is available because no technical activity was performed.

---

## 14. Knowledge Check

1. **Why does process behavior matter for evasion detection?**  
   Process relationships, paths, arguments, timing, identity, and side effects provide behavioral context that a filename alone cannot. This context helps defenders distinguish expected administration from suspicious execution.

2. **Why is Day 4 tabletop-only?**  
   No Windows/Linux host, process or memory telemetry, EDR/AV lab, baseline snapshot, SIEM workflow, or written authorization is confirmed for live validation.

3. **Why is process injection prohibited?**  
   It is high-risk behavior that can alter execution and destabilize systems, and there is no authorized host, defensive control, telemetry, or cleanup plan confirmed for it.

4. **Why is shellcode testing prohibited?**  
   Shellcode creates harmful artifact and execution risk and is outside the non-operational defensive scope.

5. **Why is memory dumping prohibited?**  
   Memory dumps can expose credentials, secrets, tokens, personal data, and other sensitive material. No authorized privacy or evidence-handling process exists today.

6. **Why is parent/child process telemetry important?**  
   It shows what launched what and helps reconstruct execution chains and identify relationships outside the expected baseline.

7. **Why is command-line capture important?**  
   It records how a process was invoked and preserves the arguments needed to interpret intent, subject to appropriate privacy and retention controls.

8. **What telemetry helps identify a process running from an unusual path?**  
   Process path and provenance, file creation and modification events, signer or hash context where appropriate, parent process, user identity, and related network or security-control telemetry.

9. **What makes short-lived processes difficult to investigate?**  
   They may start and exit before analysts can observe them interactively. High-fidelity start, exit, parent/child, command-line, and timing data is needed to reconstruct the sequence.

10. **Why is sensitive process access risky?**  
    It may expose credentials or secrets, alter execution state, interact with protected controls, or indicate behavior outside the user's approved role.

11. **Why should security-control interaction be carefully reviewed?**  
    Queries, changes, stops, or errors involving security controls may indicate routine health checks, misconfiguration, tampering, or an attempt to weaken defenses. Authorization and control logs are required for interpretation.

12. **Why should normal admin behavior be baselined?**  
    Administrators and approved tools can produce activity that resembles suspicious behavior. A baseline reduces false positives and helps analysts focus on unusual combinations of identity, timing, parent, path, arguments, and destination.

13. **Why are simulated process cards labeled clearly?**  
    Clear labels prevent hypothetical scenarios from being mistaken for real process or memory events and keep the exercise safely non-operational.

14. **What must be confirmed before future process/memory validation?**  
    An isolated host, baseline snapshot, exact written authorization, process and command-line telemetry, file and script logs, lab-owned memory and security-control telemetry, relevant network sources, centralized protected storage, time synchronization, stop conditions, cleanup, privacy protections, and evidence ownership.

15. **What is the safe Day 4 result?**  
    A tabletop process and memory detection plan with behavior categories, high-level memory risks, false-positive guidance, simulated cards, readiness requirements, and a no-go observation, with no live process or memory activity performed.

---

## 15. Day 4 Completion Checklist

- [x] Created `week7-day4-process-memory-behavior-detection-plan.md`
- [x] Performed no new technical activity
- [x] Generated no process, memory, script, file, network, or security-control events
- [x] Included no injection steps, code, API sequences, shellcode, payloads, or bypass instructions
- [x] Built a process behavior map
- [x] Included high-level memory behavior discussion
- [x] Compared normal vs suspicious process behavior
- [x] Created simulated process cards
- [x] Listed rejected actions
- [x] Included W7-O04
- [x] Answered the knowledge check
- [x] Documented future validation requirements
- [x] Documented cleanup and evidence handling

---

**Document completed by:** Cody R Johnson  
**Date:** 2026-08-21  
**Time:** 12:00 PM–3:00 PM  
**Review status:** Ready for Day 5 preparation  
**Approval:** [Exercise owner sign-off required before any hands-on work]
