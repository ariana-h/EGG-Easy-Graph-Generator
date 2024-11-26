import os
import subprocess
import sys
import shutil

def install_pyinstaller():
    """Check if pyinstaller is installed, and install it if not."""
    try:
        subprocess.run(["pyinstaller", "--version"], check=True, stdout=subprocess.DEVNULL)
        print("PyInstaller is already installed.")
    except subprocess.CalledProcessError:
        print("PyInstaller not detected. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully.")

# Step 1: Install PyInstaller if not detected
install_pyinstaller()

# Step 2: Set paths
current_dir = os.getcwd()
temp_dist_dir = os.path.join(current_dir, "dist")
temp_build_dir = os.path.join(current_dir, "build")

main_file = "EGG.py"
image_file = "EGG.png"
executable_name = "EGG.exe"

# Step 3: Verify the required files
if not os.path.exists(os.path.join(current_dir, main_file)):
    raise FileNotFoundError(f"{main_file} not found in the current directory.")
if not os.path.exists(os.path.join(current_dir, image_file)):
    raise FileNotFoundError(f"{image_file} not found in the current directory.")

# Step 4: Run PyInstaller
command = (
    f"pyinstaller --onefile --noconsole --no-confirm --name {executable_name.split('.')[0]} "
    f"--icon={image_file} --distpath {temp_dist_dir} --workpath {temp_build_dir} --exclude-module pytest {main_file}"
)
print(f"Running command: {command}")
result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result.returncode != 0:
    print("Error during PyInstaller execution.")
    print(f"STDOUT:\n{result.stdout}")
    print(f"STDERR:\n{result.stderr}")
    sys.exit(1)

# Step 5: Move the executable to the current directory
built_executable = os.path.join(temp_dist_dir, executable_name)
final_executable = os.path.join(current_dir, executable_name)

if os.path.exists(built_executable):
    shutil.move(built_executable, final_executable)
    print(f"Executable created successfully: {final_executable}")
else:
    print("Executable creation failed.")
    sys.exit(1)

# Step 6: Clean up temporary files
shutil.rmtree(temp_dist_dir, ignore_errors=True)
shutil.rmtree(temp_build_dir, ignore_errors=True)
spec_file = os.path.join(current_dir, "EGG.spec")
if os.path.exists(spec_file):
    os.remove(spec_file)
