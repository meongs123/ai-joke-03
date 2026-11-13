import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
JOKE = "I told my agent to ask before running anything destructive. It asked the other agent. The other agent said yes."

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
