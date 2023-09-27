"""
Take a file name as command line argument
and print the contents of the file
"""
import sys

filename = sys.argv[1]

try:
    with open(sys.argv[1]) as f:
        for line in f:
            print(line, end="")
except FileNotFoundError:
    print(f"Sorry file not found [{filename}]")
