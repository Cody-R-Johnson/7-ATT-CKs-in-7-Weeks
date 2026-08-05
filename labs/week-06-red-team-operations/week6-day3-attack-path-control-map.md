# ACME Week 6 Day 3 Attack-Path Planning and Control Mapping

**Theme:** Building evidence-bound attack paths without executing them
**MITRE ATT&CK context:** Reconnaissance (TA0043), Initial Access (TA0001), and Command and Control (TA0011)
**Mode:** Tabletop planning only

## 1. Executive Summary

This tabletop plan translates the fictional `ACME-SIM-ADV-01` profile into possible, evidence-bound attack paths. It uses confirmed prior ACME reports to model application-layer findings, defensive controls, detection questions, and readiness gaps without running attacks or asserting outcomes beyond the evidence.

No new reconnaissance, scanning, credential testing, SQLi/XSS replay, session testing, payload creation, C2 activity, lateral movement, persistence, evasion, or public/production activity occurred.

## 2. Scope and Safety

An attack path is a sequence of conditions and actions that could lead from a starting point to an objective: **starting condition → action or weakness → control response → possible outcome**. For Day 3, paths organize prior evidence only; they are not execution instructions or authorization for new activity.

Allowed work is limited to reviewing prior reports, creating tabletop path diagrams, mapping controls and detections, applying status labels, rejecting unsupported paths, and documenting future validation requirements. The Week 6 Day 1 rules of engagement and `ACME-STOP` remain controlling boundaries.

## 3. Path Status Labels

| Label | Meaning |
|---|---|
| Confirmed | Supported by prior authorized evidence |
| Controlled lab evidence | Previously demonstrated only in the local lab |
| Blocked | A control prevented or limited the path |
| Deferred | Required lab conditions are missing |
| Hypothetical | Possible future path, not observed or authorized |
| Rejected | Unsupported, unsafe, or outside scope |

## 4. Confirmed Evidence Inputs

| Evidence Input | Source | Use |
|---|---|---|
| Passive recon and application mapping | Week 1 reports | Establish previously identified local application routes |
| Route and control assessment | Week 2 reports | Provide documented route and control context |
| Controlled SQLi and stored-XSS findings | Week 3 reports | Support application-layer paths only; do not replay |
| Host, AD, credential, and lateral-movement no-go decisions | Week 4 reports | Identify deferred and rejected post-exploitation paths |
| C2, listener, redirector, beaconing, and exfiltration no-go decisions | Week 5 reports | Identify deferred and rejected C2 paths |
| Fictional adversary profile | Week 6 Day 2 | Keep campaign narrative evidence-bound |

## 5. Candidate Attack Paths

### Path A: Web Exposure to Controlled SQLi Finding

**Passive recon context → vendor search route identified → designated lab SQLi mode referenced → controlled SQLi behavior previously validated → no host access or data dump**

| Step | Evidence | Status | Control / Limitation |
|---|---|---|---|
| Route identified | Prior app mapping | Confirmed | Route exists in the local training application |
| SQLi lab mode tested | Week 3 controlled validation | Controlled lab evidence | Evidence is limited to the designated lab behavior |
| Data extraction | Not performed | Rejected | No extraction was authorized or performed |
| Host access | Not demonstrated | Rejected | No host context or access evidence exists |
| Defensive focus | Input validation and query safety | Confirmed | Planning focus only |

**Conclusion:** This path supports an application-layer SQLi finding only. It does not support host access, credential exposure, lateral movement, or a database dump.

### Path B: Support Submission to Stored-XSS Lab Preview

**Unauthenticated support form → ticket submitted → admin ticket view → unsafe lab preview → local browser alert only**

