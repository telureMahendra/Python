#multilevel Inheritance

class color:
    def __init__(s1,c):
        s1.ccolor=c

class brand(color):
    def __init__(s2, c, b):
        super().__init__(c)
        s2.cbrand = b

class car(brand):
    def __init__(s3, c,b,t):
        super().__init__(c,b)
        s3.type = t
    def getDetails(s3):
        print("Car type : ", s3.type)
        print("Brand is : ", s3.cbrand)
        print("Color is : ", s3.ccolor)


t = input("Enter a type  : ")
b = input("Enter a brand : ")
c = input("Enter a color : ")
print("-----------------------------------")
obj = car(c, b, t)
obj.getDetails()
