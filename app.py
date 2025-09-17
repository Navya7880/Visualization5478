import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = np.sin(x) + np.random.normal(0, 0.2, 50)
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
scatter_x = np.random.rand(50)
scatter_y = np.random.rand(50)
scatter_colors = np.random.rand(50)
scatter_sizes = 500 * np.random.rand(50)

# 1. Line Plot
plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o', color='blue')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# 2. Bar Chart
plt.figure(figsize=(6,4))
plt.bar(categories, values, color='green')
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()

# 3. Histogram
data = np.random.randn(1000)
plt.figure(figsize=(6,4))
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(scatter_x, scatter_y, c=scatter_colors, s=scatter_sizes, alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 5. Pie Chart
plt.figure(figsize=(6,6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()
