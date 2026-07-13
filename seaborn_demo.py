import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 18, 25]

sns.lineplot(x=x, y=y, marker="o")

plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50,45,78,90,34,56,78,23,45,65,83]
y = [12, 18, 25, 35, 45,89,34,23,67,90,12,56,78,34,12]

sns.scatterplot(x=x, y=y, color="red", s=100)

plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May"])
sales = np.array([120, 150, 180, 170, 210])

sns.barplot(x=months, y=sales)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

marks = np.random.normal(100,50,100)

sns.histplot(marks, bins=50, color="red")

plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

sns.heatmap(data, annot=True, cmap="YlGnBu")

plt.title("Heatmap")

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

sns.boxplot(marks)

plt.title("Box Plot")
plt.show()
