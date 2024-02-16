n1 =int(input("Enter a Number : "))
i = 1
for i in range(2,n1+1):
    for j in range(2, i ):
        if(i%j==0):
            print(i,"\n")
            break
