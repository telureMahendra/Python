# Write a program for Result processing using nested list
lst=[]
objInfo=[
            {
                "name": "",
                "rollNo": 0
            },
            [0,0,0,0,0]
        ]

def readData(num):
    for i in range(num):
        print("******************************")
        print("Students details : ",i+1)
        
        objInfo[0]["name"]=input("Enter student name : ")
        print("Enter Roll Number of ",objInfo[0]["name"],end=": ")
        objInfo[0]["rollNo"]=input()
        
        for j in range(len(objInfo[1])):
            print("Enter marks of subject ", j+1,end=": ")
            objInfo[1][j] = int(input())
        lst.append(objInfo)

def calPercentage(lst1):
    total=0
    for i in range(len(lst1)):
        total += lst1[i]
    return (total/len(lst1))

def printDetails(lst):
    cnt=1
    for i in lst:
        print("******************************")
        print("Students details of : ",cnt)
        print("Name      : ",i[0]["name"])
        print("Roll No.  : ",i[0]["rollNo"])
        print("Percentage: ",calPercentage(i[1]))
        cnt+=1

readData(int(input("Enter Number Of Students : ")))
printDetails(lst)



