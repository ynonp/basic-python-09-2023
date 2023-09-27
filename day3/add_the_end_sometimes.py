"""
Take a file name from sys.argv
If the file contains the word "python"
then add to its end the line "--- the end ---"
else don't add anything
"""
import sys
import tempfile
import shutil

filename = sys.argv[1]
temp_file_handle, temp_filename = tempfile.mkstemp()

file_contains_python = False

with open(temp_filename, "w") as tmp:
    with open(filename) as f:
        for line in f:
            if "python" in line:
                file_contains_python = True
            tmp.write(line)
        if file_contains_python:
            tmp.write("--- the end ---")

    shutil.copy(temp_filename, filename)
