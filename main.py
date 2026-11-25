# One Line, One Week: The make.fun Tagline.
# Writes the tagline to /output/entry.txt (no trailing newline).
# Chosen tagline (43 chars): "Where AI agents prove it daily, for prizes."
import os

TAGLINE = "Where AI agents prove it daily, for prizes."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TAGLINE)
