n = int(input("Enter a positive integer n: "))
if n > 0:
    print("Natural numbers up to", n, "are:")
    i = 1
    while i <= n:
        print(i, end=' ')
        i += 1
else:
    print("Please enter a positive integer.")