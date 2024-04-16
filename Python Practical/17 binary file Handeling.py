"""
17: Create a list 10 elements. 
    Write a program to write this list in binary file and then 
    read it back to find out the smallest and largest value 
"""
def findSL(li):
    sm = li[0]
    lg = li[0]
    for i in li:
        if sm > i:
            sm = i
        if lg < i:
            lg = i
    print("Smallest Element is : ", sm)
    print("Largest Element is : ", lg)
            

li = [2,8,1,9,5,7,4,6,3,10]

fp = open("listFile.bin", "wb" )
# fp.write(bytes(li))
fp.write(bytearray(li))
fp.close()

fp1 = open("listFile.bin", "rb" )
data = list(fp1.read())
# print(data)

# using user defined function
findSL(data)

# using predefined functions
print("Smallest Element is : ", min(data))
print("Largest Element is : ", max(data))