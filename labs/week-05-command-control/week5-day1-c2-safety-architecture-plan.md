# ACME Week 5 Day 1 C2 Safety and Architecture Plan

## 1. Scope and Safety

This plan was prepared for the July 22, 2026 lab window, between 12:00 PM and 3:00 PM EDT.

Day 1 is planning, architecture review, and defensive analysis only. The approved scope is limited to the local ACME training application, approved repository artifacts, and a future isolated multi-host C2 lab only after its requirements are confirmed. No C2 component was deployed.

Excluded scope includes public infrastructure, LAN, personal, employer, school, cloud, production, unknown hosts, and unconfirmed virtual machines. No listener, agent, implant, payload, redirector, tunnel, proxy, port forward, beacon, or remote callback was created or run.

## 2. C2 Concept Overview

Command and control (C2) is the communication layer between an operator and a controlled system. In a future isolated lab, its conceptual components would be:

| Component | Role | Day 1 Status |
|---|---|---|
| Operator | Person controlling the exercise | Planning only |
| C2 server | Receives callbacks and sends tasks | Not deployed |
| Listener | Network endpoint for callbacks | Not opened |
| Agent / implant | Code that would run on a target | Not created |
| Beacon | Periodic agent check-in | Simulated concept only |
| Redirector | Infrastructure that forwards traffic | Not deployed |
| Payload | Initial code that would start communication | Not created |
| Tasking | Operator instruction to an agent | Not performed |
| Output | Result returned from an agent | Not collected |

## 3. Current Lab Readiness

| Component | Status | Evidence | Proceed? |
|---|---|---|---|
| Local ACME application | Confirmed | Existing local training application and repository scope | Planning only |
| Operator/source system | Not confirmed for a C2 lab | No documented isolated operator host, IP, or account | No |
| C2 server VM | Not confirmed | No hostname, IP, snapshot, tool approval, or listener design | No |
| Target VM | Not confirmed | No isolated target hostname, IP, account, or snapshot | No |
| Isolated multi-host network | Not confirmed | Week 4 deferred host/domain testing for this same gap | No |
| Allowed listener protocol | Not confirmed | No protocol-specific authorization | No |
| Egress controls | Not confirmed | No lab-only route or internet-blocking evidence | No |
| Defensive logging stack | Not confirmed | No packet, host, process, firewall, or proxy telemetry plan | No |

Decision: **no-go for hands-on C2 deployment.**

## 4. Proposed Non-Operational Architecture

```text
[Operator notes]
      |
      | planning only; no tasking or connection
      v
[Proposed C2 server — not deployed]
      |
      | simulated beacon traffic concept only
      v
[Proposed target VM — not confirmed]
```

This is an architecture discussion, not an implementation. It does not define a tool configuration, listener address, callback path, payload, or target connection.

## 5. Required Preconditions for Future Hands-On C2

| Requirement | Needed Evidence |
|---|---|
| Isolated network | Host-only or internal-network proof, separated from external and production routes |
| Source/operator system | Confirmed hostname, IP, account, and snapshot |
| C2 server | Confirmed hostname, lab-only IP, account, snapshot, and approved tool |
| Target VM | Confirmed hostname, lab-only IP, account, and snapshot |
| Allowed protocol | Explicit authorization naming the permitted protocol and limits |
| Listener binding | Lab-only interface; never a public or all-interface binding |
| Payload controls | Clearly labeled, reversible lab artifact with written approval |
| Egress rules | Lab-only routes with no internet callback path |
| Logging plan | Packet, host, process, firewall, and relevant proxy telemetry plan |
| Stop condition | Stop after one harmless, authorized check-in |
| Cleanup plan | Terminate agent, remove temporary files, close listener, and restore snapshot as needed |

If any requirement remains incomplete, hands-on C2 work remains no-go.

## 6. Traffic Pattern Concepts

| Pattern | Defensive Relevance |
|---|---|
| Beacon interval | Regular timing can create a periodic network indicator |
| Jitter | Timing variation may reduce regularity but remains observable over time |
| Protocol | Network, proxy, firewall, and service logs provide different visibility by protocol |
| HTTP client identity | Unusual headers can help identify anomalous clients |
| URI pattern | Repeated rare paths can be useful detection context |
| Payload size | Consistent or outlier transfer sizes can support investigation |
| Traffic direction | Unexpected egress or internal flows can expose policy gaps |
| Encryption | Changes visibility but does not remove endpoint, flow, timing, or destination evidence |
| Tasking frequency | Bursts of activity can differ from normal periodic behavior |

## 7. Defensive Detection Questions

1. Which host initiated the traffic?
2. Which process opened the connection?
3. What destination was contacted, and is it expected for that host?
4. Is the timing periodic, rare, or inconsistent with the host baseline?
5. Is the protocol, path, header pattern, and transfer size expected?
6. Did traffic bypass expected proxy or egress-control paths?
7. Does endpoint telemetry show an unknown binary, file, process tree, or command line?
8. Are firewall, proxy, DNS, network-flow, and host records preserved for correlation?

