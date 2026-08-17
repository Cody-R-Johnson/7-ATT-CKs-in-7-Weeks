# ACME Week 7 Day 1 Advanced Evasion Safety and Detection Plan

**Theme:** Understanding defense evasion safely from a detection-engineering perspective

**MITRE ATT&CK:** Defense Evasion — TA0005

**Date:** 2026-08-17

**Status:** Tabletop planning and defensive analysis only (non-operational)

---

## 1. Executive Summary

Week 7 introduces advanced evasion concepts within the MITRE ATT&CK Defense Evasion framework (TA0005). This course maintains a **non-operational** posture: no hands-on evasion, bypass, tampering, or stealth validation is authorized. Day 1 establishes the ethical foundation, authorization gates, and detection-engineering perspective required for safe planning. The purpose is to understand why evasion is high-risk, how defenders detect it, and what authorization would be required before any safe lab-only validation.

All activities on Day 1 are limited to:
- Conceptual discussion
- Authorization planning  
- Detection-surface mapping
- Risk-register updates
- Defensive control mapping
- Simulated event cards

---

## 2. Scope and Safety

### 2.1 Allowed Activities

- Conceptual discussion of evasion techniques
- Authorization planning and safety gates
- Detection-surface mapping and analysis
- Risk-register updates and control identification
- Defensive control mapping against evasion themes
- Simulated event cards for tabletop exercises
- No-go readiness observations
- Documentation and knowledge review

### 2.2 Prohibited Activities

**No hands-on evasion is authorized.**

| Activity | Reason |
|---|---|
| AV or EDR bypass | Requires isolated lab and written authorization |
| Malware creation | Creates harmful artifacts |
| Payload creation | Creates harmful artifacts |
| Process injection | High-risk without lab telemetry |
| Shellcode | Creates harmful artifacts |
| Obfuscation for bypass | Can become evasion optimization |
| Disabling logs | Prohibited; breaks detection chain |
| Disabling security tools | Prohibited; undermines defense |
| Tampering with telemetry | Prohibited; breaks detection chain |
| Running suspicious LOLBin chains | Requires Windows/Linux telemetry lab |
| Credential dumping | High-risk; potential for abuse |
| Persistence | No persistence allowed; snapshot recovery only |
| C2 testing | Requires isolated C2 lab and authorization |
| Exploit replay | Requires authorized isolated lab |
| Testing against real, public, employer, school, cloud, LAN, or production systems | Excluded scope; high legal and ethical risk |

---

## 3. Defense Evasion Concept Overview

Defense evasion refers to behaviors intended to avoid, weaken, bypass, or confuse security controls.

### 3.1 Key Evasion Areas

| Area | Defensive Concern | Example |
|---|---|---|
| Logging gaps | Activity occurs without adequate records | Event logs cleared or forwarded to untrusted system |
| Security-tool tampering | Controls are disabled or weakened | AV disabled; EDR alert silenced |
| Suspicious process behavior | Unusual parent/child process chains | System process spawning cmd.exe |
| Unusual script execution | Unexpected interpreters or command shells | PowerShell launched from unusual parent |
| Living-off-the-land use | Trusted tools used in unusual ways | WMIC, net.exe, tasklist used in rapid succession |
| Obfuscation | Activity made harder to read or classify | Base64-encoded commands; variable obfuscation |
| Persistence-like behavior | Changes that survive normal user activity | Autorun registry entry; scheduled task creation |
| C2-related evasion | Stealth communication patterns | DNS tunneling; HTTPS beaconing with encryption |

### 3.2 Why Week 7 is High-Risk

1. **Evasion directly opposes detection:**  
   Techniques that work are designed to defeat the controls we depend on.

2. **Bypass testing validates attacks:**  
   Demonstrating a bypass works gives adversaries a tested technique.

3. **Lab readiness is incomplete:**  
   Without isolated hosts, lab-owned controls, and full telemetry, results are unreliable and scope creep is likely.

