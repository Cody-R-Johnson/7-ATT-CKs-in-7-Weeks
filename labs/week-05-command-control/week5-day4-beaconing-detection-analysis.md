# ACME Week 5 Day 4 Beaconing and Detection Logic

## 1. Scope and Safety

This analysis was prepared for the July 26, 2026 lab window, between 1:00 PM and 4:00 PM EDT.

Day 4 is simulated timing analysis only. No agent, implant, listener, C2 framework, payload, callback, packet, tunnel, proxy, reverse shell, or port forward was run or created. The local ACME training application and approved repository artifacts are the only confirmed scope.

No public, LAN, cloud, personal, school, employer, production, unknown, or non-lab system was contacted. The objective is to model what defenders could observe, not to tune traffic for stealth or evade controls.

## 2. Beaconing Concept

Beaconing is repeated check-in behavior from a system to a control endpoint. Conceptually:

```text
[Hypothetical target agent] → periodic check-in → [Hypothetical listener/C2]
```

For Day 4, this is only a defensive model: no agent, listener, callback, packet, or C2 traffic exists.

## 3. Current Readiness

| Component | Status | Proceed? | Notes |
|---|---|---|---|
| Target VM or agent | Not confirmed / not created | No | No isolated target or authorized agent exists |
| Listener or C2 server | Not deployed | No | Days 1–3 retained a no-go deployment decision |
| Isolated C2 network | Not confirmed | No | No route/interface containment evidence |
| Allowed protocol | Not authorized | No | No protocol-specific scope exists |
| Logging stack | Not confirmed | No | No approved network, host, listener, or proxy collection plan |
| Live beacon traffic | Not generated | No | This report uses fictional timing data only |

Decision: **no-go for live beacon testing.**

## 4. Simulated Beacon Dataset

**This table is simulated. No traffic was generated.** The host labels, endpoint labels, path, times, and byte counts are fictional training data used only to discuss defender observations.

| Time | Source | Destination | Path | Bytes Out | Bytes In | Note |
|---|---|---|---|---:|---:|---|
| 10:00 | `LAB-WS01` | `LAB-C2` | `/checkin` | 420 | 180 | Simulated check-in |
| 10:05 | `LAB-WS01` | `LAB-C2` | `/checkin` | 418 | 181 | Simulated check-in |
| 10:10 | `LAB-WS01` | `LAB-C2` | `/checkin` | 421 | 179 | Simulated check-in |
| 10:15 | `LAB-WS01` | `LAB-C2` | `/checkin` | 419 | 182 | Simulated check-in |
| 10:20 | `LAB-WS01` | `LAB-C2` | `/task` | 610 | 980 | Simulated activity change |

## 5. Detection Logic

For each source-to-destination pair, defenders can:

1. Group observed events by an appropriate time window.
2. Calculate time deltas between events and flag unusually regular timing for review.
3. Check whether the destination is rare or unapproved for the source host.
4. Compare repeated paths, headers, methods, and byte counts with known application baselines.
5. Identify bursts or size changes that follow otherwise regular activity.
6. Correlate the network pattern with endpoint process, user, file, authentication, and DNS evidence.
7. Determine whether the traffic used expected proxy and egress-control paths.
8. Treat the result as an alert candidate, then investigate false positives before declaring compromise.

This is defender-focused analytic logic, not a procedure for creating or concealing beacon traffic.

## 6. Detection Features

| Feature | Why It Helps |
|---|---|
| Low variance in time deltas | Can indicate regular automated behavior |
| Repeated rare destination | May identify an abnormal control endpoint |
| Same path repeatedly | Can reveal recurring check-in behavior |
| Small consistent byte counts | May indicate heartbeat-like traffic |
| Burst after an idle period | May indicate a change requiring further investigation |
| Unusual process owner | Supports endpoint triage and process attribution |
| Off-hours periodicity | Can identify baseline deviation |
| Direct egress that bypasses proxy | Can reveal policy or routing gaps |
| DNS-query regularity | Can identify a pattern needing resolver and endpoint review |

## 7. False Positive Considerations

A beacon-like pattern is an alert candidate, not proof of compromise. Legitimate software can create repeated traffic.

| Benign Source | Similar Pattern | Triage Consideration |
|---|---|---|
| Software updater | Periodic update checks | Confirm publisher, process path, destination, and change window |
| EDR agent | Regular telemetry | Verify approved endpoint-security tooling and policy |
| Backup client | Scheduled transfers | Compare with backup schedule and expected volume |
| Monitoring agent | Heartbeats | Confirm monitored service and management destination |
| Chat or collaboration application | Frequent keepalives | Validate user/application context and known domains |
| Browser tab | Repeated polling | Check browser process, tab behavior, and destination reputation |
| Cloud-sync client | Periodic synchronization | Confirm user activity and approved tenant/service |
| NTP or DNS client | Regular protocol traffic | Verify expected resolver/time-service configuration |

## 8. Defender Triage Questions

