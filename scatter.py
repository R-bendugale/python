import matplotlib.pyplot as plt
house_area = [800, 1000, 1200, 1500, 1800, 2000, 2300, 2500]
market_price = [120000, 150000, 180000, 210000, 250000, 270000, 300000, 330000]
plt.scatter(house_area, market_price, color='teal', edgecolor='black', s=80)
plt.title('House Area vs Market Price')
plt.xlabel('House Area (sq. ft.)')
plt.ylabel('Market Price ($)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
