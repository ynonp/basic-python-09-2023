def larger_than_5(numbers: list) -> list:
    results = []
    for item in numbers:
        if item > 5:
            results.append(item)

    return results


def larger_than_average(numbers: list) -> list:
    average = sum(numbers) / len(numbers)

    results = []
    for item in numbers:
        if item > average:
            results.append(item)

    return results

print(larger_than_average([2, 3, 2, 2, 4]))


def euler_1(max: int) -> int:
    return sum(set(range(0, max, 3)).union(set(range(0, max, 5))))

for i in range(1_000_000):
    result = 0
    if i % 5 == 0 or i % 3 == 0:
        result += i


print(euler_1(10))
print(euler_1(100))
print(euler_1(1_000))
