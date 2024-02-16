#wap to convert word into numbers using dictionary and list
#name : Mahendra B. Telure
number={
        "zero": 0,
        "one" : 1,
        "two": 2,
        "three":3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

word = list(input("Enter a word : ").split())

for i in word:
    if i in number:
        print(number[i], end=" ")
