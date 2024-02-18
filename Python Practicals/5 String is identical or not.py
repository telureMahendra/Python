s1=input("Enter First String : ")
s2=input("Enter Second String : ")
r=False

for i in range(len(s1)):
    if(s1[i] != s2[i]):
        r=True
if(r):
    print("String Is not identical")
else:
    print("String Is identical")
    
