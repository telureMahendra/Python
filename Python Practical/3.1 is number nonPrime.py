n1 =int(input("Enter a Number : "))
i = 1
for i in range(2,n1+1):
    prime = False
    for j in range(2, (i-1) ):
        if(i%j==0):
            prime =  True
    if(prime==True):
            print(i,"\n")
        
