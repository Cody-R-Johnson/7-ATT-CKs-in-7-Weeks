# ACME Week 5 Day 2 Listener and Traffic-Shaping Design Review

## 1. Scope and Safety

This design review was prepared for the July 23, 2026 lab window, between 11:00 AM and 2:00 PM EDT.

Day 2 is a defensive design exercise only. No listener was opened, no port was bound, no framework was run, no payload or agent was created, and no callback traffic was generated. The local ACME training application and approved repository artifacts remain the only confirmed scope; no isolated C2 server, target VM, or multi-host C2 network is confirmed.

Public interfaces, all-interface binding, public infrastructure, home LAN, cloud systems, real hosts, tunnels, proxies, reverse shells, port forwards, domain fronting, traffic hiding, and evasion are excluded.

## 2. Listener Concept

A listener is the C2 network endpoint that would receive a lab agent's check-in or callback. Conceptually:

```text
[Hypothetical lab agent] → [Listener] → [Proposed C2 server/operator]
```

This review does not implement that model. A future listener would require an isolated source, server, target, network, authorized protocol, lab-only interface, logging, stop condition, and cleanup plan.

## 3. Current Readiness

| Component | Status | Proceed? | Notes |
|---|---|---|---|
| C2 server VM | Not confirmed | No | No documented lab-only hostname, IP, snapshot, or tool approval |
| Target VM | Not confirmed | No | No documented target, account, snapshot, or authorization |
| Isolated multi-host network | Not confirmed | No | No route/interface or external-egress proof |
| Listener protocol | Not authorized | No | No protocol is selected or approved |
| Bind address | Not configured | No | No confirmed lab-only interface exists |
| Port | Not opened | No | No listener service exists |
| Callback path | Not configured | No | No agent or callback is allowed |
| Logging stack | Not confirmed | No | No listener, packet, host, firewall, or proxy collection plan exists |

Decision: **no-go for listener deployment.**

## 4. Proposed Listener Design

| Design Item | Decision | Reason |
|---|---|---|
| Protocol | Not confirmed | A protocol must be explicitly authorized for the isolated lab |
| Bind address | Not configured | A listener may bind only to a confirmed lab-only interface |
| Port | Not opened | No listener may be created before the lab is confirmed |
| Callback path | Not configured | No payload or agent callback is permitted today |
| TLS | Not evaluated | Certificate and inspection choices require a documented lab design |
| Agent identity | Not applicable | No target VM or agent exists |
| Allowed source | Not confirmed | A future source must be the named isolated target VM only |
| Allowed destination | Not confirmed | A future destination must be the named isolated C2 server only |
| Logging | Required before future testing | Preserve listener, packet, host, firewall, and relevant proxy evidence |
| Stop condition | One harmless authorized check-in | Limit future activity to minimal proof |
| Cleanup | Required before future testing | Close listener, remove temporary artifacts, preserve logs, restore snapshot if needed |

## 5. Binding and Exposure Rules

Future listener work may proceed only when all of these rules are satisfied:

- Bind only to a confirmed lab-only interface on an isolated network.
- Never bind to every interface, a public interface, home LAN, cloud system, or an unverified address.
- Permit callbacks only from the documented target VM to the documented C2 server.
- Ensure egress rules prevent any external callback path.
- Record the approved protocol, bind interface, port, logging controls, stop condition, and cleanup plan before starting.
- Verify the listener is not reachable outside the lab before any permitted test.

For Day 2: listener binding is not configured, no port is opened, callback path is not configured, and protocol is not authorized.

## 6. Traffic-Shaping Model

| Parameter | Simulated Decision | Defensive Relevance |
|---|---|---|
| Interval | Conceptual periodic check-ins only; no timing selected | Defenders can look for regular timing |
| Jitter | Discussed as a timing variable, not optimized | Timing variation remains analyzable over time |
| URI pattern | Not configured | Rare or repeated paths can be detection context |
| Client identity | Not configured | Unusual headers can support anomaly investigation |
| Payload size | No traffic generated | Consistent or outlier sizes can indicate a pattern |
| Method | Not selected | Protocol behavior should be compared with the host baseline |
| Error behavior | Not modeled operationally | Repeated failures can reveal attempted callbacks |
| Tasking burst | Conceptual only | Timing or size changes can be an operator-activity clue |
| Working-hours context | Conceptual only | Time-of-day comparison supports baselining |

Traffic shaping is documented here to help defenders recognize patterns, not to conceal traffic or bypass controls.

## 7. Simulated Beacon Timeline

| Simulated Time | Event | Defensive Observation |
|---|---|---|
| T+00 | Hypothetical check-in | A future network flow could associate the target with a listener destination |
| T+05 | Hypothetical repeat check-in | Repeated destination and timing could form a periodic pattern |
| T+10 | Hypothetical repeat check-in | Flow timing, endpoint process, and path metadata could be correlated |
| T+15 | Hypothetical idle response | Small, consistent transfer sizes could be reviewed against baseline activity |
| T+20 | Hypothetical activity change | A timing or size change could prompt investigation of related host telemetry |

