n = int(input("Enter a number: "))

# Set the limit
limit = n ** 2

# Initialize value
value = 1

# Use a for loop to generate powers of 2 up to n^2
for _ in range(100):  # Use a large enough range
    if value > limit:
        break
    print(value, end=" ")
    value *= 2