import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
city1_temps = [25, 27, 26, 28, 30, 29, 31]  
city2_temps = [22, 24, 23, 25, 26, 28, 27]  
plt.plot(days, city1_temps, marker='o', color='blue', label='City A')
plt.plot(days, city2_temps, marker='s', color='red', label='City B')
plt.title('Temperature Comparison of Two Cities Over 7 Days')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()
