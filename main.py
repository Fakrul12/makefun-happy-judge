"""make.fun entry: "Make the AI judge happy" (ai-happy-01).

Writes one happy image -- a smiling golden-retriever puppy in a
sunny flower meadow -- to /output/entry.png by copying the bundled
image.png. The copy is byte-for-byte (no re-encode), so both runs
write identical bytes. No network, no randomness.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
# Byte-for-byte copy (no re-encode), so the output is deterministic.
shutil.copyfile(SRC, DST)
print("wrote", DST)
