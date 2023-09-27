# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89


# return the n-th number in fib
def fib(n: int) -> int:
    a = 1
    b = 1
    for _ in range(n):
        # do something n times
        a, b = b, a + b
    return a


def fibr(n: int) -> int:
    print(f"fibr({n})")
    if n < 2:
        return 1

    return fibr(n-1) + fibr(n-2)


def euler2():
    a = 1
    b = 1
    total_sum = 0

    while a < 4_000_000:
        # do something n times
        a, b = b, a + b
        if a % 2 == 0:
            total_sum += a
    return total_sum


print(euler2())
print(fibr(5))
