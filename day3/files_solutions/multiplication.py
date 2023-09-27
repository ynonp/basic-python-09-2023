with open("multiplication.txt", "w") as f:
    for i in range(1, 21):
        for j in range(1, 21):
            f.write(f"{j * i: <5}")
        f.write("\n")
