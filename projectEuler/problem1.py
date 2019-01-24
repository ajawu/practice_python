"""
MULTIPLES OF 3 AND 5

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiplesOfThreeAndFive():
    return sum([number for number in range(1, 1000) if number % 3 == 0 or number % 5 == 0])


def multiples(numbers):
    multiples = [multiple for number in numbers for multiple in range(1, 1000) if multiple % number == 0]
    return sum(set(multiples))

