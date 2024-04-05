# 15 operator overloading 
class opOverloading:
    def __init__(s, a, b):
        s.x = a
        s.y = b
    
    def __add__(s1, other):
        s1.x = s1.x * other.x
        s1.y = s1.y * other.y
    
    def show(s):
        print("X = {0} and y = {1}".format(s.x, s.y))
    
obj1 = opOverloading(2,3)
obj2 = opOverloading(4,5)

obj1.show()
obj2.show()


print("Addition operator overloaded to multiply: ")
obj1 + obj2
obj1.show()


"""
Output: 
    X = 2 and y = 3
    X = 4 and y = 5
    Addition operator overloaded to multiply: 
    X = 8 and y = 15
"""