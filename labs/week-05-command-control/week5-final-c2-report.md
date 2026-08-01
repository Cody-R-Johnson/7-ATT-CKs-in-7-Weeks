# ACME Week 5 Final Command-and-Control Report

## 1. Executive Summary

This Week 5 command-and-control (C2) review assessed whether the ACME lab was ready for C2 architecture, listener, redirector, beaconing, exfiltration, and purple-team emulation exercises. The local ACME training application and approved repository artifacts were available, but no isolated C2 server, target VM, redirector VM, approved protocol, logging stack, synthetic-dataset authorization, or written hands-on authorization was confirmed.

All operational C2 activities were therefore correctly deferred. No listener, agent, payload, implant, redirector, callback, beacon traffic, tunnel, proxy, public infrastructure, or data transfer was created. The week produced non-operational architecture plans, simulated detection models, tabletop event cards, rejected-design analysis, cleanup requirements, and future validation criteria.

Operational C2 risk is **Not Rated** because no operational C2 capability was deployed, tested, or observed. Planning/readiness risk is **Informational** because the lab does not yet have the isolated infrastructure and authorization required for safe hands-on emulation.

## 2. Scope and Authorization

Approved scope:

- Local ACME training application: `http://127.0.0.1:8000`
- Approved repository artifacts and Week 5 reports
- Future isolated C2 lab only after explicit confirmation

Excluded scope:

- Public, personal, employer, school, cloud, LAN, production, unknown, or unconfirmed systems
- Public VPSs, CDNs, public DNS, and domain fronting
- Real data, credentials, sessions, tokens, keys, and application records for transfer

## 3. Rules of Engagement

- Planning and simulation only.
- No C2 deployment, listener, or port binding.
- No agent, implant, payload, or beacon.
- No redirector, forwarding rule, tunnel, proxy, reverse shell, or port forward.
- No public infrastructure or data movement.
- No stealth tuning, evasion, security-control disabling, or log clearing.
- Preserve logs and shell history.
- Stop when authorization, isolation, route, protocol, dataset, logging, or cleanup is unclear.

## 4. Methodology

1. Reviewed C2 components and required lab prerequisites.
2. Checked readiness for source, target, C2 server, network, protocol, logging, and authorization.
3. Modeled listener design without opening a listener.
4. Modeled redirector separation without deploying infrastructure.
5. Created a fictional beacon dataset and defender detection logic without generating telemetry.
6. Created a synthetic-only data-staging policy and exfiltration control plan.
7. Created tabletop event cards and a purple-team communications plan.
8. Rejected unsafe designs and documented future cleanup and validation requirements.

No system state changed.

## 5. Results Summary

| ID | Result | Classification | Confidence |
|---|---|---|---|
| W5-O01 | C2 deployment deferred because lab preconditions were not met | No-go readiness observation | Confirmed |
| W5-O02 | Listener deployment deferred | No-go readiness observation | Confirmed |
| W5-O03 | Redirector deployment deferred | No-go readiness observation | Confirmed |
| W5-O04 | Live beacon testing deferred | No-go readiness observation | Confirmed |
| W5-O05 | Live exfiltration deferred | No-go readiness observation | Confirmed |
| W5-O06 | Hands-on purple-team C2 emulation deferred | No-go readiness observation | Confirmed |
| W5-O07 | Simulated detection models created without telemetry generation | Planning control | High |
| W5-O08 | Unsafe C2 designs rejected | Planning control | High |

## 6. C2 Readiness Findings

### W5-O01: C2 Deployment Deferred

- Classification: No-go readiness observation
- Evidence: No isolated source/operator host, target VM, C2 server VM, approved tool, protocol, egress-control plan, or logging stack was confirmed.
- Impact: Deployment could create unauthorized callbacks, uncontrolled artifacts, or exposure beyond the lab.
- Limitation: No C2 tool, listener, agent, or detection capability was evaluated.
- Recommendation: Confirm isolated source, server, target, protocol, logging, stop condition, cleanup, and written authorization before any hands-on emulation.

### W5-O02: Listener Deployment Deferred

- Classification: No-go readiness observation
- Evidence: No C2 server VM, target VM, isolated network, authorized protocol, lab-only bind interface, port, or logging stack was confirmed.
- Impact: Opening a listener could expose a service outside authorization.
- Limitation: No listener implementation or protocol behavior was evaluated.
- Recommendation: Authorize a named lab-only server, interface, port, protocol, source target, logging plan, stop condition, and cleanup before deployment.

### W5-O03: Redirector Deployment Deferred

- Classification: No-go readiness observation
- Evidence: No redirector VM, backend C2 VM, target VM, isolated C2 network, forwarding rule, listener, firewall rule, or logging plan was confirmed.
- Impact: A redirector could forward unauthorized traffic or create uncontrolled infrastructure artifacts.
- Limitation: No redirector configuration, forwarding, or defensive correlation was evaluated.
- Recommendation: Provision lab-only redirector, backend, target, source/destination restrictions, logs, stop condition, cleanup, snapshots, and written authorization.

