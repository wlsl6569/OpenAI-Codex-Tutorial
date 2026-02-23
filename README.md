# OpenAI-Codex-Tutorial
let's learn the basics of Codex
---

## DAY 1

1. Open the repository on GitHub.
2. Open Codex (OpenAI) and ask for a simple code change.
3. Apply the change in Codex/GitHub.

4. How branches are split (easy explanation):
- Think of each Codex task/conversation as working on a separate change line (branch).
- `main` branch: original/stable project line.
- `codex/...` or `feature/...` branch: temporary work line created for that specific change.
- After the change is ready, you merge that branch back into `main` through a PR.

5. Update your Codex/change branch first, then create PR:
- On that Codex/change branch page, click `Update branch` first (if shown).
- Why: this syncs your branch with the latest `main`, so merge conflicts are less likely.
- Then click `Compare & pull request` (or `Create pull request`).

6. What is PR (Pull Request)?
- PR = a merge request asking to move your branch changes into `main`.
- In PR, you explain what changed and ask for review/approval before merge.
- Check: base = `main`, compare = your Codex/change branch.
- Write title/description, then click `Create pull request`.

7. Merge on GitHub:
- Click `Merge pull request`.
- Click `Confirm merge`.
- (Optional) click `Delete branch`.

8. Button meanings on GitHub:
- `Commit changes`: save edits to the selected branch.
- `Update branch`: sync your branch with latest `main` before merge.
- `Create pull request`: request merge of your branch into `main`.
