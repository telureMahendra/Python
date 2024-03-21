#import myPackage.functions as fun

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
