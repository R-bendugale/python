Bsalry=int(input("Enter the Bsalry : "))
if Bsalry <= 10000:
  print("HRA House rent 40% allowance")
  HRA = Bsalry*40/100
  print("HRA is = ",HRA)
  DA = Bsalry*9/100
  print("Dearness = ",DA)
elif Bsalry > 10000:
  print("HRA House rent is 30 % allowance")
  HRA = Bsalry*30/100
  print("HRA is = ",HRA)
  DA = Bsalry*11/100
  print("Dearness = ",DA)
gs = Bsalry+HRA+DA
print("Gross Salary is =",gs)
