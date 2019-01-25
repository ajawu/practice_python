def palindrome():
    three_digits = list(range(100, 1000, 1))
    for a in three_digits:
        for b in three_digits:
            product = a * b
            if product == int(str(product)[::-1]):
                yield product


print(max(list(palindrome())))
