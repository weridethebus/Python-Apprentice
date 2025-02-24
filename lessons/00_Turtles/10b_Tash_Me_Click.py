import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 4, 5, 6]
y2 = [5, 4, 3, 2, 1]
y3 = [3, 4, 5, 4, 3]
y4 = [1, 2, 1, 2, 1]
y5 = [2, 2, 3, 3, 4]

# Creating a plot with your favorite colors
plt.plot(x, y1, color='seagreen', label='Sea Green')
plt.plot(x, y2, color='teal', label='Teal')
plt.plot(x, y3, color='lightseagreen', label='Seafoam Green')
plt.plot(x, y4, color='red', label='Red')
plt.plot(x, y5, color='skyblue', label='Sky Blue')

plt.title('Plot with Favorite Colors')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