### W5-O04: Live Beacon Testing Deferred

- Classification: No-go readiness observation
- Evidence: No agent, target VM, listener, C2 server, isolated network, protocol authorization, or logging stack was confirmed.
- Impact: Live traffic could create unauthorized callbacks or misleading telemetry.
- Limitation: No real network detection capability or C2 traffic was evaluated.
- Recommendation: Keep beaconing simulated until an isolated C2 lab, approved tool/protocol, logging stack, stop condition, cleanup plan, and written authorization are confirmed.

### W5-O05: Live Exfiltration Deferred

- Classification: No-go readiness observation
- Evidence: No isolated target, receiver, listener, drop site, approved exfiltration channel, synthetic movement dataset, or DLP/network/host/server logging plan was confirmed.
- Impact: Moving data could expose real files, secrets, or unauthorized traffic.
- Limitation: No exfiltration capability or DLP detection was evaluated.
- Recommendation: Use only authorized synthetic data in an isolated lab with written scope, logging, stop conditions, and cleanup before a future test.

### W5-O06: Hands-On Purple-Team C2 Emulation Deferred

- Classification: No-go readiness observation
- Evidence: No source host, target VM, C2 server, redirector, approved protocol, logging stack, defensive telemetry-validation environment, or written authorization was confirmed.
- Impact: An emulation could create unauthorized traffic, uncontrolled artifacts, or misleading detection results.
- Limitation: No detection rule or response workflow was tested.
- Recommendation: Continue tabletop planning until isolated infrastructure, assigned participants, written authorization, telemetry sources, stop conditions, and cleanup procedures are confirmed.

## 7. Simulated Models and Defensive Logic

| Model | Status | Purpose |
|---|---|---|
| Non-operational C2 architecture | Simulated | Component and containment planning |
| Listener design | Simulated | Lab-only binding and exposure rules |
| Traffic-shaping model | Simulated | Defender timing and anomaly analysis |
| Redirector diagram | Simulated | Infrastructure separation and logging requirements |
| Beacon dataset | Simulated | Detection logic and false-positive review |
| Exfiltration staging table | Simulated | Data-movement safeguards and controls |
| Purple-team event cards | Simulated | Detection, response, communications, and cleanup planning |

No simulated model generated real traffic, files, processes, callbacks, ports, listeners, or telemetry.

## 8. Rejected Designs and Activities

| Rejected Item | Reason |
|---|---|
| Listener bound to every interface | Could expose a service on unintended interfaces |
| Public VPS or cloud listener | Public infrastructure is excluded |
| Home-LAN listener or port forward | Not isolated lab infrastructure |
| DNS channel | No isolated DNS lab stack or authorization |
| Domain fronting or CDN fronting | Third-party/public infrastructure is excluded |
| Redirector without logs | Removes defensive learning and evidence correlation |
| Redirector to unconfirmed backend | No authorized destination |
| Payload callback | Payload creation and callback testing are prohibited |
| Synthetic callbacks | No listener, route, or logging stack |
| DNS tunneling | Not authorized and abuse-prone |
| Real-data exfiltration | Real data movement is prohibited |
| Stealth tuning | Evasion optimization is prohibited |
| Disabling EDR or logging | Security-control disabling is prohibited |

## 9. Defensive Artifact Summary

| Future Activity | Potential Artifacts | Week 5 Status |
|---|---|---|
| Listener start | Process creation, socket state, firewall event | Expected only; not observed |
| Agent launch | Process tree, file artifact, command line | Expected only; not observed |
| Beaconing | Network flow, proxy, DNS, listener records | Expected only; not observed |
| Redirector forwarding | Access records, backend records, flow correlation | Expected only; not observed |
| Data staging | File access, archive creation, process events | Expected only; not observed |
| Exfiltration attempt | DLP, proxy, firewall, CASB, DNS, SIEM records | Expected only; not observed |
| Purple-team communications | Timeline, tickets, coordination records | Planning-only records |
| Cleanup | Process termination, file deletion, closed ports, snapshot restore | Expected only; not observed |

## 10. Cleanup and Evidence Handling

- No operational component, temporary payload, listener, port, redirector, transfer channel, data artifact, or remote session was created.
- No live secret, credential, token, session, or application record was retained or moved.
- No system configuration, firewall rule, forwarding rule, service, or security control was modified.
- No logs, shell history, or other defensive telemetry was cleared.
- Future cleanup must terminate processes, close ports, remove only authorized temporary artifacts, preserve telemetry, restore snapshots when needed, and verify no public route or external contact occurred.

## 11. Risk Rating

| Area | Rating | Basis |
|---|---|---|
| Operational C2 | Not Rated | No operational C2 capability was deployed, tested, or observed |
| Planning/readiness | Informational | Required isolated infrastructure, protocol authorization, logging, dataset authorization, stop conditions, cleanup, and written approval are absent |

