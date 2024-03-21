# WAP to swap the first and last letters of each word in the string

starlink = input("Enter a string : ").split()

for i in starlink:
    count = 0
    lastChar = (len(i)) - 1
    word = ""
    for j in i:
        if count == 0:  
            word = word + i[lastChar]
            count = count+1
            
        elif count == lastChar:
            word = word + i[0]
            count = count+1
            
        else:
            word = word + j
            count = count+1
    print(word)
