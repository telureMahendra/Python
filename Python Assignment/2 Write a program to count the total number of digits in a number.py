# 2.	Write a program to count the total number of digits in a number

num = int(input("Enter a number : "))
cnt=0
while(num>0):
    num = num // 10
    cnt += 1
    
print("Total digits : {0}".format(cnt))
