# The Digital Detective (`digital-detective-8509`)

An independent systems and computing investigation exploring how a computer works from hardware and Terminal operations to operating systems, program execution, number systems, Git/GitHub collaboration, and computer networking.

- **Author:** Vikas Shukla (`Vik755`)
- **Repository:** `digital-detective-8509`
- **Privacy note:** Personal system details (computer username, email address, device name, serial number, Wi-Fi name, and private IP address) are omitted or marked `[redacted]`.

## Commit & Documentation Workflow

Every mission (Mission 0 through Mission 8) was completed in order, documented in its own `README.md` using a consistent 8-section template, committed with a dedicated descriptive message, and pushed to GitHub before starting the next mission.

## Mission Index

| Mission | Title | Folder / README |
| :--- | :--- | :--- |
| Mission 0 | Create your GitHub workspace | [mission-00-setup/README.md](mission-00-setup/README.md) |
| Mission 1 | Know your computer | [mission-01-computer-basics/README.md](mission-01-computer-basics/README.md) |
| Mission 2 | Become comfortable with the Terminal | [mission-02-terminal/README.md](mission-02-terminal/README.md) |
| Mission 3 | Understand the operating system | [mission-03-operating-system/README.md](mission-03-operating-system/README.md) |
| Mission 4 | How programs run | [mission-04-programs/README.md](mission-04-programs/README.md) |
| Mission 5 | Numbers and data | [mission-05-numbers-data/README.md](mission-05-numbers-data/README.md) |
| Mission 6 | Git and GitHub | [mission-06-git-github/README.md](mission-06-git-github/README.md) |
| Mission 7 | How computers communicate | [mission-07-networking/README.md](mission-07-networking/README.md) |
| Mission 8 | Final report and submission | [mission-08-final-report/README.md](mission-08-final-report/README.md) |
| Evidence | Privacy-safe terminal outputs | [evidence/](evidence/) |

## Topics Explored

- **Computer Fundamentals & IPOS:** Input, Processing, Output, and Storage flow, hardware vs. software (OS, application, utility), and everyday embedded computer systems.
- **Terminal & File Management:** Path navigation, creating/copying/moving/appending files safely, command flags (`-l`, `-a`, `-h`), pipes (`|`), and inspecting Homebrew.
- **Operating Systems:** Kernel/OS details, processes and `PID`s, disk usage, absolute vs. relative paths, `rwx` permissions, and core OS responsibilities.
- **Program Execution:** Running Python 3 scripts and comparing compilers vs. interpreters.
- **Number Systems & Text Encoding:** Hand conversions across decimal, binary, and hexadecimal, Python verification, building `number_converter.py`, and ASCII vs. UTF-8 text representation.
- **Git & GitHub Collaboration:** Staging vs. committing, commit logs, branching (`update-about`), Pull Requests, and a Git command glossary.
- **Computer Networks:** `LAN`/`MAN`/`WAN`, `DNS`, routers, protocols, packet switching, client-server communication, `ping`, `nslookup`, and how a browser loads a website.

## Running the Number Converter

Run `number_converter.py` from inside its mission folder:

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

Enter any whole decimal integer when prompted (for example, `13`, `25`, or `255`) to see its binary and hexadecimal equivalents.

## What I Learned

Completing all nine missions connected high-level user actions down to how the computer actually executes them: every task follows the IPOS cycle managed by the OS through processes and permissions, stores numbers and text in binary/UTF-8, runs code via interpreters or compiled binaries, exchanges data across networks using DNS and protocols, and stays cleanly versioned through Git commits, branches, and Pull Requests.
