import base64
import tempfile
import subprocess
import os

# Load encoded script
with open("config.b64", "rb") as f:
    encoded = f.read()

# Decode
decoded = base64.b64decode(encoded)

# Run in temp file
with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
    tmp.write(decoded)
    tmp_path = tmp.name

try:
    subprocess.run(["python3", tmp_path], check=True)
finally:
    os.remove(tmp_path)
