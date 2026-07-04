from pathlib import Path
import re

path = Path(r"c:/Users/DeLL/Desktop/BIODATA/mahesh_biodata.html")
text = path.read_text(encoding="utf-8")
pattern = re.compile(r'<img[^>]*src="data:image/[^"\s]+;base64,[^"\s]+"[^>]*>', re.I)
new_text, count = pattern.subn('<img src="image.jpeg" alt="Mahesh M. Sawarkar">', text, count=1)
if count == 0:
    raise SystemExit("No matching image tag found")
path.write_text(new_text, encoding="utf-8")
print("Updated")
