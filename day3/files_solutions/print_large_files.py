import pathlib

for file in pathlib.Path(".").glob("*"):
    if file.stat().st_size > 1_000_000:
        print(file, file.stat().st_size)