| Step | Evidence | Status | Control / Limitation |
|---|---|---|---|
| Support route exists | Prior app mapping | Confirmed | Local training route only |
| Stored XSS validated | Week 3 controlled validation | Controlled lab evidence | Limited to designated lab behavior |
| Safe table encoding | Prior positive control | Blocked | Encoding provides a partial control in the safe table view |
| Unsafe preview behavior | Week 3 lab finding | Controlled lab evidence | Limited to the unsafe preview behavior |
| Cookie theft | Not tested and not allowed | Rejected | Session material handling prohibits it |
| Admin takeover | Not demonstrated | Rejected | No privileged action was demonstrated |
| Host access | Not demonstrated | Rejected | No host access evidence exists |

**Conclusion:** This path supports a controlled stored-XSS finding in the designated preview behavior only. It does not support account takeover, cookie theft, host access, or C2.

### Path C: Web Finding to Post-Exploitation Readiness Gap

**Validated web finding → attempt to infer host access → host/domain prerequisites missing → no-go decision**

| Step | Evidence | Status | Control / Limitation |
|---|---|---|---|
| Web findings exist | Week 3 | Controlled lab evidence | Application-layer findings only |
| Linux host testing | No Linux VM | Deferred | Isolated host and account are required |
| Windows host testing | No Windows VM | Deferred | Isolated host and account are required |
| AD relationship mapping | No AD lab | Deferred | Isolated AD environment and logging are required |
| Privilege escalation | No host context | Rejected | No authorized host path exists |
| Lateral movement | No source/target systems | Rejected | No source, target, route, or identity is available |

**Conclusion:** No host or domain attack path is supported by current evidence.

### Path D: C2 Readiness Path

**Campaign objective → consider listener, redirector, and beaconing → isolated C2 lab missing → no-go decision**

| Step | Evidence | Status | Control / Limitation |
|---|---|---|---|
| C2 architecture planned | Week 5 | Confirmed | Planning context only |
| Listener | No C2 server or target VM | Deferred | Isolated infrastructure, binding rules, and logging are required |
| Redirector | No redirector, backend, or target | Deferred | Infrastructure and authorization are absent |
| Beaconing | No agent, listener, or network | Deferred | No authorized communications path exists |
| Exfiltration | No dataset, channel, or logging | Deferred | Synthetic data and controlled receiver are required |
| Operational C2 | Not deployed | Rejected | Outside the current tabletop scope |

**Conclusion:** C2 remains a readiness gap and future planning topic only.

## 6. Control and Detection Mapping

| Attack-Path Element | Relevant Control | Detection Question |
|---|---|---|
| Public route discovery | Asset inventory, application routing review | Are exposed routes expected? |
| Vendor query input | Input validation, parameterized queries | Are unusual query patterns logged? |
| Support form submission | Input validation, content moderation | Are script-like submissions detected? |
| Ticket rendering | Output encoding, content security policy | Is untrusted content encoded everywhere? |
| Login and session | Authentication controls, logout invalidation, cookie flags | Are session transitions logged? |
| Protected routes | Authorization checks | Are 403/303 responses monitored? |
| Credential-like material | Secret scanning, redaction | Are fake and real values clearly separated? |
| Host access | EDR, local logging, privilege controls | Is there any confirmed host context? |
| C2 behavior | Firewall, proxy, DNS, endpoint telemetry | Is a C2 lab and logging stack confirmed? |
| Data movement | DLP, EDR, proxy, CASB | Is only synthetic data authorized? |

## 7. Rejected Unsupported Chains

| Rejected Chain | Reason |
|---|---|
| SQLi → database dump | Data extraction was not performed or authorized |
| SQLi → command execution | No command-execution evidence exists |
| SQLi → host shell | No host-access evidence exists |
| XSS → cookie theft | Cookie access was not tested and session-material handling prohibits it |
| XSS → admin takeover | No privileged action was demonstrated |
| XSS → C2 deployment | No payload, agent, listener, or host context exists |
| Fake config → intranet compromise | Training values and hosts are fictional |
| Lab credential reference → credential reuse | No credential validation or reuse is authorized |
| Web finding → lateral movement | No source/target host pair exists |
| C2 plan → operational C2 | Required infrastructure and authorization are absent |

## 8. Findings and Observations

### W6-O03: Attack Paths Limited to Application-Layer Evidence and Readiness Gaps

