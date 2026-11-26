# Mission 5 — Numbers and data

## 1. Task / objective
Practise manual conversions between decimal, binary, and hexadecimal, verify every calculation using Python's built-in functions, build and test `number_converter.py`, and explain how characters are stored using ASCII and UTF-8.

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| Convert decimal `13` to binary. | Repeated division by 2: `13 ÷ 2 = 6` remainder `1`; `6 ÷ 2 = 3` remainder `0`; `3 ÷ 2 = 1` remainder `1`; `1 ÷ 2 = 0` remainder `1`. Reading remainders bottom-to-top gives **`1101`**. Check: `8 + 4 + 0 + 1 = 13`. |
| Convert decimal `25` to binary. | Repeated division by 2: `25 ÷ 2 = 12` remainder `1`; `12 ÷ 2 = 6` remainder `0`; `6 ÷ 2 = 3` remainder `0`; `3 ÷ 2 = 1` remainder `1`; `1 ÷ 2 = 0` remainder `1`. Reading remainders bottom-to-top gives **`11001`**. Check: `16 + 8 + 0 + 0 + 1 = 25`. |
| Convert binary `1010` to decimal. | Positional powers of 2: `(1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰) = 8 + 0 + 2 + 0 =` **`10`**. |
| Convert binary `1101` to decimal. | Positional powers of 2: `(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰) = 8 + 4 + 0 + 1 =` **`13`**. |
| Convert hexadecimal `A` to decimal. | In base 16, `A = 10`: `10 × 16⁰ =` **`10`**. |
| Convert hexadecimal `1F` to decimal. | In base 16, `F = 15`: `(1 × 16¹) + (15 × 16⁰) = 16 + 15 =` **`31`**. |
| Convert binary `1111` to hexadecimal. | Four bits equal one hex digit: `(1 × 8) + (1 × 4) + (1 × 2) + (1 × 1) = 15` in decimal, which is **`F`** in hexadecimal. |

### Task 5.2 — Verify using Python
Verified in Python 3 using `bin()`, `hex()`, and `int(value, base)`:

| Expression tested | Observed Python result | Matches manual calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes (`1101`) |
| `bin(25)` | `'0b11001'` | Yes (`11001`) |
| `int('1010', 2)` | `10` | Yes (`10`) |
| `int('1101', 2)` | `13` | Yes (`13`) |
| `int('A', 16)` | `10` | Yes (`10`) |
| `int('1F', 16)` | `31` | Yes (`31`) |
| `hex(15)` | `'0xf'` | Yes (`F`) |
| `hex(31)` | `'0x1f'` | Yes (`1F`) |
| `hex(int('1111', 2))` | `'0xf'` | Yes (`F`) |

### Task 5.3 — Build a small number converter
Built `mission-05-numbers-data/number_converter.py`, which prompts the user for a decimal integer via `input()`, parses it with `int()`, and prints both binary (`bin()`) and hexadecimal (`hex()`) results (with and without the `0b` / `0x` prefixes). Invalid non-integer text is caught cleanly with a `try/except ValueError` message.

- **What `bin()` and `hex()` do:** Python's built-in `bin(n)` takes an integer and returns its binary representation as a string prefixed with `'0b'` (e.g., `bin(13) -> '0b1101'`). Python's built-in `hex(n)` takes an integer and returns its base-16 hexadecimal representation as a lowercase string prefixed with `'0x'` (e.g., `hex(255) -> '0xff'`).

**Test runs from Terminal (`python3 number_converter.py`):**

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| `13` | `0b1101` (`1101`) | `0xd` (`D`) |
| `25` | `0b11001` (`11001`) | `0x19` (`19`) |
| `255` | `0b11111111` (`11111111`) | `0xff` (`FF`) |

### Task 5.4 — How is text stored?
- **ASCII decimal codes:** Uppercase `'A'` is `65` (`ord('A') == 65`) and lowercase `'a'` is `97` (`ord('a') == 97`).
- **Why computers need an encoding standard:** Computer memory can only store numbers in binary (`0`s and `1`s), so an encoding standard provides an agreed lookup table mapping each character to a specific numeric code—ensuring two different programs or computers read the same bytes back as the exact same letters and symbols.
- **Character outside basic ASCII:** The Indian Rupee symbol `₹` (Unicode `U+20B9`, encoded in UTF-8 as three bytes `E2 82 B9`) or accented letters like `é` and emojis like `😊` are not part of 7-bit basic ASCII (`0–127`), which is why UTF-8 is widely used today.

## 3. Commands / tools used
- `python3 -c "..."` — Verified manual conversions and ASCII `ord()` codes in Python 3.
- `python3 number_converter.py` — Ran and tested the interactive converter script with `13`, `25`, `255`, and invalid input `abc`.
- Python built-ins `input()`, `int()`, `bin()`, `hex()`, `ord()` — Used for reading input, converting types/bases, and inspecting character codes.

## 4. My understanding
Everything inside a computer—whether a whole number or a text message—is stored as bits (`0` and `1`). Binary matches hardware on/off states directly, while hexadecimal groups 4 bits per digit (`0–F`) so humans can read long binary values compactly. Text encodings such as ASCII and UTF-8 extend this idea by assigning standardized numbers to characters so text stays consistent across devices and languages.

## 5. Difficulties faced
When first running `bin()` and `hex()`, Python prefixes outputs with `0b` and `0x`, which looks slightly different from hand-written conversions like `1101` or `19`. Also, entering non-numeric text into `int()` raises a `ValueError` crash if unhandled.

## 6. How I resolved them
I kept the standard `0b`/`0x` outputs from `bin()` and `hex()` so the representation is unambiguous, displayed the prefix-stripped uppercase hex form alongside it for readability, and wrapped `int(raw_value)` in `try/except ValueError` so invalid input prints a friendly error instead of crashing.

## 7. Evidence / files
- `number_converter.py` (working Python decimal-to-binary and decimal-to-hexadecimal converter)
- `README.md` (manual working, Python verification, test table, and text-encoding notes)

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Status:** Committed and pushed to `origin/main` on GitHub.
