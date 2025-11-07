class employee:
    def __init__ (self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ₹{self.salary}")   
emp1=employee("rahul",50000)
emp2=employee("Vaidehi", 60000)
emp1.display()
emp2.display()