## 8. Findings and Observations

### W5-O01: C2 Deployment Deferred Because Lab Preconditions Are Not Met

- Classification: No-go readiness observation
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - No isolated C2 server VM is confirmed.
  - No target VM is confirmed.
  - No lab-only listener protocol is authorized.
  - No egress-control or defensive-logging plan is confirmed.
  - Week 4 also deferred host/domain testing because a multi-host lab was not confirmed.
- Impact: Deploying C2 without these controls could create unsafe callbacks, unauthorized exposure, or uncontrolled artifacts.
- Limitation: This does not evaluate any C2 tool, implementation, or detection capability.
- Recommendation: Provision an isolated lab with documented source, server, target, logging, stop condition, cleanup, and written authorization before any future emulation.

## 9. Prohibited Actions

- Deploying agents, implants, beacons, listeners, redirectors, or payloads
- Opening callback listeners or testing remote callbacks
- Creating reverse shells, tunnels, SOCKS proxies, or port forwards
- Running C2 frameworks against a host
- Using public infrastructure, domain fronting, traffic hiding, or evasion
- Exfiltrating data or staging data for exfiltration
- Creating persistence or disabling security controls
- Testing against non-isolated, personal, school, employer, cloud, LAN, public, or production systems

## 10. Defensive Artifacts Plan

| Future Action | Expected Artifact | Preserve? |
|---|---|---|
| Start listener | Open port, process event, firewall state | Yes |
| Agent launch | Process creation, file creation, command-line telemetry | Yes |
| Beacon check-in | Network flow, proxy/firewall record, endpoint telemetry | Yes |
| Tasking | Server-side record and host command telemetry | Yes |
| Output return | Network flow and server-side record | Yes |
| Redirector forwarding | Web-server or proxy records | Yes |
| Agent cleanup | Process termination and file-deletion event | Yes |
| Snapshot restore | Hypervisor event | Yes |

These are planned artifacts only; none were created on Day 1.

## 11. Cleanup and Recovery Plan

No cleanup was required because no C2 component or temporary artifact was created.

For future authorized work, cleanup must be planned before deployment: terminate the lab agent, close the lab-only listener, remove lab-created temporary files, preserve required telemetry, verify no public route existed, and restore the appropriate VM snapshot if state changed. Logs and shell history must not be cleared.

## 12. Evidence Log

| Date/Time | Location | Action | Purpose | Result | State Changed? | Cleanup |
|---|---|---|---|---|---|---|
| 2026-07-22 12:08 PM EDT | Week 5 brief and Week 4 evidence | Scope and prerequisite review | Confirm whether C2 deployment is safe | Multi-host C2 lab remains unconfirmed | No | None |
| 2026-07-22 12:37 PM EDT | Approved ACME repository | Architecture review | Define non-operational components and boundaries | Planning diagram and component status recorded | No | None |
| 2026-07-22 1:16 PM EDT | Day 1 plan | Traffic and detection analysis | Identify defensive questions without generating traffic | Concepts and artifacts documented | No | None |
| 2026-07-22 1:54 PM EDT | Day 1 plan | No-go decision | Prevent unsafe deployment | No listener, agent, or payload created | No | None |
| 2026-07-22 2:35 PM EDT | Day 1 plan | Cleanup and recovery review | Define future rollback requirements | No temporary C2 artifacts require cleanup | No | None |

## 13. Knowledge Check

1. Command and control is the communication layer between an operator and a controlled system.
2. A listener is the network endpoint that would receive callbacks; an agent is code that would run on a target and initiate or maintain communication.
3. Beaconing is periodic check-in behavior by an agent; Day 1 treats it only as a simulated concept.
4. C2 is unsafe without an isolated lab because callbacks, artifacts, and traffic could reach systems outside authorization.
5. A listener must not bind to public interfaces because it could expose an unauthorized service outside the lab boundary.
6. A lab listener needs documented isolation, lab-only address, authorized protocol, server/target snapshots, logging, egress controls, stop condition, and cleanup plan.
7. Redirectors are not used today because no isolated infrastructure or hands-on authorization exists.
8. Repeated timing, unusual destinations, path/header patterns, and transfer sizes can make beaconing detectable.
9. A C2 listener could create open-port, process, firewall, network, and server-log artifacts.
10. Payloads must be clearly labeled lab-only so they cannot be confused with or reused as real operational code.
11. Cleanup is critical to remove temporary lab artifacts, close listeners, restore state, and preserve learning telemetry.
12. Public infrastructure is excluded because it broadens exposure beyond the controlled lab.
13. Traffic hiding or evasion is prohibited because Day 1 is defensive planning, not stealth or bypass testing.
14. The safe Day 1 result for an incomplete lab is a documented no-go architecture and readiness plan.
15. Hands-on C2 emulation requires confirmed isolated source, server, and target systems; lab-only routes; approved protocol/tool; logging; stop condition; cleanup; and written authorization.
