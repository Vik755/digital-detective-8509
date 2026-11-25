# Mission 1 — Know your computer

## 1. Task / objective
Explain how a computer takes input, processes data, produces output, and stores information (IPOS). Identify and classify hardware and software items, and describe everyday computer-based systems beyond laptops and mobile phones.

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
**Chosen activity:** Writing, formatting, and saving a study note in a text editor on a laptop.

| Stage | What happens in my example? | Hardware / component involved |
| :--- | :--- | :--- |
| Input | Keystrokes and trackpad clicks enter text characters and save commands as electrical signals. | Keyboard and trackpad |
| Processing | The processor translates key codes into characters, applies editor formatting, and holds the active document in RAM while preparing the file bytes. | CPU (processor) and RAM (memory) |
| Output | The rendered characters, cursor updates, and "Saved" status indicator appear visually on the display. | Display screen and graphics controller |
| Storage | When saved, the file bytes are written permanently to non-volatile storage so the note remains available after power-off. | Solid-State Drive (SSD) |
| Retrieval (extra step) | Later, opening the note reads the stored bytes back from the SSD into RAM so the CPU can display them again. | SSD, RAM, CPU, and display screen |

**How the activity flows:** Physical key presses on the keyboard send input signals to the CPU, which processes them in memory (RAM) and updates the screen immediately as output. While editing, the note lives in temporary RAM; pressing Save instructs the operating system and CPU to write the data onto the SSD for long-term storage.

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| Keyboard | Hardware | Not applicable | Captures typed characters and shortcut commands as input |
| Solid-State Drive (SSD) | Hardware | Not applicable | Provides fast, non-volatile long-term storage for the OS, apps, and files |
| Display / Monitor | Hardware | Not applicable | Renders text, images, and UI windows as visual output |
| CPU (Central Processing Unit) | Hardware | Not applicable | Executes instructions and coordinates arithmetic, logic, and data movement |
| RAM (Memory) | Hardware | Not applicable | Temporarily holds active programs and data while the computer is running |
| macOS | Software | Operating system software | Manages hardware resources, memory, files, and provides the system environment for apps |
| VS Code | Software | Application software | Helps write, edit, and organize code and Markdown files |
| Web Browser (Chrome / Safari) | Software | Application software | Requests and renders web pages and online documentation |
| Terminal | Software | Utility software | Provides a command-line interface to inspect, manage, and maintain files and tools |
| Activity Monitor | Software | Utility software | Monitors running processes, CPU usage, memory, and disk activity to maintain system health |

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| Automated Teller Machine (ATM) | Dispenses cash and handles basic bank account transactions | Bank card insertion and PIN entered on keypad | Cash dispensed and transaction receipt printed / screen balance shown |
| Metro Ticket Vending Machine | Issues travel tickets or recharges transit smart cards | Touchscreen station selection and cash/UPI payment confirmation | Printed QR ticket or updated smart card balance |
| Automated Traffic Signal Controller | Regulates vehicle and pedestrian flow safely at intersections | Vehicle loop sensor / pedestrian push-button signal | Timed red, amber, and green LED light signals |

## 3. Commands / tools used
- Text editor (Markdown) — Used to structure and document the IPOS trace, hardware/software classification table, and everyday computer systems table.
- `git add mission-01-computer-basics/README.md`, `git commit`, `git push` — Stages, commits, and publishes Mission 1 independently.

## 4. My understanding
Every computing task follows the IPOS cycle regardless of device size: input captures raw data or user actions, processing turns that data into useful state in CPU and RAM, output presents results back to the user, and storage preserves data permanently across restarts. Distinguishing between hardware (physical components) and the three kinds of software (operating system, application, and utility) clarified how the OS sits between hardware and user applications, while utility tools help inspect and maintain the system. Everyday devices like ATMs and traffic lights are also computers running the same IPOS loop for dedicated tasks.

## 5. Difficulties faced
Deciding whether Terminal belongs under application software or utility software required careful thought, because it launches like an app yet is primarily used for system management and maintenance.

## 6. How I resolved them
I reviewed the definitions in the assignment: since Terminal and Activity Monitor are used to manage, inspect, and maintain the computer rather than create end-user documents, classifying them as utility software fits cleanly alongside VS Code and a web browser as application software.

## 7. Evidence / files
- `mission-01-computer-basics/README.md` (this report containing Tasks 1.1, 1.2, and 1.3)

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Status:** Committed and pushed to `origin/main` on GitHub.
