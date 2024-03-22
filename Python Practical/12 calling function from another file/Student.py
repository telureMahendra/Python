#filename: functions.py

def readMarks():
    return (int(input("Enter a Marks : ")))
def readName():
    return (input("Enter a Student name : "))

-----------------------------------------------
#Filename: student.py

from functions import *
sname = readName()
marks = readMarks()
print("Name is : ", sname)
print("Marks is : ", marks)

"""
Output:
    Enter a Student name : Mahi
    Enter a Marks : 45
    Name is :  Mahi
    Marks is :  45
""" 


