def sum_3_5():
    total = 0
    for x in range(1,1000):
        if x % 3 == 0 or x % 5 == 0:
            total += x
            print(total)
    return total
        
sum_3_5()