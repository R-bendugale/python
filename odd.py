n = int(input("Enter a positive integer n: "))
if n > 0:
    print("Odd numbers up to", n, "are:")
    i = 1
    while i <= n:
        print(i, end=' ')
        i += 2
else:
    print("Please enter a positive integer.")
