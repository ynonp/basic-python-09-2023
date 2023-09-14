def vowels_at_the_beginning_key(character: str) -> int:
    print("Wow!")
    if character in "aeiou":
        return 1
    else:
        return 2


def vowels_at_the_beginning_key_v2(character: str) -> int:
    return character not in "aeiou"


# Using lambda is the same as passing in the function name
print(sorted("hello", key=lambda character: character not in "aeiou"))
print(sorted("hello", key=vowels_at_the_beginning_key_v2))


f = lambda x, y, z: x + y + z
print(f(3, 5, 9))



#
#
#
#
# print(vowels_at_the_beginning_key)
# print(vowels_at_the_beginning_key('a'))
#
#
#
# ########################
#
def print_times(text: str, times: int):
    for _ in range(times):
        print(text)


print_times("one", 3)
print_times(text="one", times=3)
print_times("one", times=5)
print_times(times=2, text="one")


#
# 1, 2, 3, 4, 5
#  *
#  2, 3, 4, 5
#    *
#    6, 4, 5
#      *
#      24, 5
#        *
#        120
#


from functools import reduce


def mul(acc, value):
    return acc * value


print(reduce(lambda acc, value: acc * value, range(1, 6)))
print(reduce(mul, range(1, 6)))



