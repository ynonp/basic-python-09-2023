# sys - builtin module
import sys
import shutil

print(sys.argv)
# sys.argv[1:3]
# sys.argv[1:]
for destination in sys.argv[1:]:
  source = sys.argv[0]
  print(f"copy {source} -> {destination}")
  shutil.copy(source, destination)