4. **Authorization and escalation matter:**  
   Hands-on evasion requires explicit approval, clear stop conditions, and reversibility.

5. **Artifacts can persist:**  
   Malware, obfuscated code, payloads, and persistence mechanisms can survive cleanup.

---

## 4. Current Lab Readiness

### 4.1 Lab Component Status

| Component | Status | Day 1 Meaning | Future Readiness Needed |
|---|---|---|---|
| Local ACME app | Confirmed | Tabletop evidence only | Snapshot baseline for Day 6+ |
| Prior week reports | Confirmed | May be summarized | Defensive findings reusable |
| Linux VM | Not confirmed | No host evasion testing | Confirmed Linux host, telemetry stack, snapshot |
| Windows VM | Not confirmed | No process/logging testing | Confirmed Windows host, EDR/AV, process telemetry |
| AD lab | Not confirmed | No domain control testing | Confirmed AD environment, domain events, snapshot |
| EDR/AV lab | Not confirmed | No control-bypass testing | Lab-owned EDR/AV, tamper protection, alerting |
| Telemetry stack | Not confirmed | No detection validation | Centralized logging, SIEM, host agents, correlation |
| C2 lab | Not confirmed | No payload, beacon, or listener testing | Isolated C2 network, listener logs, beacon telemetry |
| Written evasion authorization | Not confirmed | No hands-on evasion | Named behavior, allowed limits, stop conditions, escalation |

### 4.2 Day 1 Readiness Decision

```
No hands-on defense-evasion testing is authorized on Day 1.

Reason: Lab components are not confirmed. 
Proceed with tabletop planning and defensive analysis only.
```

---

## 5. Authorization Gates for Future Hands-On Work

Before any future evasion validation is authorized, all of the following gates must be satisfied:

| Gate | Required Evidence | Why It Matters |
|---|---|---|
| **Isolated lab** | Host-only or internal network proof; no internet, no shared LAN, no production access | Prevents accidental or intentional exposure to real systems |
| **Test host** | Confirmed VM, hostname, IP, baseline snapshot | Enables rollback; creates forensic baseline for before/after analysis |
| **Security tool** | Lab-owned tool (not production EDR/AV) or intentionally configured training control | Allows safe testing against controls; no risk to real infrastructure |
| **Written authorization** | Named behavior, allowed limits, stop condition, escalation procedure, exercise owner approval | Creates accountability; defines scope boundaries |
| **Logging plan** | Host, process, command-line, file, network, and control telemetry documented and verified working | Ensures detection coverage; enables validation |
| **Reversible artifact** | No persistence, no destructive changes; benign simulator only | Allows safe cleanup; prevents unintended side effects |
| **Synthetic payload policy** | Benign simulator only, not malware | Avoids creation of harmful artifacts |
| **Stop condition** | Stop after one observable benign event; escalation to ACME-STOP | Prevents scope creep; enables immediate halt |
| **Cleanup plan** | Remove artifact, restore snapshot, preserve logs, sign-off | Verifies return to baseline; documents what was learned |
| **Escalation** | ACME-STOP stop word; exercise owner contact info | Enables immediate cessation if safety concern emerges |

### 5.1 Gate Satisfaction Check

**Current status:** None of the above gates are satisfied.

**Decision:** No hands-on evasion testing is authorized until all gates are satisfied.

---

## 6. Evasion Risk Register

