#Addition of Digits of number using while Loop
number=int(input("Enter the number : "))
temp=number
add=0
while temp:
    r=temp%10
    add+=r
    temp=temp//10 
 
print("\nAddition of ",number,"is ",add) 
