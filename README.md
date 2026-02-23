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
- Commit/Push/PR quick clarification (Korean):
  - `git commit`: 내 컴퓨터(로컬 브랜치)에 변경 저장.
  - `git push`: 로컬 커밋을 원격 저장소(GitHub 등)로 업로드.
  - `PR (Pull Request)`: 내 브랜치 변경을 `main` 같은 기본 브랜치에 합쳐달라는 요청.
  - PR은 자동 반영이 아니고, 리뷰/승인 후 merge 되어야 원본 브랜치에 반영됨.
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


## Codex 코드 작성 후 브랜치/PR/푸시/머지 전체 흐름 (Korean)

아래 순서대로 하면 됩니다.

### 1) 새 브랜치에서 작업 시작
```bash
git checkout -b feature/gibberish-detector
```

### 2) Codex로 코드 작성 후 로컬 커밋
```bash
git add .
git commit -m "Add gibberish detector"
```

### 3) 원격 저장소로 브랜치 푸시
```bash
git push -u origin feature/gibberish-detector
```

### 4) PR 생성
- GitHub에서 `Compare & pull request` 버튼 클릭
- base: `main`, compare: `feature/gibberish-detector` 확인
- 변경 설명 작성 후 PR 생성

### 5) 사이트에서 머지
- 리뷰/체크 통과 후 GitHub PR 페이지에서 `Merge pull request` 클릭
- `Confirm merge` 클릭
- 필요하면 `Delete branch`로 작업 브랜치 정리

### 6) 로컬 main 최신화
```bash
git checkout main
git pull origin main
```

### 빠른 체크 포인트
- 커밋만 하면 로컬에만 저장됨
- 푸시해야 GitHub에 올라감
- PR 머지되어야 `main`에 최종 반영됨
