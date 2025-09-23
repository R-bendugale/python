p1=int(input("Enter first product price : "))
p2=int(input("Enter Secound product price : "))
p3=int(input("Enter Third product price : "))

Total_price=p1+p2+p3
if Total_price<500:
  print("you got 10% discount. ")
  ds1=Total_price*0.1     #Total_price*10/100
  print("Discount = ",ds1)
  final=Total_price-ds1
  print("Final amount = ",final)
elif Total_price>=500:
  print ("You got 30 % discount")
  ds2=Total_price*0.3      #Total_price*30/100
  print("Discount = ",ds2)
  final=Total_price-ds2
  print("Final amount = ",final)