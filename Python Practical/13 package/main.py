#Filename: myPackage/functions.py
# WAP to swap the first and last letters of each word in the string
def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a//b

----------------------------------------------------------------

#filename: main.py
from myPackage.functions import *

a,b = 30,20

add = addition(a,b)
sub = substraction(a,b)
mul = multiplication(a,b)
div = division(a,b)

print("Addition of {0} and {1} is : {2}". format(a,b,add))
print("Substraction of {0} and {1} is : {2}". format(a,b,sub))
print("Multiplication of {0} and {1} is : {2}". format(a,b,mul))
print("Division of {0} and {1} is : {2}". format(a,b,div))


"""
Output :
    Addition of 30 and 20 is : 50
    Substraction of 30 and 20 is : 10
    Multiplication of 30 and 20 is : 600
    Division of 30 and 20 is : 1
"""
