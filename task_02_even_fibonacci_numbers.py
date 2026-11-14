def even_fibo():
    a, b = 1, 2
    even = 0

    while a <= 4000000:
        if a % 2 == 0:
            even += a
        a, b = b, a + b

    return even

print(even_fibo())
