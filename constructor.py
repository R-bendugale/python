class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor called. Student name is:", self.name)

    def __del__(self):
        print("Destructor called. Object is being deleted.")
s1 = Student("Vaidehi")
del s1