| Risk | Cause | Control | Status |
|---|---|---|---|
| **Unauthorized bypass** | Testing against real security controls without isolation or authorization | Isolated lab and written authorization; no public/prod/school/employer systems | Pending gate satisfaction |
| **Telemetry loss** | Logs disabled, cleared, or forwarded to untrusted destination | Logs must remain enabled and preserved; central backup required | Pending telemetry stack confirmation |
| **Malware-like artifact** | Payload or obfuscated code created during testing | Benign simulator only; no payloads or harmful code today or in future | Enforced by policy |
| **Scope creep** | Moving from tabletop to execution; unauthorized expansion of testing | ROE, stop word (ACME-STOP), no-go gates, escalation procedure | Enforced by authorization gates |
| **Misleading results** | No telemetry stack exists; detections cannot be validated | Mark all detections as simulated; indicate telemetry gaps | Pending telemetry stack confirmation |
| **Persistence risk** | Artifact survives exercise; becomes unintended backdoor | No persistence; snapshot recovery only | Enforced by policy and reversibility gate |
| **Public exposure** | Testing outside lab; accidental or intentional leakage | No public, LAN, cloud, or production systems; isolated network only | Enforced by isolation gate |
| **Legal or compliance violation** | Testing on employer, school, government, cloud, or customer systems without consent | Isolated lab only; explicit written authorization required | Enforced by authorization gate |

---

## 7. Defensive Control Mapping

For each evasion theme, a defender must answer a critical question. Mapping these controls helps plan detection coverage.

| Evasion Theme | Defensive Control | Defender Question | Detection Indicator |
|---|---|---|---|
| **Log tampering** | Centralized logging, protected logs, log forwarding to SIEM | Are logs complete and protected from tampering? | Sudden log gap; unexpected log deletion; forwarding to untrusted system |
| **Security-tool tampering** | Tamper protection, integrity monitoring, alerting | Would control changes alert? Are changes logged and protected? | Service stop events; driver unload; config change alert |
| **Suspicious process chains** | EDR/process telemetry, parent-child tracking | Are parent-child relationships visible and baselined? | System spawning cmd.exe; Notepad launching PowerShell; Office spawning shell |
| **Script abuse** | Script-block logging, command-line logging, interpreter tracking | Are interpreter executions visible and logged? | PowerShell, cmd.exe, VBScript, Python, etc. launching from unusual parents or with suspicious arguments |
| **LOLBin misuse** | Application control, allowlisting, baseline behavior | Is trusted-tool behavior baselined and monitored? | WMIC, net.exe, tasklist, certutil, msiexec in unexpected patterns |
| **Obfuscation** | Content inspection, command-line capture, behavior analysis | Can analysts still interpret the event? Is intent reconstructible? | Base64, hex, or encoded commands; variable obfuscation; comment injection |
| **Persistence-like changes** | Autorun monitoring, scheduled-task auditing, registry alerting | Are durable changes detected? Is there an approved change record? | New registry autorun entry; new scheduled task; cron job creation; LaunchAgent addition |
| **C2-related evasion** | Firewall logs, DNS logs, proxy logs, endpoint telemetry, process context | Is network behavior correlated with process context? Are patterns recognized? | DNS tunneling, HTTPS C2, encrypted beaconing, suspicious port usage |

---

## 8. Simulated Event Cards

Use tabletop cards only. These are **simulations for discussion, not operational events.**

| Card ID | Simulated Behavior | Expected Defender Question | Sample Detection Strategy |
|---|---|---|---|
| **EVA-SIM-01** | Hypothetical security-control change is proposed (e.g., AV engine disabled, policy weakened) | Is this authorized and logged? Is there a change approval record? | Check change management system; verify authorization; require justification |
| **EVA-SIM-02** | Hypothetical unusual script execution appears (e.g., PowerShell launched from Notepad) | What process launched it and why? Is this normal admin behavior? | Correlate parent process; check user and timestamp; baseline against approved scripts |
| **EVA-SIM-03** | Hypothetical trusted tool used unusually (e.g., WMIC querying processes in rapid loops) | Is this normal admin behavior or suspicious? Does it match baselines? | Build baseline of legitimate WMIC usage; alert on anomalies |
| **EVA-SIM-04** | Hypothetical log gap appears (e.g., 2 minutes of missing events) | Was telemetry disabled, missing, or misconfigured? | Check log forwarding; verify SIEM receipt; investigate agent health |
| **EVA-SIM-05** | Hypothetical encoded command appears in logs (e.g., Base64-encoded PowerShell) | Can analysts reconstruct intent safely? Is decoding available? | Decode command line; review process arguments; correlate with script-block logs |
| **EVA-SIM-06** | Hypothetical persistence-like change appears (e.g., new scheduled task, new registry autorun) | Is there an approved change record? Who authorized this? | Cross-reference CMDB; check change tickets; verify service account permissions |

