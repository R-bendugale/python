import matplotlib.pyplot as plt
import random
salaries = [random.randint(30000, 120000) for _ in range(200)]
plt.hist(salaries, bins=10, color='orange', edgecolor='black')
plt.title('Salary Distribution in Company')
plt.xlabel('Salary Range ($)')
plt.ylabel('Number of Employees')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

