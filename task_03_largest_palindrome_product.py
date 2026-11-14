largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        text = str(product)
        if text == text[::-1] and product > largest:
            largest = product

print(largest)




