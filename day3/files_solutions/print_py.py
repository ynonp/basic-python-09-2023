import pathlib

for file in pathlib.Path(".").glob("*.py"):
    print(file)
