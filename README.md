# OpenAI-Codex-Tutorial
let's learn the basics of Codex
---

## DAY 1

1. Open Visual Studio Code and the terminal.
2. In the terminal, navigate to the location where you want to clone the repository (in this tutorial, we use `C:\`).
3. Clone the example repository:
```bash
git clone https://github.com/wlsl6569/OpenAI-Codex-Tutorial.git
```
4. Navigate into the project folder and verify that the files were cloned correctly:
```bash
cd OpenAI-Codex-Tutorial  # go into the project folder
dir                      # check that all files are included
git status               # verify the branch and working tree status
```

5. Ask Web Codex (OpenAI) for a simple code example.

6. Create and update your own branch before editing code:
```bash
git checkout -b feature/day1-practice   # create + switch to new branch
git branch                              # check current branch list
git status                              # verify branch and changed files
```

7. How branches are split (easy explanation):
- `main` branch: stable/original line of the project.
- `feature/...` branch: your personal work line for new changes.
- You work in `feature/...`, then request merge to `main` with PR.

8. After Codex generated code, commit your changes locally:
```bash
git add .
git commit -m "Add day1 practice code"
```

9. Push your branch to GitHub:
```bash
git push -u origin feature/day1-practice
```

10. Create PR (Pull Request) on GitHub:
- Open your repository page on GitHub.
- Click `Compare & pull request`.
- Confirm: base = `main`, compare = `feature/day1-practice`.
- Write title/description, then click `Create pull request`.

11. Merge on GitHub after review/checks:
- Click `Merge pull request`.
- Click `Confirm merge`.
- (Optional) click `Delete branch`.

12. Update your local `main` after merge:
```bash
git checkout main
git pull origin main
```
