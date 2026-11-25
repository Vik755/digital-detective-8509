# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use the command-line interface (CLI) to inspect directories, practise creating/copying/moving/appending files safely inside a dedicated practice folder (`terminal-practice/`), understand command flags and pipes, and explore how a package manager (`Homebrew`) works on macOS without installing or removing software.

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| Current-directory display (`pwd`) | Prints the full path of the folder currently open in the shell. | Displayed `/Users/[redacted]/.gemini/antigravity/scratch/digital-detective-8509`. |
| Directory listing (`ls`) | Lists visible files and folders in the current directory. | Listed `README.md`, `evidence`, and all `mission-00` through `mission-08` folders. |
| Detailed listing (`ls -l`) | Shows long-format metadata: permissions, link count, owner, group, byte size, timestamp, and name. | Showed `-rw-r--r--@` for `README.md` (`1928` bytes) and `drwxr-xr-x@` for mission folders. |
| Change directory (`cd ..` / `cd digital-detective-8509`) | Moves the shell working location to another folder (`..` goes to the parent folder). | `cd ..` moved one level up to `scratch/`; `cd digital-detective-8509` returned to the repository root. |
| Create directory (`mkdir`) | Creates a new empty folder at the specified path. | Created `terminal-practice/` inside the repository. |
| Create empty file (`touch`) | Creates an empty file (or updates the timestamp if it already exists). | Created `terminal-practice/sample.txt` with size `0B`. |
| Copy file (`cp`) | Duplicates an existing file to a new path or filename while keeping the original. | Copied `sample.txt` to `sample_copy.txt`; both existed side by side. |
| Move / rename file (`mv`) | Moves a file to another path or renames it in place without leaving a duplicate. | Renamed `sample_copy.txt` to `sample_renamed.txt`; the old name disappeared. |
| Display file contents (`cat`) | Reads and prints the text content of a file directly to Terminal output. | Printed both lines stored in `terminal-practice/notes.txt`. |

### Task 2.2 — Practise file changes safely
Inside `terminal-practice/`:
1. Created `notes.txt` with a first line using `>` (`echo "First line: exploring terminal safely" > terminal-practice/notes.txt`).
2. Appended a second line using `>>` (`echo "Second line: appending preserves existing text" >> terminal-practice/notes.txt`).
3. Displayed `notes.txt` with `cat` and confirmed both lines were present.
4. Made a backup copy (`cp notes.txt notes_backup.txt`) and renamed the backup (`mv notes_backup.txt notes_archive.txt`).

**Questions and answers:**
- **Difference between replacing a file's contents and adding text to the end:** Single redirection (`>`) overwrites the entire file from scratch (erasing prior contents), whereas append redirection (`>>`) keeps all existing contents and adds new text at the end of the file.
- **Difference between copying a file and moving a file:** `cp` creates a second, independent duplicate so both the source and destination exist; `mv` transfers or renames the single file so it exists only at the new name/location.
- **What information `pwd` provides:** It prints the exact absolute path from the root directory `/` down to the current working directory, helping confirm where commands will run before modifying files.
- **Why `ls` is useful:** It lets you verify which files and directories exist in a folder before running commands on them, preventing typos, accidental overwrites, or running scripts from the wrong folder.

### Task 2.3 — Understand flags and pipes
- **Comparing `ls` and `ls -lah`:** Plain `ls` displays only visible file and folder names in columns. Adding `-l` switches to long detailed format (permissions, owner, size, modified date), `-a` reveals hidden dot-entries such as `.` (`current dir`), `..` (`parent dir`), and `.git` (in the repo root), and `-h` converts raw byte counts into human-readable units like `85B` or `192B`.
- **Using a pipe (`ls -la | head -n 5`):** The pipe symbol `|` connects the standard output of the left command directly into the standard input of the right command without creating temporary files. `ls -la` generates the full detailed listing (including hidden files), and `head -n 5` filters that stream so only the first 5 lines (`total 8`, `.`, `..`, `.git`, `README.md`) appear on screen.

### Task 2.4 — Understand package managers
- Checked Homebrew safely in read-only mode:
  - `brew --version` reported `Homebrew 7.0.16`.
  - `brew list --formula` showed `15` installed command-line formulas managed by Homebrew.
- **Why package managers are useful:** A package manager automates finding, downloading, verifying, installing, updating, and removing software tools along with all their required dependencies from trusted repositories. Instead of manually searching websites for installers and tracking version conflicts, one consistent command keeps developer tools organized and up to date.

## 3. Commands / tools used
- `pwd` — Prints current working directory path.
- `ls`, `ls -l`, `ls -lah` — Lists directory contents with optional detailed, hidden, and human-readable flags.
- `cd` — Changes the current working directory.
- `mkdir`, `touch`, `cp`, `mv` — Creates folders/files, duplicates files, and renames/moves files.
- `echo`, `>`, `>>`, `cat` — Writes, appends, and displays file text.
- `|` and `head -n 5` — Pipes command output into a line-limiting filter.
- `brew --version`, `brew list --formula` — Inspects the Homebrew package manager version and installed formulas.

## 4. My understanding
Working in the Terminal gives precise control over files and directories using short composable commands. Flags modify how a single command behaves (for example showing hidden `.git` folders or readable sizes), while pipes (`|`) let small single-purpose tools combine into workflows like listing and slicing top lines. Understanding `>` vs `>>` and `cp` vs `mv` prevents accidental data loss when automating or editing files.

## 5. Difficulties faced
Running `ls -la` inside a personal user path prints the local computer username in the owner column and full path, which cannot be published publicly under the assignment's privacy rules.

## 6. How I resolved them
I kept all file experiments strictly inside `terminal-practice/` within the repository and redacted the local account name with `[redacted]` before saving any command output to `evidence/`.

## 7. Evidence / files
- Practice folder: `../terminal-practice/` (`notes.txt`, `notes_archive.txt`, `sample.txt`, `sample_renamed.txt`)
- Redacted terminal log: `../evidence/mission-02-terminal-output.txt`

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Status:** Committed and pushed to `origin/main` on GitHub.
