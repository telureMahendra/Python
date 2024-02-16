
#WAP to find largest of three without any control statement
n1=int(input("Enter 1st Number : "))
n2=int(input("Enter 2nd Number : "))
n3=int(input("Enter 3rd Number : "))
lar1 = ((n1+n2) + abs(n1-n2))//2
lar2 = ((lar1 + n3) + abs(lar1-n3))//2
print("Max Number is : ", lar2)
