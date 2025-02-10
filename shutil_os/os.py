import os

# List all files and directories in the specified path
files = os.listdir('path_to_directory')
print(files)
# Create a new directory
os.mkdir('new_directory')
# Remove a file
os.remove('file_to_remove.txt')
# Rename a file or directory
os.rename('old_name.txt', 'new_name.txt')
# Get the current working directory
current_directory = os.getcwd()
print(current_directory)