def factorial(n):
    r = 1
    for i in range(1 , n+1):
        r *= i
    return r
def num_sum(number):
    tol = 0
    number = str(number)
    for i in number:
        tol += int(i)
    return tol
print(num_sum(factorial(100)))


        
