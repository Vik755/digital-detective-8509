# Mission 6 — Git and GitHub

## 1. Task / objective
Understand the basic Git workflow (`status`, `add`, `commit`, `log`), create and publish a feature branch (`update-about`) updating the root `README.md` with a "My Learning" section, open a Pull Request into `main`, and build a personal Git command glossary.

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| Check repository status (`git status`) | Shows the active branch and lists modified, untracked, and staged files in the working tree. |
| Stage selected changes (`git add <file>`) | Copies the chosen file modifications into the staging area (index) to include them in the next snapshot. |
| Create a commit (`git commit -m "..."`) | Records all currently staged changes as a permanent versioned snapshot in the local repository history with an explanatory message. |
| View commit history (`git log --oneline`) | Lists past commits in reverse chronological order with their short commit hashes and messages. |

**Difference between staging (`git add`) and committing (`git commit`):**
Staging (`git add`) lets you prepare and select *which* specific changes belong in the next update—like packing items into a shipping box before sealing it. Committing (`git commit`) permanently seals that staged box into Git's history with a timestamp and commit message, so unrelated edits left unstaged stay out of that snapshot.

### Task 6.2 — Create and use a branch
1. Created and switched to a new branch named `update-about` (`git checkout -b update-about`).
2. Edited the root `README.md` on `update-about` to add a `## My Learning` section summarizing key takeaways from Missions 1–5.
3. Checked `git status`, staged `README.md`, committed (`"Add My Learning section to root README"`, commit `ba9e317`), and published the branch (`git push -u origin update-about`).

### Task 6.3 — Create a Pull Request
- Opened Pull Request **#1** (`https://github.com/Vik755/digital-detective-8509/pull/1`) from `update-about` into `main` titled `"Add My Learning section to root README"`.
- **Current PR status:** **Open (not merged)** — kept open intentionally per the assignment instruction *"Merge the PR only if your instructor has asked you to complete the merge"*, with branch and Pull Request activity visible on GitHub.
- Switched back to `main` locally (`git checkout main`) to continue documenting Mission 6 without mixing branch changes.
- **What a branch and Pull Request are, and why they matter for teamwork:** A **branch** is an independent line of development branched off from `main` where changes can be built and tested without breaking working code for teammates. A **Pull Request (PR)** is a formal proposal on GitHub to merge changes from one branch into another—it lets collaborators inspect the exact diff, leave review comments, and approve changes safely before updating the shared `main` branch.

### Task 6.4 — Build your Git command glossary

| Git operation | Command | One-line explanation in my own words |
| :--- | :--- | :--- |
| Initialise a repository | `git init` | Turns the current folder into a new Git repository by creating a hidden `.git` history database. |
| Check status | `git status` | Reports which branch you are on and which files are untracked, modified, or staged for commit. |
| Stage changes | `git add <file>` | Marks specific file edits to be included in the upcoming commit snapshot. |
| Commit changes | `git commit -m "<msg>"` | Saves staged changes permanently into the local repository history with a descriptive message. |
| View history | `git log` | Displays past commits, their hashes, authors, dates, and messages. |
| Create or list branches | `git branch [name]` | Lists all local branches, or creates a new branch at the current commit when a name is given. |
| Switch branches | `git checkout <name>` / `git switch <name>` | Moves your working tree and `HEAD` pointer onto another branch. |
| Publish changes | `git push` | Uploads local branch commits to the remote repository on GitHub. |
| Retrieve remote changes | `git pull` | Downloads new commits from the remote repository and merges them into your current local branch. |

## 3. Commands / tools used
- `git status`, `git add`, `git commit`, `git log --oneline` — Core local version-control workflow.
- `git checkout -b update-about`, `git checkout main` — Branch creation and switching.
- `git push -u origin update-about` — Publishes the feature branch to GitHub.
- `gh pr create`, `gh pr list` — Creates and verifies Pull Request #1 on GitHub.

## 4. My understanding
Git separates editing files, choosing what to include (`git add`), saving snapshots (`git commit`), and sharing with GitHub (`git push`). Branching and Pull Requests make collaboration safe: each contributor works on an isolated branch like `update-about`, opens a PR so changes can be reviewed line by line, and only merges into `main` once approved.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- Branch on GitHub: `update-about` (commit `ba9e317`)
- Pull Request on GitHub: [Pull Request #1](https://github.com/Vik755/digital-detective-8509/pull/1) (Status: Open)
- `README.md` (Mission 6 workflow notes and Git command glossary)

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Status:** Committed and pushed to `origin/main` on GitHub.