**Clear statement:**
```
These cards represent simulated scenarios for tabletop discussion.
No actual events were generated during Day 1.
All scenarios are hypothetical and for defensive planning only.
```

---

## 9. Rejected Activities

Activities that are rejected and the reasons they cannot proceed:

| Rejected Activity | Reason | Impact |
|---|---|---|
| **AV/EDR bypass testing** | No isolated control lab is confirmed; no written authorization exists | Scope creep; risk of damaging production controls |
| **Obfuscation testing** | Can easily become evasion optimization; no telemetry baseline to measure against | Results will be unreliable; may develop offensive capabilities |
| **Process injection** | High-risk without confirmed Linux/Windows host telemetry lab; can crash systems | Lack of detection surface means no validation possible |
| **Security-tool disabling** | Prohibited by policy; violates detection chain requirement | Breaks investigation; violates compliance and audit controls |
| **Log clearing** | Prohibited by policy; violates detection chain requirement | Forensics destroyed; compliance violation; no audit trail |
| **LOLBin execution chains** | No Windows/Linux telemetry lab confirmed; results unreliable | Cannot validate detection; scope creep risk |
| **Payload generation** | Prohibited by policy; creates harmful artifacts | Malware-like code could escape lab or be misused |
| **C2 evasion testing** | No isolated C2 lab confirmed; no telemetry correlation capability | Cannot validate stealth or detection; risk of operational impact |
| **Public or production testing** | Excluded scope; high legal, compliance, and security risk | Potential breach, legal liability, compliance violation |

---

## 10. Findings and Observations

### W7-O01: Advanced Evasion Limited to Ethics, Authorization, and Defensive Planning

- **Classification:** Planning control / Scope gate
- **Severity:** Not applicable (planning phase; no operational risk on Day 1)
- **Confidence:** Confirmed
- **Evidence:**
  - Week 6 established tabletop-only campaign operations.
  - No Linux, Windows, AD, C2, EDR/AV, or telemetry lab is confirmed.
  - No written hands-on evasion authorization exists.
  - Current lab readiness check shows all components as "Not confirmed."
  - All authorization gates remain unsatisfied.
  
- **Impact:**
  - The team can plan detection coverage and safety gates on Day 1.
  - The team cannot ethically or safely perform evasion, bypass, tampering, or stealth validation without lab readiness and authorization.
  - Future hands-on work requires all 10 authorization gates to be satisfied.
  
- **Limitation:**
  - No security control, endpoint telemetry, or bypass resistance was tested on Day 1.
  - Detection strategies are based on theory, not validation.
  - No baseline telemetry or control behavior was captured.
  - Evasion techniques are discussed but not executed.
  
- **Recommendation:**
  - Keep Week 7 tabletop-only until all of the following are confirmed:
    1. Isolated lab (host-only network, no internet access)
    2. Confirmed test hosts (Linux VM, Windows VM with snapshots)
    3. Lab-owned or training controls (EDR/AV not production)
    4. Written evasion authorization with named behaviors and stop conditions
    5. Verified telemetry stack (host, process, command-line, network logs flowing to SIEM)
    6. Documented cleanup and rollback procedures
    7. Escalation contact and ACME-STOP stop word
  - Once all gates are satisfied, proceed to Day 2–Day 6 defensive analysis.
  - Until then, treat evasion as high-risk and non-operational.

---

## 11. Cleanup and Evidence Handling

### 11.1 Day 1 Cleanup

Since Day 1 is tabletop-only:

- No live systems were accessed
- No artifacts were created
- No logs were modified
- No tools were executed
- No code was written

