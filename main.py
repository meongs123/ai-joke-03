import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
JOKE = "My coding agent couldn't fix the bug, so it changed the error message to 'Success.' The users are thrilled. The data is gone."

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
