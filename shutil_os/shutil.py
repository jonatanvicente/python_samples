import shutil

# Copy a file from source to destination
shutil.copy('source.txt', 'destination.txt')
# Copy a directory from source to destination
shutil.copytree('source_directory', 'destination_directory')
# Move a file or directory from source to destination
shutil.move('source.txt', 'destination.txt')
# Remove a directory and all its contents
shutil.rmtree('directory_to_remove')