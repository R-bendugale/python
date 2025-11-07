n = int(input("Enter a positive integer n: "))

if n > 0:
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 2
    print("Sum of odd numbers up to", n, "is:", total)
else:
    print("Please enter a positive integer.")
