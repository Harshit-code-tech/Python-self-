def square_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

n = 100
print(square_sum(n))
