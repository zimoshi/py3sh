#!/usr/bin/env python3

import sys, os

print("Py3Sh Generator")

if len(sys.argv) < 3:
    print("Usage: script.py <python_script> <output_script> [args...]")
    sys.exit(1)

output_path = os.path.abspath(sys.argv[2])
symlink_path = f"/usr/local/bin/{os.path.basename(output_path)}"

with open(output_path, "w") as p:
    p.write("#!/bin/bash\n")  # Add shebang for execution
    command = f"python3 {sys.argv[1]} " + " ".join(sys.argv[3:]) + "\n"
    p.write(command)

# Make the script executable
os.chmod(output_path, 0o755)

# Handle symlink creation safely
try:
    if os.path.exists(symlink_path) or os.path.islink(symlink_path):
        os.remove(symlink_path)  # Remove existing file/symlink
    
    os.symlink(output_path, symlink_path)
    print(f"Generated {output_path} link to {symlink_path}")
except PermissionError:
    print(f"⚠️  Permission denied: Cannot create symlink at {symlink_path}")
    print("Try running the script with sudo if you need global access.")

