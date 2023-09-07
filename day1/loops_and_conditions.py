n = 10
   # bool
if n % 2 == 0 or n % 3 == 0:
    print("n is an even number")
    print("more lines")
else:
    print("n is an odd number")
    print("more else lines")

for character in "hello":
    print(character)

for i in range(3, 10):
    print(i)

print("---")
for x in range(10):
    print(x)

print("---")
for x in range(3, 100, 2):
    print(x)

print(sum(range(3, 100, 2)))

print("I'm out of if")

# while True:
#     print("Select a number")
#     n = int(input())
#     if n > 5:
#         print("That's it!")
#         break


while True:
    print("Select a number")
    try:
        n = int(input())
        print(f"7 / {n} = {7 / n}")
        break
    except ValueError:
        print("That wasn't a number. Try again")
    except ZeroDivisionError:
        print("Sorry zero doesn't work")


print(f"You typed {n}")