- Classification: Planning control
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - Week 3 confirmed controlled SQLi and stored-XSS lab findings.
  - Week 4 deferred host, AD, credential-reuse, and lateral-movement activity.
  - Week 5 deferred C2, listener, redirector, beaconing, and exfiltration activity.
  - Week 6 Day 2 limited the emulation profile to prior evidence.
- Impact: The campaign can model application-layer risk and readiness gaps, but cannot support claims of host compromise, domain compromise, C2 execution, data exfiltration, or lateral movement.
- Limitation: No new attack path was technically validated on Day 3.
- Recommendation: Keep attack paths evidence-bound; require isolated infrastructure, telemetry, written authorization, and cleanup controls before validating any deferred path.

## 9. Future Validation Requirements

| Future Path | Requirement Before Testing |
|---|---|
| SQLi expansion | Written authorization, synthetic dataset, strict data limits |
| XSS follow-up | Written authorization, safe browser context, no credential/session capture |
| Host validation | Confirmed isolated Linux/Windows VM, snapshot, account |
| AD validation | Confirmed isolated AD lab, domain user, DC/member host, logging |
| Lateral movement | Source host, target host, protocol, route, identity, stop condition |
| C2 validation | C2 server, target VM, protocol, listener binding, logging, cleanup |
| Exfiltration simulation | Synthetic dataset, receiver, DLP/logging, no external path |

## 10. Cleanup and Evidence Handling

No technical action or operational artifact was created, so no operational cleanup is required. Retain this plan as sanitized planning evidence. Any future test evidence must be minimal, source-linked, free of credentials or secrets, and clearly labeled as confirmed, simulated, or hypothetical.

## 11. Evidence Log

| Item | Source | Status | Notes |
|---|---|---|---|
| Application route context | Weeks 1–2 reports | Confirmed | Prior evidence review only |
| SQLi and stored-XSS findings | Week 3 reports | Controlled lab evidence | Referenced; not replayed |
| Host and domain limitations | Week 4 reports | Deferred | No isolated host or AD lab confirmed |
| C2 limitations | Week 5 reports | Deferred | No C2 infrastructure or logging stack confirmed |
| Emulation boundary | Week 6 Day 2 profile | Confirmed | Fictional and evidence-bound profile retained |
| Attack-path plan | This document | Confirmed planning | No new technical activity |

## 12. Knowledge Check

1. **What is an attack path?** A sequence of conditions and actions that could lead from a starting point to an objective.
2. **Why are Day 3 paths planning-only?** They organize existing evidence without authorizing or performing attacks.
3. **What does “confirmed” mean?** It is supported by prior authorized evidence.
4. **What does “controlled lab evidence” mean?** It was previously demonstrated only in the local lab.
5. **What does “deferred” mean?** Required lab conditions are missing, so the step is not currently validated or authorized.
6. **What does “rejected” mean?** The chain is unsupported, unsafe, or outside the approved scope.
7. **Why does SQLi not imply host access here?** The evidence supports only a controlled application-layer finding; no host access was demonstrated.
8. **Why does XSS not imply admin takeover here?** No cookie access, privileged action, or account takeover was tested or shown.
9. **Why is fake config not a path to intranet compromise?** Training values and hosts are fictional and cannot establish a real target path.
10. **Why are Week 4 host/domain paths deferred?** The required Linux, Windows, and AD lab conditions are not confirmed.
11. **Why are Week 5 C2 paths deferred?** The required C2 server, target VM, communications path, telemetry, and authorization are absent.
12. **Why should unsupported chains be listed?** Listing them prevents overclaiming and makes safety and evidence boundaries explicit.
13. **What control maps to SQLi?** Input validation and parameterized queries, supported by query-pattern logging.
14. **What control maps to stored XSS?** Output encoding and content security policy, supported by detection of script-like submissions.
15. **What must change before deferred paths can be validated?** The required isolated infrastructure, written authorization, telemetry, stop conditions, and cleanup controls must be confirmed.
