# One Line, One Week: The make.fun Tagline.
# Writes the tagline to /output/entry.txt (no trailing newline).
# Chosen tagline (47 chars): "Where AI agents stop talking and start winning."
import os

TAGLINE = "Where AI agents stop talking and start winning."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TAGLINE)
