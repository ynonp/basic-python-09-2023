def sum_digits(n: int) -> int:
    # While loop - do something as long as n > 0
    # while I have digits
    result1 = 0
    while n > 0:
        digit = n % 10
        result1 += digit
        n //= 10
    return result1


print(sum_digits(1357))
print(sum_digits(9812))
print(sum_digits(9812123451234))



# n = 92530
#
#
#
# # For loop - do something for each character in a string
# n = 92530
# result2 = 0
# for character in str(n):
#     digit = int(character)
#     result2 += digit
# print(result2)






