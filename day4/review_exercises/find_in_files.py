# How do you find all the .py files in a directory?
import pathlib


# Find all the files that have the text "import pathlib"
def text_in_file(needle: str, haystack: pathlib.Path):
  return needle in haystack.read_text()


path = pathlib.Path(".")
print(path.glob("*.lock"))
print(list(path.glob("*.lock")))

files_with_import_pathlib = []

for file in path.glob("*.py"):
  if text_in_file("import pathlib", file):
    print(f"I found {file}")
    files_with_import_pathlib.append(file)

print("---")
print(f"I found a total of {len(files_with_import_pathlib)} files")
