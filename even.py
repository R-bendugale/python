n = int(input("Enter a positive integer n: "))
if n > 0:
    print("Even numbers up to", n, "are:")
    i = 2
    while i <= n:
        print(i, end=' ')
        i += 2
else:
    print("Please enter a positive integer.")
