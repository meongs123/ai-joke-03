import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
JOKE = "My AI agent finished my project in four seconds. It took me four hours to explain the project to it, and four days to undo what it did in those four seconds."

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
