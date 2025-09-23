# i=97
# print(chr(i))
# while i<=122:
#   print(chr(i)," ",end="")
#   i+=1

# # reverce
# i=122
# while i>=97:
#   print(chr(i)," ",end="")
#   i-=1

# i=65
# while i<=91:
#   print(chr(i)," ",end="")
#   i+=1

Alpha=input("Enter character")
i=ord(Alpha)
while i>=ord("A"):
  print(chr(i),end=" ")
  i-=1