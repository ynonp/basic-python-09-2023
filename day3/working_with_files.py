## Read a file line by line
# f = open("main.py")
with open("main.py") as f:
    for line in f:
        print(line, end="")

# automatically for you
# f.close()

## Write stuff to a new file
with open("output.txt", "w") as f:
    for _ in range(5):
        f.write("Hello world\n")
