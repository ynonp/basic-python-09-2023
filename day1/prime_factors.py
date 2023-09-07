n = 1921
start = 2


while n != 1:
    n = divide_n_by_start_as_many_times_as_you_can(n, start)
    start = next_prime_number_after(start)



start_is_prime = True

while True:
    while n % start == 0:
        print(start)
        n = n // start

    start_is_prime = False
    if n == 1:
        break

    while not start_is_prime:
        start += 1
        start_is_prime = True
        for i in range(2, start):
            if start % i == 0:
                start_is_prime = False

