import pathlib

for file in pathlib.Path(".").glob("*.py"):
    if "import pathlib\n" in file.read_text():
        print(file)


