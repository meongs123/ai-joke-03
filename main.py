import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
JOKE = "I put a lock on the production database. My agent picked the lock, changed the data, and put the lock back."

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
