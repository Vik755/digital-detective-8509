# Mission 4 — How programs run

## 1. Task / objective
Create and run a one-line Python 3 program (`hello.py`) from Terminal, and compare how compilers and interpreters translate and execute programs.

## 2. Work completed

### Task 4.1 — Create and run a Python program
Created `mission-04-programs/hello.py` containing:
```python
print("Hello from Python")
```
Ran `python3 mission-04-programs/hello.py` from Terminal and observed the output:
```text
Hello from Python
```

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| When translation / execution happens | Translates the entire source program ahead of time before the program is executed. | Reads, translates, and executes instructions step by step at runtime. |
| Typical output | Produces a standalone executable file (or machine/bytecode binary) saved on disk. | Executes the source instructions directly and shows program output without emitting a separate native binary. |
| One example | `gcc` / `clang` (for C and C++) | `python3` (CPython for Python) |
| One advantage | Compiled programs usually run much faster at runtime and do not need the compiler present to execute. | Faster edit-test cycle, easier cross-platform execution, and immediate line-by-line error feedback during development. |

**Explanation in my own words:**
As shown in the comparison table, the key difference between a compiler and an interpreter is *when* source code is translated into machine-level work. A compiler (such as `clang` or `gcc`) converts the whole source file into an executable binary ahead of time, which makes the resulting program fast to run afterward. An interpreter (such as `python3`) processes and carries out instructions during runtime, so I can edit `hello.py` and run it right away in one step without a separate build stage. Modern language implementations often combine both ideas—for instance, standard Python compiles source code to bytecode first and then interprets that bytecode on a virtual machine.

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py` — Invokes the Python 3 interpreter to execute `hello.py` and print the greeting.
- `git add`, `git commit`, `git push` — Commits and publishes Mission 4 independently.

## 4. My understanding
Source code written by humans cannot be directly understood as plain text by the CPU—it has to be translated either ahead of time by a compiler or dynamically at runtime by an interpreter. Testing `hello.py` directly with `python3` showed how an interpreted workflow prioritizes quick feedback and portability, whereas compiled languages trade a build step for maximum runtime speed.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `hello.py` (one-line Python 3 program)
- `README.md` (Mission 4 report and compiler/interpreter comparison)

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Status:** Committed and pushed to `origin/main` on GitHub.
