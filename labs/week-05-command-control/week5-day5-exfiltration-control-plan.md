# ACME Week 5 Day 5 Data Staging and Exfiltration Control Plan

## 1. Scope and Safety

This plan was prepared for the July 27, 2026 lab window, between 3:00 PM and 6:00 PM EDT.

Day 5 is policy, safeguards, and simulation only. **No data was collected, staged, compressed, encoded, encrypted, uploaded, transferred, or exfiltrated.** No files were read for collection, no private directories were searched, and no local ACME data, database, cookie jar, credential, token, key, or session material was accessed or moved.

No public endpoint, cloud storage, drop site, listener, DNS channel, HTTP upload, email, clipboard, screenshot, tunnel, proxy, or callback was created or used.

## 2. Exfiltration Concept Overview

| Concept | Meaning | Day 5 Status |
|---|---|---|
| Data discovery | Finding data of interest | Not performed |
| Data staging | Preparing data before movement | Simulated only |
| Compression | Reducing data size | Not performed |
| Encoding/encryption | Transforming data before transfer | Not performed |
| Exfiltration | Moving data out of a system | Not performed |
| Exfiltration channel | Protocol or path used for movement | Not configured |
| Drop site | Destination for received data | Not created |
| Data loss prevention | Control that detects or blocks movement | Discussed only |

Data staging is the preparation of information before a potential transfer. Exfiltration is movement of data from a system to another destination. Neither occurred in this exercise.

## 3. Approved Data Policy

| Rule | Requirement |
|---|---|
| Data source | Synthetic placeholders only unless a separate written authorization says otherwise |
| File creation | Placeholder names only; no real file is created for this Day 5 exercise |
| Content | No real data, personal data, secrets, tokens, keys, credentials, sessions, screenshots, or application records |
| Transfer | None today |
| Destination | None today |
| Logs | Preserve all applicable telemetry and evidence |
| Evidence | Sanitized metadata only |
| Cleanup | Remove only authorized future test artifacts |
| Secrets | Never included in a simulated data set |
| Scope | Do not read private directories or actual local application data |

## 4. Simulated Exfiltration Scenario

**This scenario is fictional. No file exists and no transfer occurs.**

A fictional analyst models how 12 synthetic records totaling 4,096 bytes could appear if staged for an authorized transfer between future isolated training systems. The synthetic label and dummy filename below are planning placeholders, not real data and not a transfer plan.

## 5. Simulated Staging Table

| Stage | Simulated Item | Defensive Observation |
|---|---|---|
| Identify | `ACME-SIMULATED-DATASET-A` | A data-classification event would matter |
| Stage | `dummy-customer-list.csv` | A future file-creation event would be observable |
| Prepare | 4,096 fictional bytes | Any compression or encoding would change process/file metadata |
| Transfer | `LAB-WS01` → `LAB-C2` | A future network flow would be observable |
| Receive | Fictional `LAB-C2` storage | A future server-side record would exist |
| Cleanup | Remove fictional staged item | A future file-deletion event would exist |

The table is a defensive model only. It does not create a file, process, network flow, server record, or cleanup artifact.

## 6. Current Readiness

| Component | Status | Proceed? | Notes |
|---|---|---|---|
| Isolated target VM | Not confirmed | No | No documented isolated source host or snapshot |
| C2 server or receiver | Not confirmed | No | No authorized destination or snapshot |
| Listener or drop site | Not created | No | No receiving endpoint exists |
| Exfiltration channel | Not configured | No | No approved protocol or route |
| Allowed moving dataset | Not authorized | No | No synthetic file set is approved for a live transfer |
| Defensive logging stack | Not confirmed | No | No DLP, proxy, firewall, packet, host, or server plan |
| Public or cloud destination | Excluded | No | Public infrastructure is outside scope |

Decision: **no-go for live data staging or exfiltration.**

## 7. Findings and Observations

### W5-O05: Live Exfiltration Deferred Because Data-Movement Preconditions Are Not Met

- Classification: No-go readiness observation
- Severity: Not applicable
- Confidence: Confirmed
- Evidence:
  - No isolated target VM, C2 server, listener, drop site, or exfiltration channel is confirmed.
  - No allowed dataset is authorized for movement.
  - No DLP, proxy, firewall, packet, host, or server logging plan is confirmed.
  - Days 1–4 deferred C2 deployment, listeners, redirectors, and live beaconing.
- Impact: Moving data without these controls could expose real files, secrets, or unauthorized network traffic.
- Limitation: No exfiltration capability or DLP detection was evaluated.
- Recommendation: Use only synthetic datasets in a confirmed isolated lab with written authorization, logging, stop conditions, cleanup, and no external destination before any hands-on exercise.

## 8. Rejected Exfiltration Designs

