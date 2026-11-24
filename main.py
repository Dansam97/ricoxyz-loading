import os

TEXT = "Tip: your agent has read your code, your comments, and the lies in your README. It is now deciding which one to believe."


def validated_text():
    text = TEXT
    text.encode("utf-8")  # raises if not valid UTF-8
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be exactly one line"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main():
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Re-read the written file and prove its bytes are exactly what was validated.
    with open(path, "rb") as f:
        written = f.read()
    assert written == (text + "\n").encode("utf-8"), "written bytes differ from validated text"


if __name__ == "__main__":
    main()
