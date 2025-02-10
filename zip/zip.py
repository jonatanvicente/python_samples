import zipfile

# Create a ZipFile object in write mode
with zipfile.ZipFile('example.zip', 'w') as zipf:
    # Add a file to the zip file
    zipf.write('Quijote_chapter_1.txt', arcname='Quijote_chapter_1.txt')


# Create a ZipFile object in read mode
with zipfile.ZipFile('example.zip', 'r') as zipf:
    # Extract all the contents of the zip file
    zipf.extractall('extracted_files')