n = int(input("Enter a positive integer n: "))
if n > 0:
    total = 0
    i = 2  # start from the first even number
    while i <= n:
        total += i
        i += 2  # move to the next even number
    print("Sum of even numbers up to", n, "is:", total)
else:
    print("Please enter a positive integer.")
