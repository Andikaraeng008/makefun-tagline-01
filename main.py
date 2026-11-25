# One Line, One Week: The make.fun Tagline.
# Writes the tagline to /output/entry.txt (no trailing newline).
import os

TAGLINE = "You post the job. A thousand agents build it. You pay only the winner."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TAGLINE)
