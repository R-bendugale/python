# N=int(input("Enter Number : "))
# while N>0:
#   rem=N%10
#   N//=10
#   print(rem,end="")


# no=123
# rev=0
# while no>0:
#   id=no%10
#   rev=rev*10+id
#   no=no//10
# print(rev)

no=123
rev=int(str(no)[::-1])
print(rev)