**Cleanup steps:**
1. Save this plan document to evidence folder
2. Archive simulated event cards and defensive mappings
3. Document knowledge check answers
4. Sign off on no-go decision

### 11.2 Future Cleanup (Post-Authorization)

Once hands-on evasion is authorized and executed:

1. **Restore snapshot:**
   - Halt test host
   - Restore to baseline snapshot
   - Verify system state matches pre-test baseline
   
2. **Preserve logs:**
   - Export all telemetry (host, process, command-line, network, control events)
   - Archive to evidence folder with metadata
   - Do not clear or modify logs
   
3. **Remove artifacts:**
   - Verify no malware, payloads, obfuscated code, or persistence remain
   - Scan with antivirus and endpoint detection
   - Confirm all test files deleted
   
4. **Sign-off:**
   - Exercise owner confirms cleanup complete
   - Documenting what was learned from the exercise
   - Archive evidence and findings to week evidence folder

---

## 12. Evidence Log

### 12.1 Day 1 Evidence

| Evidence | Source | Status | Location |
|---|---|---|---|
| Week 7 Day 1 evasion-safety-detection-plan.md | Tabletop planning | Complete | [this file] |
| Lab readiness assessment | Component checklist | Complete | Section 4 |
| Authorization gate template | Planning control | Complete | Section 5 |
| Evasion risk register | Risk assessment | Complete | Section 6 |
| Defensive control mapping | Defensive analysis | Complete | Section 7 |
| Simulated event cards | Tabletop exercise | Complete | Section 8 |
| Rejected activities register | Scope enforcement | Complete | Section 9 |
| Finding W7-O01 | Planning observation | Complete | Section 10 |

### 12.2 Future Evidence (Post-Authorization, if approved)

Once hands-on evasion is authorized:

- Host telemetry (process events, command-line logs, network logs, file operations)
- EDR/AV detection logs and alerts
- SIEM correlation events
- Snapshot before and after hash verification
- Cleanup logs and sign-off
- Analyst findings and defensive recommendations

---

## 13. Knowledge Check

Answer the following questions based on Day 1 planning:

1. **What is defense evasion?**
   - Behaviors intended to avoid, weaken, bypass, or confuse security controls (e.g., logging gaps, tool tampering, suspicious process behavior, obfuscation, persistence).

2. **Why is Week 7 high-risk?**
   - Evasion directly opposes detection; bypass testing validates attacks; lab readiness is incomplete; authorization and escalation matter; artifacts can persist.

3. **Why is Day 1 tabletop-only?**
   - Lab components (Linux, Windows, AD, EDR/AV, telemetry stack, C2 lab) are not confirmed; no written evasion authorization exists; authorization gates are unsatisfied.

4. **Why is AV/EDR bypass testing prohibited today?**
   - No isolated control lab is confirmed; no written authorization exists; would require all 10 authorization gates to be satisfied first.

5. **Why is log clearing prohibited?**
   - Clearing logs destroys the detection chain, prevents forensic analysis, violates compliance and audit controls, and undermines the defender's ability to detect and respond.

6. **Why is process injection prohibited today?**
   - High-risk without confirmed Linux/Windows host telemetry lab; can crash systems; lack of detection surface means no validation possible; scope creep risk.

7. **Why are LOLBin chains not executed today?**
   - No Windows/Linux telemetry lab confirmed; results would be unreliable; cannot validate detection; scope creep risk.

8. **What is an authorization gate?**
   - A required piece of evidence or readiness condition that must be satisfied before hands-on evasion testing is permitted (e.g., isolated lab, written authorization, telemetry stack, stop conditions).

9. **What telemetry would defenders need for future evasion validation?**
   - Host, process, command-line, file, network, and control telemetry; centralized logging; SIEM correlation; EDR/AV detection logs; baseline artifacts for before/after comparison.

