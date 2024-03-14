# Practical no.: 10
#Program to check whether the given number is palindrome by passing function name as an argument to another function.

def checkString(strg):
    if strg == strg[::-1]:
        print(strg, " is Palindrome String")
    else:
        print(strg, " is not a Palindrome String")
        
def checkNumber(num):
    ogNum=num
    rev=0
    while (num > 0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if ogNum == rev:
        print(ogNum, " is Palindrome Number" )
    else:
        print(ogNum, " is not a Palindrome Number" )
        
def read(fun):
    if fun == checkString:
        num = input("Enter a String to check is palindrome or not: ")
        fun(num)
    elif fun == checkNumber:
        num = int(input("Enter a Number to check is palindrome or not: "))
        fun(num)
    else:
        print("Provide valid argument!")
        
print("Choose your Selection")
print("1. string\n2. number")
inp = int(input("Enter selection number : "))

match inp:
        case 1:
            read(checkString)
        case 2:
            read(checkNumber)
        case default:
            print("Oops! wrong choice")
            
"""
Output 1:
    Choose your Selection
    1. string
    2. number
    Enter selection number : 2
    Enter a Number to check is palindrome or not: 123
    123  is not a Palindrome Number


Output 2:
    Choose your Selection
    1. string
    2. number
    Enter selection number : 1
    Enter a String to check is palindrome or not: aba
    aba  is Palindrome String
"""








