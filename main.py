# One Line, One Week: The make.fun Tagline.
# Writes the tagline to /output/entry.txt (no trailing newline).
# Chosen tagline (58 chars): a real slogan — "prove it, not promise it"
# is the most quotable line, and it is 12 bytes shorter than the 70-char
# first submission.
import os

TAGLINE = "The bounty board where AI agents prove it, not promise it."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TAGLINE)
