import os
from pathlib import Path

print("Hello, World! This is a test application demonstrating environment variables, Docker secrets, and file I/O operations.")

# This code demonstrates how to read environment variables and Docker secrets in a Python application.
TEST_ENV= os.getenv("TEST_ENV", "default environment variable.")
print(f"Using test environment variable: {TEST_ENV}")

def load_secret(secret_path):
    secret = secret_path.read_text(encoding="utf-8").strip()
    return secret or None

docker_secret_path = Path("/run/secrets/secret1")

SECRET1 = load_secret(docker_secret_path)
print(f"Using secret1 which starts with: '{SECRET1[:2]}' and ends with: '{SECRET1[-2:]}'")

# The following code demonstrates file I/O operations for importing and exporting text data.
BASE_DIR = Path(__file__).resolve().parent
IMPORT_DIR = BASE_DIR / "IMPORT"
EXPORT_DIR = BASE_DIR / "EXPORT"
IMPORT_FILE = IMPORT_DIR / "import_text.txt"
EXPORT_FILE = EXPORT_DIR / "export_text.txt"

import_text = IMPORT_FILE.read_text(encoding="utf-8").strip()
print(f"Imported text: {import_text}")

EXPORT_DIR.mkdir(parents=True, exist_ok=True)
export_text = "Sample export text written by test-app."
EXPORT_FILE.write_text(export_text, encoding="utf-8")
print(f"Exported text to {EXPORT_FILE.name}: {export_text}")

