# Defining the function
def next_number(value: int) -> int:
    return value + 1

# default value
def multiply_3(a: float = 1, b: float = 1, c: float = 1) -> float:
    return a * b * c


def print_times(text: str, times: int = 1):
    for _ in range(times):
        print(text)


print_times("hello")

# Using the function / invocation
six = next_number(5)
print(multiply_3(2, 3))
print(six)

