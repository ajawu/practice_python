def primes(end):
    prime_list = []
    sieve_list = [True] * (end + 1)
    for each_number in range(2, end + 1):
        if sieve_list[each_number]:
            prime_list.append(each_number)
            for every_multiple_of_the_prime in range(each_number * each_number, end + 1, each_number):
                sieve_list[every_multiple_of_the_prime] = 0
    return prime_list


def largestPrimeFactor(number):
    # Reduce number of values to check
    largest_possible = int(number ** 0.5)

    # change value of largest_possible to closest odd if even
    if not largest_possible % 2:
        largest_possible -= 1

    prime_numbers = primes(largest_possible)[::-1]

    # Return largest factor that is a prime number
    for value in prime_numbers:
        if not number % value:
            return value
    return number


# 6857
print(largestPrimeFactor(600851475143))
