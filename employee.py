class Employee:
    def work(self):
        print("Employee works in the company.") 
class Manager(Employee):
    def work(self):
        print("Manager manages the team and projects.")
class Developer(Employee):
    def work(self):
        print("Developer writes and tests code.")
class Intern(Employee):
    def work(self):
        print("Intern assists and learns from seniors.")
employees = [Manager(), Developer(), Intern()]
for emp in employees:
    emp.work()
