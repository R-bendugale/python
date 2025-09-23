n=int(input("Enter the number : "))
i=1
print("Factors of ",n)
while i<=n:
  if n%i==0:
    print(i,end=" ")
  i+=1