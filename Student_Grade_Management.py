students = ["Amit", "Neha", "Raj"]
grades = [85, 90, 78]

students.append("Ravi")
grades.append(88)

index = students.index("Neha")
grades[index] = 95

index = students.index("Raj")
students.pop(index)
grades.pop(index)

average = sum(grades) / len(grades)

highest = max(grades)
lowest = min(grades)

print("Students:", students)
print("Grades:", grades)
print("Average Grade:", average)
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
