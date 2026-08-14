HISTORY REWRITE NOTICE

Date: 2026-08-14

Summary:
- The repository history on `main` was rewritten to correct recent commit author/committer information.
- The four Week 6 commits (Day 4–Day 7 files) were updated to use "Cody R Johnson <cody-r-johnson@users.noreply.github.com>" as the author and committer.
- The rewritten history was force-pushed to `origin/main` with `--force-with-lease`.

If you have cloned or fetched this repository before this notice, please follow one of these options to synchronize safely:

1) If you have no local changes on `main` and want to update to the rewritten history:

```bash
# fetch remote updates
git fetch origin
# reset your local main to match remote
git checkout main
git reset --hard origin/main
```

2) If you have local commits on `main` that you wish to preserve, create a branch to keep them before resetting:

```bash
# create a branch storing your local work
git checkout -b my-local-main-backup
# then update local main to match remote
git checkout main
git fetch origin
git reset --hard origin/main
# reapply your work as needed from 'my-local-main-backup'
```

3) If you collaborate via pull requests or forks, ensure your feature branches are rebased onto the updated `main`:

```bash
git fetch origin
git checkout my-feature-branch
git rebase origin/main
# resolve conflicts and force-push your branch if needed
git push --force-with-lease origin my-feature-branch
```

Why this matters:
- Because history was rewritten, commit SHAs changed for the affected commits. Anyone who pulled the old commits may see divergence and must re-sync to avoid merge conflicts.

Questions / help:
- If you want, I can open an issue or draft a message to the team (requires permission to use your GitHub account or an API token). Alternatively, paste the commands above into your team chat or email.

Thank you — Cody
