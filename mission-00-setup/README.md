# Mission 0 — Create your GitHub workspace

## 1. Task / objective
Create a correctly named local project folder and matching public GitHub repository (`digital-detective-8509`), verify that Python 3 and Git are installed, prepare the full mission folder and file structure, write the initial root `README.md`, and push the initial setup commit before moving on to Mission 1.

## 2. Work completed
- **Repository name:** `digital-detective-8509` (matching the naming rule `digital-detective-` + last 4 digits of USN `8509`).
- **Tools checked and versions:**
  - Python: `Python 3.15.2`
  - Git: `git version 2.56.1`
- **Folders and files created:**
  - `README.md`
  - `mission-00-setup/README.md`
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-05-numbers-data/README.md`
  - `mission-05-numbers-data/number_converter.py`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/.gitkeep`
- Created the public GitHub repository `Vik755/digital-detective-8509` without initializing a duplicate online `README.md`, connected the local repository to `origin`, and pushed the initial commit.

## 3. Commands / tools used
- `python3 --version` — Checks the installed Python 3 version.
- `git --version` — Checks the installed Git version.
- `mkdir -p` / `touch` — Creates the mission folders and placeholder files inside `digital-detective-8509`.
- `git init -b main` — Initializes a new local Git repository with `main` as the default branch.
- `git config user.name` and `git config user.email` — Sets a local commit author name and privacy-safe GitHub noreply email.
- `gh repo create` — Creates the public GitHub repository and links it as the `origin` remote.
- `git add .`, `git commit -m "..."`, `git push -u origin main` — Stages, commits, and publishes the Mission 0 setup to GitHub.

## 4. My understanding
A **repository** is a project folder tracked by Git that stores both the current files and the full history of snapshots (commits) made over time, which can also be synced to a remote host like GitHub. Organising the folder structure by mission (`mission-00-setup/` through `mission-08-final-report/`) keeps each topic isolated, prevents files from mixing together in the root directory, and makes it easy for both me and a reviewer to trace one mission per commit.

## 5. Difficulties faced
Git does not track completely empty directories, so the `evidence/` folder would not appear on GitHub by itself during initial setup. Also, I needed to make sure no personal email address was exposed in the public commit metadata.

## 6. How I resolved them
I placed a placeholder `.gitkeep` file inside `evidence/` so Git tracks the directory on GitHub right away, and configured the repository-local `user.email` to use GitHub's privacy-safe `noreply` address (`Vik755@users.noreply.github.com`).

## 7. Evidence / files
- Root index: `../README.md`
- Placeholder mission files across `mission-01-computer-basics/` through `mission-08-final-report/`
- `../evidence/.gitkeep`

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Status:** Committed locally and pushed to `origin/main` on GitHub (`https://github.com/Vik755/digital-detective-8509`).
