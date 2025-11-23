
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("dataset.csv")

# Bar chart
plt.bar(df['Category'], df['Sales'])
plt.title("Sales by Category")
plt.savefig("charts/bar_chart.png")
plt.close()

# Pie chart
plt.pie(df['Expense'], labels=df['Category'])
plt.title("Expense Distribution")
plt.savefig("charts/pie_chart.png")
plt.close()

# Scatter plot
plt.scatter(df['Sales'], df['Expense'])
plt.title("Sales vs Expense")
plt.xlabel("Sales")
plt.ylabel("Expense")
plt.savefig("charts/scatter_plot.png")
plt.close()
