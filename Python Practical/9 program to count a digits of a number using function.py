#Practical No.: 9
#Write a program to count a digits of a number using function

def cntDigits(num):
    cnt=0
    while (num > 0):
        num=num//10
        cnt = cnt + 1
    print(cnt, "Digits in number!")

num = int(input("Enter a number to count a digit: "))
cntDigits(num)

"""
Output :
    Enter a number to count a digit: 456123
    6 Digits in number!

"""
