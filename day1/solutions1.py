# Q1
print("What is your age in years?")
age_years = int(input())
age_month = age_years * 12

print(f"Your age in month is {age_month}")


# Q2
print("Please enter a random 10 digit number?")
number = int(input())
print(f"This is your number {number}")
number_7 = number % 7

if number_7 == 0 or "7" in str(number):
  print("Your number is divisable by 7")
else:
  print("Your number is not divisable by 7 or contains 7")


# Q3
n = 49
a = 3
L = 99

S = (n / 2) * (a + L)
print(S)
