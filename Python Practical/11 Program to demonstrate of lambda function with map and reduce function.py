# 11: Program to demonstrate of lambda function with map and reduce function

from functools import reduce
num = input("Enter a number to addition of digits : ")
res = reduce(lambda x,y: int(x) + int(y), list(map(lambda x: int(x), num)))
print(res)