No Medium or High operational risk is assigned without operational evidence.

## 12. Requirements for Future Hands-On C2 Validation

| Requirement | Description |
|---|---|
| Isolated source/operator host | Hostname, IP, account, and snapshot |
| Isolated target VM | Hostname, IP, account, and snapshot |
| C2 server VM | Hostname, IP, account, and snapshot |
| Optional redirector VM | Hostname, IP, account, and snapshot |
| Network isolation | Host-only/internal network proof with no public or external route |
| Approved protocol | Explicitly named and bounded |
| Listener binding | Lab-only interface only |
| Egress controls | No public or external callback path |
| Logging stack | Host, network, listener, firewall, proxy, and DNS evidence as needed |
| Synthetic dataset | Approved fictional data only |
| Written authorization | Hosts, protocols, techniques, timing, and stop conditions |
| Cleanup plan | Terminate processes, close ports, remove temporary files, restore snapshots |
| Defensive artifact plan | Evidence defenders should observe and preserve |

## 13. Limitations

- No C2 server, target VM, redirector VM, isolated network, or approved protocol was confirmed.
- No listener, payload, agent, traffic, beaconing, or data transfer occurred.
- No live detection rule or response workflow was validated.
- No public infrastructure was used.
- This report makes no conclusion about real-world C2 detection capability.

## 14. Evidence Timeline

| Date | Activity | Outcome |
|---|---|---|
| July 22, 2026 | C2 safety and architecture plan | Deployment deferred |
| July 23, 2026 | Listener design review | Listener deferred |
| July 25, 2026 | Redirector architecture plan | Redirector deferred |
| July 26, 2026 | Beaconing detection analysis | Live beaconing deferred |
| July 27, 2026 | Exfiltration control plan | Live data movement deferred |
| July 28, 2026 | Purple-team C2 plan | Hands-on emulation deferred |
| July 30, 2026, 12:00–4:00 PM EDT | Final C2 synthesis | Week 5 planning evidence consolidated |

## 15. Week 5 Reflection

C2 requires stricter containment than many earlier exercises because it can create remote communications, listening services, data movement, and persistent artifacts. The no-go decisions were useful because they prevented the project from treating a local application or fictional architecture as authorization for network operations.

The simulated beacon dataset and defender triage questions were the most useful models because they connect timing, destination, size, and process context to practical investigation without producing traffic. Rejecting public infrastructure and all-interface listener binding was especially important because both could breach the lab boundary. Tabletop event cards give defenders a repeatable way to practice visibility, correlation, response, and cleanup before a future isolated exercise.

Hands-on C2 becomes appropriate only after isolated hosts, a contained network, lab-only addresses, approved protocol/tooling, comprehensive logging, synthetic data authorization, written scope, stop conditions, and cleanup/rollback controls are in place.

## 16. Knowledge Check

1. **Why was operational C2 risk Not Rated?** No operational C2 capability was deployed, tested, or observed.
2. **Why is planning/readiness risk Informational?** The lab lacks the isolated infrastructure, authorization, protocol scope, logging, synthetic-dataset approval, stop conditions, and cleanup plan needed for safe hands-on work.
3. **Why were all hands-on C2 activities deferred?** The required source, target, C2 server, optional redirector, isolated network, approved protocol, logging, and written authorization were not confirmed.
4. **Why is binding to all interfaces unsafe?** It can expose a listening service on unintended networks outside the lab boundary.
5. **Why is public infrastructure excluded?** It extends the exercise beyond controlled, authorized infrastructure and can create external exposure.
6. **Why was redirector deployment deferred?** No redirector, backend C2, target, isolated network, forwarding scope, or logging plan was confirmed.
7. **Why was live beacon testing deferred?** No agent, target, listener, C2 server, isolated route, protocol authorization, or logging stack existed.
8. **Why was live exfiltration deferred?** No authorized synthetic dataset, isolated source/receiver, channel, or defensive-control plan was available.
9. **Why are simulated event cards useful?** They let teams rehearse expected evidence, detection questions, response, and cleanup without generating activity.
10. **Why are defensive artifacts marked expected rather than observed?** The report documents planned future behaviors; Week 5 did not create operational C2 telemetry.
11. **Why is stealth tuning prohibited?** The objective is safe defensive visibility and containment, not evasion or bypass.
12. **Why is real data movement prohibited?** It could expose sensitive information and send data outside the authorized boundary.
13. **Why is a logging stack required?** It enables defenders to observe, correlate, investigate, and preserve evidence from a future authorized test.
14. **What must be confirmed before launching a future agent?** Isolated source and target systems, lab-only addresses, approved tool/protocol, written authorization, logging, stop condition, cleanup, and reversible payload controls.
15. **What must cleanup verify after a future C2 exercise?** Components stopped, ports closed, temporary artifacts removed, logs preserved, snapshots restored where needed, and no external route or contact occurred.