| Question | Purpose |
|---|---|
| What process made the connection? | Identify the source binary and process tree |
| Is the destination known and approved? | Perform allowlist, ownership, and reputation checks |
| Is timing expected for this application? | Compare with normal host and application behavior |
| Are byte counts consistent or bursty? | Assess heartbeat-like behavior and activity changes |
| Does the path repeat across hosts? | Look for shared configuration or campaign indicators |
| Is traffic direct or proxied? | Check egress-control compliance |
| Is the user context expected? | Correlate account, session, and process evidence |
| Are related file or process events present? | Expand endpoint timeline context |
| Did behavior begin after a new file appeared? | Link network activity to execution or installation events |

## 9. Findings and Observations

### W5-O04: Live Beacon Testing Deferred Because C2 Lab Preconditions Are Not Met

- Classification: No-go readiness observation
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - No agent or target VM is confirmed.
  - No listener or C2 server is deployed.
  - No isolated C2 network, logging stack, or protocol authorization exists.
  - Days 1–3 also deferred deployment, listener, and redirector work.
- Impact: Generating live beacon traffic without containment could create unauthorized callbacks or misleading telemetry.
- Limitation: No real network detection capability or C2 traffic was evaluated.
- Recommendation: Keep Day 4 simulated until an isolated C2 lab, approved tool/protocol, logging stack, stop condition, cleanup plan, and written authorization are confirmed.

## 10. Rejected Actions

| Rejected Action | Reason |
|---|---|
| Run an agent | No isolated target VM or authorization |
| Start a listener | Listener deployment remains no-go |
| Generate synthetic callbacks | Could create unauthorized traffic or artifacts |
| Use a public endpoint | Public infrastructure is excluded |
| Tune jitter for stealth | Evasion optimization is prohibited |
| Use a DNS beacon | No DNS lab stack or authorization |
| Send test packets | No confirmed listener or isolated lab route |
| Capture production traffic | Outside course scope |

## 11. Defensive Artifacts

| Hypothetical Future Action | Expected Artifact | Day 4 Status |
|---|---|---|
| Agent starts | Process creation and file artifact | Not observed |
| Beacon connects | Network flow and listener record | Not observed |
| Web-style check-in | Proxy or web-style records | Not observed |
| DNS-style check-in | DNS resolver records | Not observed |
| Activity burst | Larger or irregular flow and server record | Not observed |
| Agent stop | Process-termination event | Not observed |
| Cleanup | File-deletion and snapshot-restore records | Not observed |

## 12. Cleanup and Recovery

No cleanup was required because Day 4 generated no traffic and created no agent, listener, payload, process, or temporary artifact.

Future authorized live testing must confirm the agent is stopped, listener is closed, periodic traffic has ceased, temporary files are removed, logs are preserved, snapshots are restored when appropriate, and no public or non-lab destination was contacted. Logs and shell history must not be cleared.

## 13. Evidence Log

| Date/Time | Location | Action | Purpose | Result | State Changed? | Cleanup |
|---|---|---|---|---|---|---|
| 2026-07-26 1:09 PM EDT | Week 5 Days 1–3 plans | Readiness review | Confirm whether live beacon testing is allowed | Agent, listener, C2 server, isolated network, and logging remain unconfirmed | No | None |
| 2026-07-26 1:42 PM EDT | Day 4 analysis | Simulated dataset design | Model defender-visible timing without network activity | Clearly fictional data set recorded | No | None |
| 2026-07-26 2:18 PM EDT | Day 4 analysis | Detection and false-positive analysis | Define alert logic and triage safeguards | Detection features and benign alternatives documented | No | None |
| 2026-07-26 2:56 PM EDT | Day 4 analysis | No-go and rejected-action review | Prevent live traffic generation | No callbacks, packets, listeners, or agents created | No | None |
| 2026-07-26 3:34 PM EDT | Day 4 analysis | Cleanup review | Define future recovery controls | No current artifacts; future cleanup verification documented | No | None |

## 14. Knowledge Check

1. Beaconing is repeated check-in behavior from a system to a control endpoint.
2. Day 4 is simulated only because no isolated target, listener, C2 server, network, protocol authorization, or logging plan is confirmed.
3. An interval is the time between check-ins.
4. Jitter is variation around an expected interval.
5. Jitter must not be optimized today because the objective is defensive detection analysis, not stealth or evasion.
6. Periodic timing, repeated destinations/paths, consistent sizes, process context, and baseline deviation can make traffic detectable.
7. Destination rarity is useful because unusual destinations may not match a host’s expected network behavior.
8. Byte counts help identify consistent heartbeats or activity changes that warrant triage.
9. A burst can indicate a change in activity and should be correlated with host and server evidence.
10. Software updaters are a false-positive consideration because legitimate update checks can be periodic.
11. Process context is important because it identifies which binary and user initiated the connection.
12. Synthetic callbacks must not be generated because there is no confirmed listener, route, or isolated lab authorization.
13. A live beacon could create process, file, network-flow, listener, proxy, DNS, and firewall artifacts.
14. Future cleanup must verify stopped agent, closed listener, no remaining periodic traffic, removed temporary files, preserved logs, restored snapshot when needed, and no non-lab contact.
15. The safe Day 4 result is a simulated dataset and defensive detection analysis with a documented no-go decision.
