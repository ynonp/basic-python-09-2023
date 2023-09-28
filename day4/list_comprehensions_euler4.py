def is_palindromic_number(n: int) -> bool:
  return str(n)[::-1] == str(n)


pelindroms = [i * j for i in range(999, 99, -1)
                    for j in range(999, 99, -1)
                    if is_palindromic_number(i * j)]

# Same as:
# for i in range(999, 99, -1):
#     for j in range(999, 99, -1):
#         product_of_two_3_digit = i * j
#
#         if is_palindromic_number(product_of_two_3_digit):
#             pelindroms.append(product_of_two_3_digit)

print(max(pelindroms))


# squares = []
# for i in range(10):
#     squares.append(i * i)
# List Comprehension
squares = [i * i for i in range(10)]
print(squares)






