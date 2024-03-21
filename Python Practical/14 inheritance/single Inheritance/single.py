class student:
    def __init__(self, sroll, sname, classOfStudent):
        self.roll = sroll
        self.name = sname
        self.sclass = classOfStudent
        
    def display(self):
        print("Roll No.         : ", self.roll)
        print("Name             : ", self.name)
        print("Class of student : ", self.sclass)

obj = student(11,"Mahi", "MCA")
obj.display()

