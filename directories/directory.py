from pathlib import Path

directory_path = Path('../')

# List all files and directories in the specified directory
for entry in directory_path.iterdir():
    print(entry)