"""Simple decimal-to-binary and decimal-to-hexadecimal converter."""


def convert_decimal(number: int) -> tuple[str, str]:
    """Return binary and hexadecimal string representations for an integer."""
    return bin(number), hex(number)


def main() -> None:
    """Prompt the user for a decimal integer and print its binary and hex values."""
    raw_value = input("Enter a decimal integer: ").strip()
    try:
        decimal_number = int(raw_value)
    except ValueError:
        print("Error: please enter a valid whole number (for example, 25).")
        return

    binary_value, hex_value = convert_decimal(decimal_number)
    print(f"Decimal: {decimal_number}")
    print(f"Binary: {binary_value} (without prefix: {binary_value.removeprefix('0b') if decimal_number >= 0 else '-' + binary_value.removeprefix('-0b')})")
    print(f"Hexadecimal: {hex_value} (without prefix: {hex_value.removeprefix('0x').upper() if decimal_number >= 0 else '-' + hex_value.removeprefix('-0x').upper()})")


if __name__ == "__main__":
    main()
