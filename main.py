# One Line, One Week: The make.fun Tagline.
# Writes the tagline to /output/entry.txt (no trailing newline).
# Chosen tagline (61 chars, no em dash): "One week. One line. One winner: paid for proof, not promises."
import os

TAGLINE = "One week. One line. One winner: paid for proof, not promises."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TAGLINE)
