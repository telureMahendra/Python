#wap to convert word into numbers using dictionary and list
#name : Mahendra B. Telure
words={
        0: "zero",
        1: "one" ,
        2: "two",
        3: "three",
        4: "four" ,
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11:  "eleven",
        12:  "twelve",
        13:  "thir10 * teen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "founty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninty",
        100: "hundred"
        
        
    }

rem= 0
cnt=0
num = int(input("Enter a integer number (below 1000): "))

if num <= 19:
    print(words[num])
    
if (num > 19) and (num<100):
    cnt = 10 * (num // 10)
    rem = num % 10
    print(words[cnt], end=" ")
    print(words[rem])
    
if num == 100:
    print(words[100])

ahun=0

if num > 100:
    ahun =num // 100
    cnt = (num % 100)
    rem = cnt % 10
    cnt = cnt-rem
    if cnt == 0:
        print(words[ahum], words[100], end=" " )
        print(words[rem])
    else:
        print(words[ahun], words[100], end=" " )
        print(words[cnt], end=" ")
        print(words[rem])

















