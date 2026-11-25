# Mission 3 — Understand the operating system

## 1. Task / objective
Explore the operating system environment, inspect running processes, available storage, absolute vs. relative paths, and file permissions, and summarize the six core responsibilities of an operating system in my own words.

## 2. Work completed

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| Operating system / system details (`uname -sm`, `sw_vers`) | Identifies the OS kernel, CPU architecture, OS product name, and build version. | `Darwin arm64`; `macOS` version `27.2.1` (Build `26B131`). |
| Current account identity (`whoami`) | Shows which user account owns the active Terminal session and determines default file permissions. | `[redacted]` (standard non-administrator user account used for the session). |
| Available and used storage (`df -h .`) | Reports filesystem capacity, used space, free space, and mount point for the drive holding the current folder. | Total `926Gi`, Used `116Gi`, Available `782Gi` (`13%` capacity) mounted on `/System/Volumes/Data`. |
| System activity snapshot (`ps -eo pid,comm \| head -n 12`) | Lists active processes currently scheduled by the kernel along with their process IDs and executable paths. | Observed core system processes starting at `PID 1` (`/sbin/launchd`), `logd` (`PID 531`), `fseventsd` (`PID 536`), and `configd` (`PID 545`). |

### Task 3.2 — Understand processes
- **What is a process?** A process is an active instance of a program currently loaded into memory and being executed/scheduled by the operating system (along with its open files, state, and allocated resources).
- **What does the PID column represent?** `PID` stands for **Process Identifier**—a unique positive integer assigned by the OS kernel to each running process so the OS and user tools can track, inspect, or signal a specific instance (for example, `PID 1` is `/sbin/launchd`, the first system daemon started on macOS).
- **Two examples of processes running on my computer:**
  1. `/sbin/launchd` (`PID 1`) — macOS's foundational service manager that starts and oversees background system daemons.
  2. `/usr/libexec/configd` (`PID 545`) or an interactive shell/editor like `zsh` — background configuration service or user-facing application running in memory.

### Task 3.3 — Understand paths and permissions
- **Absolute path vs. relative path:**
  - An **absolute path** always starts from the filesystem root `/` and uniquely identifies a location regardless of where your Terminal currently is. Example from this assignment: `/Users/[redacted]/.gemini/antigravity/scratch/digital-detective-8509/terminal-practice`
  - A **relative path** starts from your current working directory (`pwd`) and changes meaning depending on where you are located. Example from this assignment: when inside `digital-detective-8509`, moving into the subfolder uses `cd terminal-practice`, and returning to the repo root uses `cd ..`.
- **Inspecting file permissions (`ls -l terminal-practice/notes.txt`):**
  - Observed output: `-rw-r--r--@ 1 [redacted]  staff  85 Nov 25 21:38 terminal-practice/notes.txt`
  - The leading `-` indicates a regular file (whereas `d` indicates a directory).
  - The next three characters (`rw-`) show the **owner's permissions**:
    - `r` (Read): **Yes** — the owner can open and read the file's contents.
    - `w` (Write): **Yes** — the owner can modify or overwrite the file's contents.
    - `-` (Execute): **No** — execute permission is not set, because `notes.txt` is a plain text file rather than a runnable script or binary.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| `r` — Read | Allows a file's contents to be viewed (or directory contents to be listed). | Reading `terminal-practice/notes.txt` with `cat`. |
| `w` — Write | Allows a file's contents to be changed (or files inside a directory to be added/removed). | Appending a line to `notes.txt`. |
| `x` — Execute | Allows a file to be run as a program; on a directory, allows entering/traversing it. | Navigating into `terminal-practice/` with `cd`. |

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| Process management | Creates, schedules, switches between, and terminates running programs so multiple tasks share the CPU fairly. | Running `zsh`, a browser, and background daemons like `launchd` concurrently. |
| Memory management | Allocates RAM to active processes, keeps each program's memory isolated, and frees memory when programs close. | Giving a Python script its own memory space without letting it overwrite the text editor's data. |
| Device management | Uses drivers to coordinate communication between software and physical hardware devices. | Translating keyboard keystrokes and SSD read/write requests into hardware operations. |
| File management | Organizes data on storage drives into hierarchical folders and files with names, metadata, and paths. | Storing `notes.txt` inside `terminal-practice/` and reading it back by path. |
| User interface / shell | Provides a graphical desktop or command-line shell so users can launch programs and issue instructions. | Typing `ls -l` or `df -h` inside macOS Terminal (`zsh`). |
| Security and permissions | Verifies user identities and enforces read/write/execute rules so unauthorized users or apps cannot access protected files. | Restricting `notes.txt` to `-rw-r--r--` so only the file owner can edit it. |

## 3. Commands / tools used
- `uname -sm`, `sw_vers` — Displays OS kernel, CPU architecture, and macOS version/build.
- `whoami` — Prints the active user account name (redacted in notes).
- `df -h .` — Shows disk capacity, used space, and available space in human-readable units.
- `ps -eo pid,comm | head -n 12` — Displays a snapshot of active processes and their PIDs.
- `cd`, `pwd` — Switches between the repo folder and `terminal-practice/` to observe path changes.
- `ls -l` — Inspects file ownership and `rwx` permission bits.

## 4. My understanding
The operating system acts as the coordinator between raw hardware and user programs. By assigning PIDs to processes, isolating RAM, organizing files into paths, and checking `rwx` permission bits on every access, the OS keeps multiple applications running safely at the same time without stepping on each other or exposing protected data.

## 5. Difficulties faced
When checking the process list inside a restricted shell environment, `ps` was initially blocked with `operation not permitted`, and `whoami` / `ls -l` output contained my local username.

## 6. How I resolved them
I ran the read-only `ps -eo pid,comm` inspection in a permitted Terminal session to capture real system process IDs, and replaced my local username with `[redacted]` across all saved outputs and notes.

## 7. Evidence / files
- Redacted OS inspection log: `../evidence/mission-03-os-output.txt`
- Inspected practice file: `../terminal-practice/notes.txt`

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Status:** Committed and pushed to `origin/main` on GitHub.
