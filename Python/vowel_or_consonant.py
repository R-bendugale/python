A = input("Enter a single alphabet : ")
if len(A)==1 and A.isalpha():
  if A.lower() in ['a','e','i','o','u']:
    print("It is a vowel.")
  else:
    print("It is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet.")