10. **Why should security tools remain enabled?**
    - Security tools are part of the detection chain; disabling them breaks the investigation; prevents validation of evasion techniques; violates policy and compliance.

11. **Why should all simulated cards be labeled clearly?**
    - To prevent confusion between simulated scenarios and real events; to ensure analysis remains theoretical until hands-on testing is authorized; to avoid accidental operational impact.

12. **Why are public or production systems excluded?**
    - High legal, compliance, and security risk; potential breach or data exfiltration; violation of authorization boundaries; testing outside isolated lab is prohibited.

13. **What makes obfuscation testing risky?**
    - Can easily become evasion optimization; results are unreliable without a baseline; may develop offensive capabilities; no telemetry surface to measure against.

14. **What must cleanup verify after future authorized evasion validation?**
    - No malware, payloads, obfuscated code, or persistence remain; system state matches pre-test baseline snapshot; all telemetry is preserved; all artifacts are removed; sign-off from exercise owner.

15. **What is the safe Day 1 result?**
    - A documented, tabletop-only evasion safety and detection plan that establishes ethical boundaries, authorization gates, risk controls, and defensive strategies without executing any evasion, bypass, or tampering.

---

## 14. Day 1 Completion Checklist

Week 7 Day 1 is complete when all items below are verified:

- [x] Created `week7-day1-evasion-safety-detection-plan.md`
- [x] Performed no new technical activity (tabletop only)
- [x] Ran no bypass, evasion, payload, injection, LOLBin chain, C2, or control-tampering action
- [x] Defined defense evasion conceptually (Section 3)
- [x] Documented current lab readiness (Section 4)
- [x] Listed future authorization gates (Section 5)
- [x] Created evasion risk register (Section 6)
- [x] Built defensive control mapping (Section 7)
- [x] Created simulated event cards (Section 8)
- [x] Listed rejected activities (Section 9)
- [x] Included finding W7-O01 (Section 10)
- [x] Answered knowledge check (Section 13)
- [x] Documented cleanup procedures for future authorized work (Section 11)
- [x] Maintained evidence log (Section 12)

---

## 15. References and Next Steps

### 15.1 MITRE ATT&CK Defense Evasion (TA0005)

Reference: https://attack.mitre.org/tactics/TA0005/

Key techniques to study (tabletop only):
- Disable or Modify Tools (T1562)
- Impair Defenses (T1562)
- Obfuscated Files or Information (T1027)
- Process Injection (T1055)
- Modify System Behavior (T1554)
- Living off the Land Binaries and Scripts (T1036)

### 15.2 Next Steps (Day 2)

**Week 7 Day 2:** Logging, telemetry, and detection surfaces.

- Map host, process, command-line, file, network, and control telemetry.
- Identify gaps where evasion might succeed.
- Plan telemetry hardening and correlation.
- Create detection surface coverage map.

### 15.3 Gate Satisfaction Tracking

| Gate | Current Status | Target Completion | Owner |
|---|---|---|---|
| Isolated lab | ❌ Not confirmed | [TBD] | [Exercise lead] |
| Test host | ❌ Not confirmed | [TBD] | [Lab lead] |
| Security tool | ❌ Not confirmed | [TBD] | [Security lead] |
| Written authorization | ❌ Not confirmed | [TBD] | [Manager] |
| Logging plan | ❌ Not confirmed | [TBD] | [SIEM/SOC lead] |
| Reversible artifact | ❌ Policy enforced | N/A | [Policy] |
| Synthetic payload policy | ❌ Policy enforced | N/A | [Policy] |
| Stop condition | ❌ Policy enforced | N/A | [Policy] |
| Cleanup plan | ⚠️ Drafted | [TBD] | [Exercise lead] |
| Escalation | ❌ Not configured | [TBD] | [Exercise owner] |

---

**Document completed by:** Cody R Johnson  
**Date:** 2026-08-17  
**Review status:** Ready for knowledge check and Day 2 preparation  
**Approval:** [Exercise owner sign-off required before any hands-on work]
