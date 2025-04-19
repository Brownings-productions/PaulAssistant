import os
import subprocess
import sys

def create_virtual_environment(env_name="env", requirements_file="requirements.txt"):
    # Step 1: Create a virtual environment
    print(f"Creating virtual environment '{env_name}'...")
    subprocess.run([sys.executable, "-m", "venv", env_name])

    # Step 2: Activate the virtual environment (platform-specific instructions)
    activate_script = os.path.join(env_name, "Scripts" if os.name == "nt" else "bin", "activate")
    print(f"Virtual environment '{env_name}' created. Activate it using:")
    if os.name == "nt":
        print(f"{activate_script}\\activate")
    else:
        print(f"source {activate_script}")

    # Step 3: Install dependencies from requirements.txt
    pip_path = os.path.join(env_name, "Scripts" if os.name == "nt" else "bin", "pip")
    if os.path.exists(requirements_file):
        print(f"Installing dependencies from '{requirements_file}'...")
        subprocess.run([pip_path, "install", "-r", requirements_file])
        print("Dependencies installed successfully!")
    else:
        print(f"'{requirements_file}' not found. Make sure the file exists in the same directory.")

if __name__ == "__main__":
    create_virtual_environment()