| Rejected Design | Reason |
|---|---|
| Upload to public cloud storage | Public/cloud infrastructure is excluded |
| Email attachment test | Sends data outside the lab |
| DNS tunneling | Not authorized and commonly abuse-prone |
| HTTP upload to listener | No listener or target is confirmed |
| Compress local ACME database | Actual local data movement is prohibited |
| Screenshot collection | Can capture potentially sensitive visual data |
| Clipboard transfer | Can leak unintended content |
| Cookie/session export | Session material is prohibited |
| Credential-file staging | Secret material is prohibited |

## 9. Defensive Control Mapping

| Control | What It Watches |
|---|---|
| DLP | Sensitive-content patterns and policy violations |
| EDR | File collection, archive/compression tools, and unusual process trees |
| Proxy | Upload-like web requests and unusual destinations |
| DNS logging | Large or patterned DNS queries |
| Firewall | Egress volume and unusual protocols |
| CASB | Cloud-storage upload behavior |
| Email gateway | Attachment or outbound-message paths |
| File integrity monitoring | New archives and staged directories |
| SIEM | Correlated file, process, identity, and network events |

No bypasses or control tests were attempted.

## 10. Defensive Artifacts

| Hypothetical Future Action | Expected Artifact | Day 5 Status |
|---|---|---|
| Data access | File-access event | Not observed |
| Archive creation | File-creation and process event | Not observed |
| Encoding or compression | Process and file-metadata changes | Not observed |
| Upload attempt | Proxy, firewall, server, and network records | Not observed |
| DNS-tunneling attempt | Resolver records and query-pattern alert | Not observed |
| DLP block | DLP alert and policy record | Not observed |
| Cleanup | File-deletion and timeline event | Not observed |

## 11. Cleanup and Recovery

No cleanup was required because no data, placeholder file, staged directory, archive, channel, drop site, listener, or transfer artifact was created.

Future authorized cleanup must verify that no real data is retained; synthetic staged files are removed; the drop site is emptied or removed; the listener is closed; the transfer channel is disabled; logs are preserved; snapshots are restored when needed; and no external destination was contacted. Logs and shell history must not be cleared.

## 12. Evidence Log

| Date/Time | Location | Action | Purpose | Result | State Changed? | Cleanup |
|---|---|---|---|---|---|---|
| 2026-07-27 3:09 PM EDT | Week 5 Days 1–4 plans | Readiness review | Confirm whether any data movement is allowed | Target, receiver, channel, data authorization, and logging remain unconfirmed | No | None |
| 2026-07-27 3:42 PM EDT | Day 5 plan | Placeholder-data policy review | Define a no-real-data boundary | Synthetic-only policy recorded | No | None |
| 2026-07-27 4:18 PM EDT | Day 5 plan | Simulated scenario design | Model defensive visibility without files or transfer | Fictional staging table recorded | No | None |
| 2026-07-27 4:57 PM EDT | Day 5 plan | Control and rejected-design review | Identify detection points and exclude unsafe routes | No live channel, data, or test created | No | None |
| 2026-07-27 5:36 PM EDT | Day 5 plan | Cleanup review | Define future recovery requirements | No current artifacts; future cleanup requirements recorded | No | None |

## 13. Knowledge Check

1. **What is data staging?** Preparing information before a possible transfer.
2. **What is exfiltration?** Moving data from a system to another destination.
3. **Why is Day 5 simulated only?** No isolated source, receiver, channel, dataset authorization, or logging plan exists.
4. **Why should real files not be moved today?** They may contain private, sensitive, or out-of-scope material.
5. **Why is synthetic data preferred for exfiltration simulation?** It permits defensive modeling without exposing real information.
6. **Why are public cloud uploads rejected?** Public infrastructure is outside the isolated lab boundary.
7. **Why is DNS tunneling rejected today?** It is not authorized and needs a specifically approved isolated DNS lab.
8. **Why is compressing the ACME database prohibited?** It would move or transform actual local application data.
9. **What defensive artifacts would archive creation produce?** File-creation, process, command-line, file-metadata, and integrity-monitoring artifacts.
10. **What controls can detect exfiltration?** DLP, EDR, proxy, DNS, firewall, CASB, email gateway, file-integrity monitoring, and SIEM controls.
11. **Why should secrets never be included in simulated datasets?** They expand access risk and can be inadvertently retained or transferred.
12. **Why should DLP testing require written authorization?** Policy testing can affect sensitive content, workflows, and security controls.
13. **What must cleanup verify after future exfil testing?** No real data remains; synthetic artifacts are removed; receiver/channel/listener are disabled; logs are preserved; snapshots restored when needed; and no external contact occurred.
14. **Why should logs be preserved?** So defenders can reconstruct the exercise and validate controls.
15. **What is the safe Day 5 result?** A synthetic-only policy and simulated defensive control plan with a documented no-go for live data movement.
