# WAP to swap two numbers using BITWISE operators
n1=int(input("Enter 1st Number : "))
n2=int(input("Enter 2nd Number : "))
print("Befor Swaping N1 = ", n1, " N2 = ",n2)
n1 = n1 ^ n2
n2 = n1 ^ n2 
n1 = n1 ^ n2
print("After Swapping N1 = ", n1, " N2 = ",n2)
