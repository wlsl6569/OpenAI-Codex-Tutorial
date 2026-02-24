# OpenAI-Codex-Tutorial
let's learn the basics of Codex
---

## DAY 1

1. Open Codex (OpenAI) first, then connect/select your target GitHub repository.
   - Important: start by making sure Codex is working on the correct repository before asking for changes.
2. Open that same repository on GitHub and confirm you are in the right repo.
3. Ask Codex for a simple code change.

4. How branches are split (easy explanation):
- Think of each Codex task/conversation as working on a separate change line (branch).
- `main` branch: original/stable project line.
- `codex/...` or `feature/...` branch: temporary work line created for that specific change.
- After the change is ready, you merge that branch back into `main` through a PR.

5. From here, Steps 6-8 are the real "apply your change" flow on GitHub.

6. Update your Codex/change branch first, then create PR:
- On that Codex/change branch page, click `Update branch` first (if shown).
- Why: this syncs your branch with the latest `main`, so merge conflicts are less likely.
- Then click `Compare & pull request` (or `Create pull request`).

7. What is PR (Pull Request)?
- PR = a merge request asking to move your branch changes into `main`.
- In PR, you explain what changed and ask for review/approval before merge.
- Check: base = `main`, compare = your Codex/change branch.
- Write title/description, then click `Create pull request`.

8. Merge on GitHub:
- Click `Merge pull request`.
- Click `Confirm merge`.
- (Optional) click `Delete branch`.

9. Button meanings on GitHub:
- `Commit changes`: save edits to the selected branch.
- `Update branch`: sync your branch with latest `main` before merge.
- `Create pull request`: request merge of your branch into `main`.

## DAY 2

Today's goal:
- Clone the project to your local computer.
- Use terminal + Git commands to review files/changes received from Codex.
- Run the project locally.

1. Clone the repository to your local machine
- Open terminal and move to your target folder:
  - `cd path/to/your/folder`
- Clone the GitHub repository:
  - `git clone https://github.com/<username>/<repo>.git`
- Move into the project directory:
  - `cd <repo>`

2. Check current repository state (branch + changes)
- Check current branch:
  - `git branch`
- Check all branches (including remote):
  - `git branch -a`
- Check changed files/status:
  - `git status`

3. Review changes from Codex
- Check recent commits:
  - `git log --oneline --decorate --graph -n 10`
- See which files were changed in a commit:
  - `git show --name-only <commit-hash>`
- Review code diff:
  - `git show <commit-hash>`
  - Or compare uncommitted local changes with: `git diff`

4. Sync with remote updates
- Fetch latest remote metadata:
  - `git fetch`
- Pull latest changes into your working branch:
  - `git pull origin <branch-name>`

5. Run the project (follow repository-specific instructions)
- Install dependencies:
  - Example: `npm install` or `pip install -r requirements.txt`
- Run the app/script:
  - Example: `npm run dev` or `python main.py`

6. Quick checks before/after running
- Before running: use `git status` to confirm no unexpected changes.
- If errors happen: read terminal logs first.
- If run succeeds: confirm behavior in terminal/browser output.

7. Key takeaway
- Flow: clone → check branch/status → inspect commit/diff → sync with pull → run.
- Use Git commands to understand "what changed" before you execute.
