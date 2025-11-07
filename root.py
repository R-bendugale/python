num = int(input("Enter a number: "))
sqrt = int(num ** 0.5)
if sqrt * sqrt == num:
    for i in range(2, sqrt):
        if sqrt % i == 0:
            print("Square root is not prime")
            break
    else:
        print("Square root is prime")
else:
    print("Not a perfect square")