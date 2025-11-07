def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
n = int(input("Enter the value of n: "))
sum_series = 0
for i in range(n + 1):
    sum_series += 1 / factorial(i)
print(f"The sum of the series up to 1/{n}! is: {sum_series}")