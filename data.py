import pandas as pd
numbers = pd.Series([10, 20, 30, 40, 50])
print("Series:\n", numbers)
print("\nSum:", numbers.sum())
print("Mean:", numbers.mean())
print("Max:", numbers.max())
print("Min:", numbers.min())
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("\nNames:\n", df['Name'])
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame after adding Bonus column:\n", df)
high_salary = df[df['Salary'] > 60000]
print("\nEmployees with Salary > 60,000:\n", high_salary)