The timeline is illustrative only. No traffic was sent or received.

## 8. Findings and Observations

### W5-O02: Listener Deployment Deferred Because Lab Preconditions Are Not Met

- Classification: No-go readiness observation
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - Day 1 confirmed no C2 server VM.
  - No target VM is confirmed.
  - No isolated multi-host network is confirmed.
  - No protocol, bind address, port, or logging stack is authorized.
- Impact: Opening a listener without a lab-only interface could expose a service outside authorization and create uncontrolled network artifacts.
- Limitation: No listener implementation, port binding, protocol behavior, or detection capability was evaluated.
- Recommendation: Confirm a C2 server VM, target VM, lab-only network, approved protocol, bind interface, port, logging, stop condition, and cleanup plan before any deployment.

## 9. Rejected Designs

| Rejected Design | Reason |
|---|---|
| Listener bound to every interface | Could expose the listener on interfaces outside the lab |
| Public cloud listener | Public infrastructure is excluded from the exercise |
| Home-LAN listener | It is not confirmed isolated lab infrastructure |
| DNS channel | Not authorized; no isolated DNS lab stack exists |
| HTTPS listener | No C2 server, certificate plan, bind interface, or target is confirmed |
| SMB-style channel | No Windows target or internal lab is confirmed |
| Redirector-fronted listener | Redirectors are not authorized or deployed |
| Payload callback to a listener | Payload creation and callback testing are prohibited |

## 10. Defensive Artifacts

| Hypothetical Future Action | Expected Artifact | Day 2 Status |
|---|---|---|
| Listener process starts | Process-creation event | Not observed |
| Port bind occurs | Listening socket and firewall state | Not observed |
| Callback received | Listener record and network flow | Not observed |
| Beacon repeats | Periodic flow records | Not observed |
| Web-like callback | Proxy or web-style records | Not observed |
| Encrypted callback | Flow, certificate, and endpoint telemetry | Not observed |
| Task sent | Server-side tasking record | Not observed |
| Listener closed | Process termination and socket-closure event | Not observed |

## 11. Cleanup and Recovery

No cleanup was required because no listener, configuration, payload, agent, or callback artifact was created.

Future authorized listener work must stop the listener, verify the port is closed, remove temporary listener configuration and lab-created artifacts, preserve logs, restore snapshots if state changed, and confirm no public route was exposed. Logs and shell history must remain intact.

## 12. Evidence Log

| Date/Time | Location | Action | Purpose | Result | State Changed? | Cleanup |
|---|---|---|---|---|---|---|
| 2026-07-23 11:08 AM EDT | Week 5 Day 1 plan | Readiness review | Confirm whether listener deployment can proceed | C2 server, target VM, and isolated network remain unconfirmed | No | None |
| 2026-07-23 11:36 AM EDT | Day 2 design review | Binding and exposure analysis | Define future listener guardrails | No bind address, port, or callback path configured | No | None |
| 2026-07-23 12:14 PM EDT | Day 2 design review | Traffic-pattern modeling | Document defensive indicators without generating traffic | Simulated timing and artifact model recorded | No | None |
| 2026-07-23 12:48 PM EDT | Day 2 design review | Rejected-design review | Eliminate unsafe deployment options | Public, all-interface, payload, redirector, and unconfirmed-protocol designs rejected | No | None |
| 2026-07-23 1:32 PM EDT | Day 2 design review | Cleanup review | Define recovery for future authorized test | No current artifacts; future cleanup steps recorded | No | None |

## 13. Knowledge Check

1. A listener is a network endpoint that would receive an agent’s check-in or callback.
2. It must bind only to a confirmed lab interface to prevent exposure outside the isolated exercise boundary.
3. Binding to every interface is unsafe because it can expose a service on unintended networks.
4. Selecting a protocol requires documented lab hosts, isolation, approved protocol scope, logging, egress controls, stop condition, and cleanup plan.
5. Traffic shaping describes how communication appears over time, including timing, size, behavior, and protocol context.
6. Jitter is discussed defensively because the objective is to recognize timing behavior, not optimize stealth or evade monitoring.
7. Beaconing can be detectable through periodic timing, repeated destinations, unusual paths/headers, transfer sizes, and endpoint process evidence.
8. A process-creation event can show that a listener process exists.
9. A listening socket and firewall state can show that a port is open.
10. Payload callbacks are prohibited because no target, listener, or isolated lab is confirmed.
11. Public cloud infrastructure is rejected because it is outside the controlled lab boundary.
12. A DNS channel is rejected because no authorization or isolated DNS lab stack exists.
13. Future cleanup must verify listener termination, closed port, temporary-artifact removal, preserved logs, snapshot recovery when needed, and no public exposure.
14. Logs must be preserved because they are needed to understand and detect future lab activity.
15. The safe Day 2 result when no lab exists is a non-operational no-go design review with defensive modeling only.
