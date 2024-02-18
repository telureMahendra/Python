# Write a program for Result processing using Dictionary

st ={}

def calPercentage(dic1):
    return ((dic1["sub1"] + dic1["sub2"] + dic1["sub3"])/len(dic1))

def printDetails(dic):
    print("Name      : ",dic["name"])
    print("Roll No.  : ",dic["rollNo"])
    print("Percentage: ",calPercentage(dic["marks"]))

def getInput(n):
    student={}
    student["name"] = input("Enter a student Name : " )
    student["rollNo"] = input("Enter a Roll Number : ")
    d = {}
    for i in range(3):
        d['sub'+str(i+1)] = int(input(f"Enter a marks of Subject {i+1}  : "))
    student["marks"] = d
    st['st'+str(n)] = student

count = int(input("Enter a number of students  : "))

for i in range(count):
    print("*******************************")
    getInput(i)
    
for i in range(count):
    print("*******************************")
    printDetails(st['st'+str(i)])


--------------------------------------------------------------------------
Output -
Enter a number of students  : 2
*******************************
Enter a student Name : mahi
Enter a Roll Number : 11
Enter a marks of Subject 1  : 54
Enter a marks of Subject 2  : 65
Enter a marks of Subject 3  : 76
*******************************
Enter a student Name : azhr
Enter a Roll Number : 12
Enter a marks of Subject 1  : 65
Enter a marks of Subject 2  : 75
Enter a marks of Subject 3  : 85
*******************************
Name      :  mahi
Roll No.  :  11
Percentage:  65.0
*******************************
Name      :  azhr
Roll No.  :  12
Percentage:  75.0





    




