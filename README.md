# OpenAI-Codex-Tutorial

A practical beginner tutorial for learning Codex, especially for AI-search and research workflows.

## 7-Day Codex Learning Roadmap

### Day 1 (Foundation): What to do today

**Goal:** Learn the core Codex workflow: request clearly, execute safely, verify results.

#### 1) Set up your working habit (15 min)
- Open your project in terminal.
- Run:
  - `pwd`
  - `rg --files`
  - `git status`
- What these commands mean:
  - `pwd`: shows your current folder path (where terminal is currently pointing).
  - `rg --files`: lists project files quickly so you can understand repo structure.
  - `git status`: shows what changed, what is staged, and whether your branch is clean.
- Terminal/CLI quick clarification:
  - Yes — if you cloned the repository and opened that folder in VS Code, the **VS Code Terminal** is your project terminal.
  - **Terminal** = the app/panel where you type commands.
  - **CLI** (Command Line Interface) = the command-based way of using tools inside that terminal.
  - If `pwd` output ends with your repo folder name (for example `.../OpenAI-Codex-Tutorial`), you are in the correct project folder.
- Understand where files are and whether your working tree is clean.

#### 2) Learn a good Codex prompt structure (15 min)
Use this template for every coding task:
1. **Goal**: what should be built or fixed.
2. **Context**: what file/module is relevant.
3. **Constraints**: style rules, no big refactor, keep behavior.
4. **Validation**: what command proves success.
5. **Output format**: summary + changed files + test output.

Example:
> "Add input validation to `search.py`. Keep existing behavior except invalid input should raise `ValueError`. Do minimal diff. Run tests and show output."

#### 3) Do your first small task (20 min)
Pick one very small task:
- rename a variable for readability,
- add one small helper function,
- improve one error message.

Then do this loop:
1. Ask Codex with the template.
2. Review the diff.
3. Run checks/tests.
4. Commit if correct.

#### 4) Build verification mindset (10 min)
Before accepting changes, always ask:
- Did it change only what I requested?
- Are there side effects?
- Did checks/tests pass?

#### 5) End-of-day note (10 min)
Write a short log:
- 1 prompt that worked well,
- 1 mistake you made,
- 1 thing to improve tomorrow.

### Day 1 Success Criteria
- You used a structured prompt at least once.
- You reviewed a diff before accepting changes.
- You ran at least one validation command.
- You can explain the Codex loop in your own words.

---

### Days 2–7 (Preview)
- **Day 2:** Terminal and repo navigation speed.
- **Day 3:** Git discipline (small commits, clean messages).
- **Day 4:** Testing and debugging workflow.
- **Day 5:** AI-search mini project.
- **Day 6:** Reusable prompt patterns.
- **Day 7:** Capstone + portfolio-ready output.

## Simple Word vs Gibberish Detector

I added a tiny character-level language model example:
- File: `lm_gibberish_detector.py`
- Purpose: classify input text as likely real word (`word`) or gibberish (`gibberish`)

### Run

```bash
python lm_gibberish_detector.py hello qzxptx applle machine
```

### Example output

```text
hello           -> word      (confidence=0.98, score=0.000)
qzxptx          -> gibberish (confidence=0.55, score=-4.022)
applle          -> word      (confidence=0.95, score=-2.877)
machine         -> word      (confidence=0.75, score=-3.510)
```

### Notes
- This is a simple educational model, not production-grade NLP.
- It uses character bigrams + basic heuristics.
- If `/usr/share/dict/words` exists, it automatically uses it as extra training data.
