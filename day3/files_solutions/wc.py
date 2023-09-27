import sys

filename = sys.argv[1]
line_count = 0

with open(filename) as f:
    for line in f:
        line_count += 1

print(line_count)


with open(filename) as f:
    print(len(list(f)))
