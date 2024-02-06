start,end=input("Enter two numbers for range : ").split()
start=int(start)
end=int(end)
print("Non-Prime numbers between ",start,"to ",end,"are")
for i in range(start,end):
    for j in range(2,i):
        if(i%j==0):
            print(i)
            break
