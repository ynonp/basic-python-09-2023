# Q1

print("enter a number?")
number = input()
sum_of_digits = 0

for x in number:
  sum_of_digits = sum_of_digits + int(x)

print(f"sum of digits: {sum_of_digits}")

# Q1 - as number
print("enter a number?")
number = int(input())
sum_of_digits = 0

while number > 0:
  sum_of_digits += number % 10
  number = number // 10

print(f"sum of digits: {sum_of_digits}")

# Q1 - taste from the future
print(sum(int(digit) for digit in input()))


# Q2
import random

secret_number = random.randint(1, 100)

while True:
  user_number = int(input("Select a number: "))
  if user_number == secret_number:
    print("Wow! That's the one")
    break
  elif user_number > secret_number:
    print("Too big, try a smaller one")
  elif user_number < secret_number:
    print("Too small, try a bigger one")


# Q2 - without the break
import random

secret_number = random.randint(1, 100)

user_number = int(input("Select a number: "))
while user_number != secret_number:
  if user_number > secret_number:
    print("Too big, try a smaller one")
  elif user_number < secret_number:
    print("Too small, try a bigger one")
  user_number = int(input("Select a number: "))

print("Wow! You found it")



# Q3
n = 1242

start = 2
start_is_prime = True

while True:
  while n % start == 0:
    print(start)
    n = n // start

  if n == 1:
    break

  start_is_prime = False

  while not start_is_prime:
    start += 1
    start_is_prime = True
    for i in range(2, start):
      if start % i == 0:
        start_is_prime = False



# n = 1242
# prime_factor = 2
# while n > 1:
#   while n % prime_factor == 0:
#     print(prime_factor)
#     n = n // prime_factor
#   prime_factor = next_prime_number_after(prime_factor)


# for -> iterate over a sequence of "things"
# while -> repeat something until / while a condition is true / false








