# ACME Week 5 Day 3 Redirector and Infrastructure Separation Plan

## 1. Scope and Safety

This plan was prepared for the July 25, 2026 lab window, between 12:00 PM and 3:00 PM EDT.

Day 3 is architecture planning and defensive analysis only. No redirector, listener, agent, payload, proxy, tunnel, forwarding rule, firewall rule, port, callback, or public infrastructure was deployed or configured. The local ACME training application and approved repository artifacts remain the only confirmed scope.

Public VPSs, cloud services, home routers, LAN interfaces, domain fronting, CDNs, traffic hiding, evasion, real hosts, and unconfirmed virtual machines are excluded.

## 2. Redirector Concept

A redirector is an intermediate system that would receive traffic and forward it to a backend service. In a future isolated lab, the conceptual sequence would be:

```text
[Proposed target VM] → [Proposed redirector VM] → [Proposed backend C2 VM]
```

This plan does not define or implement a working route, tool, configuration, address, port, or callback. The purpose is to understand containment, logging, and defensive visibility.

## 3. Why Infrastructure Separation Matters

| Layer | Purpose |
|---|---|
| Edge | Would receive traffic only from the confirmed lab target |
| Forwarding layer | Would route only documented lab traffic to an approved backend |
| Backend C2 | Would retain controlled tasking and operator records in the lab |
| Logging layer | Would preserve evidence for defenders and post-exercise review |
| Cleanup layer | Would support rule removal, teardown, and snapshot recovery |

In this course, separation serves safe containment and observability. It is not used to conceal infrastructure or avoid detection.

## 4. Current Readiness

| Component | Status | Proceed? | Notes |
|---|---|---|---|
| Redirector VM | Not confirmed | No | No documented hostname, lab IP, account, or snapshot |
| Backend C2 VM | Not confirmed | No | No documented hostname, lab IP, account, or snapshot |
| Target VM | Not confirmed | No | No documented target, account, or snapshot |
| Isolated C2 network | Not confirmed | No | No host-only/internal network evidence |
| Allowed protocol | Not authorized | No | No protocol-specific scope exists |
| Listener | Not opened | No | Listener deployment remains no-go |
| Payload or agent | Not created | No | Creation is prohibited |
| Logging stack | Not confirmed | No | No packet, host, firewall, redirector, or backend plan exists |

Decision: **no-go for redirector deployment.**

## 5. Non-Operational Architecture

```text
[Proposed target VM — not confirmed]
        |
        | no callback; no traffic generated
        v
[Proposed redirector VM — not deployed]
        |
        | no forwarding rule configured
        v
[Proposed backend C2 VM — not deployed]
```

All components are placeholders. No communication path exists.

## 6. Required Preconditions for Future Redirector Work

| Requirement | Needed Evidence |
|---|---|
| Isolated lab network | Host-only/internal network proof, with no external or production route |
| Redirector VM | Confirmed hostname, lab-only IP, account, and snapshot |
| Backend C2 VM | Confirmed hostname, lab-only IP, account, and snapshot |
| Target VM | Confirmed hostname, lab-only IP, account, and snapshot |
| Allowed protocol | Explicit written authorization for a named protocol and limits |
| Forwarding rule | Named source, destination, port, purpose, and stop condition |
| Bind interface | Confirmed lab-only address; never every interface or public interface |
| Logging | Redirector, backend, packet, host, and firewall telemetry plan |
| Firewall rules | Lab-only source/destination restrictions with deny visibility |
| Stop condition | One harmless authorized check-in or synthetic request |
| Cleanup plan | Rule removal, port closure, process stop, temporary-artifact removal, and snapshot recovery |
| Written authorization | Specific hosts, protocol, allowed action, and test bounds |

## 7. Future Lab-Only Routing Design

| Route Element | Planned Value | Status |
|---|---|---|
| Source | Confirmed target VM only | Not confirmed |
| Destination | Confirmed redirector lab interface only | Not confirmed |
| Forward target | Confirmed backend C2 lab interface only | Not confirmed |
| Protocol | Explicitly authorized protocol | Not confirmed |
| Port | Lab-only documented port | Not opened |
| Allowed direction | Target → redirector → backend | Conceptual only |
| Public route | None permitted | Required control |
| Logging | Redirector, backend, packet, host, and firewall telemetry | Required before test |
| Stop condition | One harmless authorized check-in or synthetic request | Required before test |

## 8. Findings and Observations

### W5-O03: Redirector Deployment Deferred Because Infrastructure Preconditions Are Not Met

- Classification: No-go readiness observation
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - No redirector VM is confirmed.
  - No backend C2 VM is confirmed.
  - No target VM is confirmed.
  - No isolated C2 network, approved protocol, forwarding rule, listener, or logging stack is confirmed.
