def evenFibonacci():
    a, b = 1, 2
    while a < 4000000:
        if a % 2 == 0:
            yield a
        a, b = b, a + b


total_fibonacci = sum(evenFibonacci())
print(total_fibonacci)