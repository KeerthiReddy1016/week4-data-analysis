
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data.csv")

# Bar chart
plt.bar(df['Category'], df['Sales'])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("bar_chart.png")
plt.close()

# Line chart
plt.plot(df['Month'], df['Temperature'])
plt.title("Monthly Temperature Changes")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.savefig("line_chart.png")
plt.close()

print("Charts generated: bar_chart.png, line_chart.png")
