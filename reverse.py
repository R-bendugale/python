n = int(input("Enter a positive integer n: "))
if n > 0:
    print("Natural numbers up to", n, "in reverse order:")
    i = n
    while i >= 1:
        print(i, end=' ')
        i -= 1
else:
    print("Please enter a positive integer.")
