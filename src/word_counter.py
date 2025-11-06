import sys
from pathlib import Path

def normalize_text(text: str) -> str:
    """Remove Windows EOF char (SUB, 0x1A) and normalize CRLF to LF."""
    # Remove ASCII SUB (Ctrl+Z) if present and normalize CRLF -> LF
    return text.replace("\x1a", "").replace("\r\n", "\n").replace("\r", "\n")

def count_text(text: str):
    """Return (lines, words, characters) for given text."""
    if not text:
        return 0, 0, 0

    # Normalize first
    text = normalize_text(text)

    # Lines: splitlines() handles multi-line cases cleanly
    lines_list = text.splitlines()
    lines = len(lines_list) if lines_list else 0

    # Words: split on whitespace (handles multiple spaces/newlines/tabs)
    words = len(text.split())

    # Characters: count everything except we may want to exclude the trailing newline if any.
    characters = len(text)

    return lines, words, characters

def display_output(lines: int, words: int, characters: int):
    print("\n--- RESULT ---")
    print(f"Lines     : {lines}")
    print(f"Words     : {words}")
    print(f"Characters: {characters}")

def read_from_stdin():
    print("Enter the Text below. (Ctrl+Z then Enter on Windows, Ctrl+D on Linux/Mac)")
    # Read until EOF
    text = sys.stdin.read()
    return text

def read_from_file(file_name: str):
    p = Path(file_name)
    if not p.exists():
        print(f"The file {file_name} does not exist.")
        return None
    try:
        return p.read_text(encoding="utf-8")
    except PermissionError:
        print(f"You don't have permission to read {file_name}.")
        return None

def main():
    option_invalid = True
    while option_invalid:
        option = input("\nSelect input mode (1 or 2)\n1. Direct text\n2. Text file\n> ").strip()
        if option in ("1", "2"):
            option_invalid = False

    if option == "1":
        text = read_from_stdin()
        text = normalize_text(text)
        lines, words, characters = count_text(text)
        display_output(lines, words, characters)

    else:  
        file_name = input("Enter file path: ").strip()
        text = read_from_file(file_name)
        if text is not None:
            text = normalize_text(text)
            lines, words, characters = count_text(text)
            display_output(lines, words, characters)

if __name__ == "__main__":
    main()