- Impact: Deploying a redirector without containment could expose infrastructure, forward unauthorized traffic, or create uncontrolled artifacts.
- Limitation: No redirector configuration, traffic forwarding, or detection capability was evaluated.
- Recommendation: Provision a lab-only redirector, backend C2 VM, target VM, network isolation, logging, firewall rules, stop condition, cleanup plan, and written authorization before hands-on work.

## 9. Rejected Redirector Designs

| Rejected Design | Reason |
|---|---|
| Public VPS redirector | Public infrastructure is excluded |
| Cloud load balancer | Cloud environment is not authorized |
| Home-router port forward | Not isolated and could expose the home LAN |
| Redirector bound to every interface | Could expose a service outside the lab |
| Domain-fronted redirector | Prohibited and unnecessary for a defensive lab |
| CDN-fronted redirector | Uses public infrastructure and third-party services |
| Redirector without logs | Removes defensive learning, correlation, and accountability |
| Redirector to an unconfirmed backend | Backend is not confirmed or authorized |
| Redirector with a real callback payload | Payload creation and callback testing are prohibited |

## 10. Defensive Detection Questions

1. Which process would listen on the redirector?
2. What documented rule would forward traffic, and who approved it?
3. Which named source is permitted, and are non-lab sources denied?
4. Would flow records prove whether traffic reached the backend?
5. Do redirector and backend records correlate in time, source, destination, and volume?
6. Are request paths, timing, and sizes consistent with the named lab exercise?
7. Is there any evidence of a route beyond the isolated lab?
8. Was the forwarding rule removed and the port closed after the test?

## 11. Defensive Artifacts

| Hypothetical Future Action | Expected Artifact | Day 3 Status |
|---|---|---|
| Start web server or proxy | Process-creation event and open-port state | Not observed |
| Configure forwarding | Configuration or firewall-rule change | Not observed |
| Receive authorized request | Access record and packet capture | Not observed |
| Forward to backend | Flow record and backend record | Not observed |
| Deny non-lab source | Firewall or proxy denial record | Not observed |
| Remove forwarding | Configuration difference, process stop/restart, or firewall change | Not observed |
| Restore snapshot | Hypervisor event | Not observed |

## 12. Cleanup and Recovery

No cleanup was required because no redirector, rule, listener, port, process, configuration, or callback artifact was created.

Future authorized cleanup must verify that the forwarding rule is removed, listener port closed, process stopped, temporary configuration removed, logs preserved, snapshots restored when needed, and no public route was exposed. Logs and shell history must not be cleared.

## 13. Evidence Log

| Date/Time | Location | Action | Purpose | Result | State Changed? | Cleanup |
|---|---|---|---|---|---|---|
| 2026-07-25 12:08 PM EDT | Week 5 Day 1–2 plans | Readiness review | Check redirector prerequisites | Redirector, backend, target, network, and logging remain unconfirmed | No | None |
| 2026-07-25 12:39 PM EDT | Day 3 plan | Architecture review | Define a non-operational separation model | Placeholder-only diagram and route boundaries recorded | No | None |
| 2026-07-25 1:14 PM EDT | Day 3 plan | Defensive-analysis review | Identify visibility and correlation requirements | Detection questions and expected artifacts documented | No | None |
| 2026-07-25 1:48 PM EDT | Day 3 plan | Rejected-design review | Exclude unsafe routing choices | Public, all-interface, payload, and unconfirmed-backend designs rejected | No | None |
| 2026-07-25 2:31 PM EDT | Day 3 plan | Cleanup review | Define future recovery requirements | No current artifacts; future teardown checks recorded | No | None |

## 14. Knowledge Check

1. A redirector is an intermediate system that would receive traffic and forward it to a backend service.
2. Separating a redirector from backend C2 can support containment, access restriction, logging, and defender visibility in an isolated lab.
3. Public VPS infrastructure is rejected because it extends the exercise beyond the authorized isolated lab.
4. A home-router port forward is unsafe because it can expose a home network and is not a confirmed lab boundary.
5. Forwarding requires confirmed isolated hosts, lab-only interfaces, authorized protocol, named source/destination/port, logging, firewall restrictions, stop condition, cleanup plan, and written approval.
6. Source and destination must be specified so the route is constrained, auditable, and cannot forward unknown traffic.
7. A process-creation event and open-port state can show that a redirector process exists.
8. Flow records, access records, and backend records can show that forwarding occurred.
9. Logs are required so defenders can correlate traffic, validate containment, and learn from the exercise.
10. Domain fronting is prohibited because it is not needed for this defensive planning lab and can involve unauthorized third-party infrastructure.
11. A redirector without a confirmed backend is invalid because there is no authorized destination or containment model.
12. A redirector to an unconfirmed target is rejected because source authorization and isolation cannot be verified.
13. Future cleanup must verify rule removal, closed ports, stopped processes, removed temporary configuration, preserved logs, snapshot recovery when needed, and no public exposure.
14. A public route must never be exposed because it defeats the isolated-lab safety boundary.
15. The safe Day 3 result when infrastructure is missing is a non-operational no-go architecture plan with defensive analysis only.
