# Tooling Notes

The 7-week course names common red-team and assessment tools so you can learn where they fit in an operation. This repository does not install or configure those tools automatically.

## Safe Use Rules

- Point tools only at `127.0.0.1`, a disposable lab VM, or an explicitly authorized environment.
- Prefer passive review and documentation when a tool could generate noisy or destructive traffic.
- Save commands and outputs in the matching weekly `evidence/` folder.
- For dual-use tools such as Metasploit, Mimikatz, Empire, Mythic, and evasion scripts, focus on lab architecture, detection opportunities, and written analysis unless you are in an isolated environment designed for that tool.

## Local ACME Fit

The ACME site is intentionally a lightweight web target. It is enough for web mapping, proxy review, authentication observation, evidence collection, SQL injection comparison, IDOR analysis, stored XSS comparison, and reporting practice. Heavier network, Active Directory, C2, or evasion tools should be studied conceptually here or used only in a separate purpose-built lab.
