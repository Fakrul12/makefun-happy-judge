"""make.fun entry: "Make the AI judge happy".

Writes one happy image to /output/entry.png by copying the
bundled image.png. No network, no randomness: both runs write
identical bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote", DST)
