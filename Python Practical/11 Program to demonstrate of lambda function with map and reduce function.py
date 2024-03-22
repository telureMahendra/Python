# 11: Program to demonstrate of lambda function with map and reduce function
# program to add digits off number
from functools import reduce
num = input("Enter A number : ")
res = reduce(lambda x,y: int(x) + int(y), list(map(lambda x: int(x), num)))
print("Addition Of digits : ",res)


"""
Output:
    Enter A number : 1234
    Addition Of digits :  10
"""
