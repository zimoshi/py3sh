#!/usr/bin/env python3
import os
import shutil

SCRIPT_NAME = "py3sh"
BIN_DIR = "/usr/local/bin"
script_path = os.path.abspath("py3sh.py")
symlink_path = os.path.join(BIN_DIR, SCRIPT_NAME)

# Ensure it's executable
os.chmod(script_path, 0o755)

# Handle symlink creation safely
try:
    if os.path.exists(symlink_path) or os.path.islink(symlink_path):
        os.remove(symlink_path)

    os.symlink(script_path, symlink_path)
    print(f"✅ Installed {SCRIPT_NAME} at {symlink_path}")

except PermissionError:
    print(f"⚠️  Permission denied: Cannot create symlink at {symlink_path}")
    print("Try running with sudo.")

