import matplotlib.pyplot as plt
import numpy as np

x =np.array [1, 2, 3, 4, 5]
y =np.array [10, 20, 15, 30, 25]

plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array[10, 20, 30, 40, 50]
y = np.array[12, 18, 25, 35, 45]

plt.scatter(x, y, color='red')

plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()

import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May"])
sales = np.array([120, 150, 180, 170, 210])

plt.bar(months, sales, color="skyblue")

plt.title("Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()

import matplotlib.pyplot as plt
import numpy as np

marks = np.random.normal(100,50,100)
plt.hist(marks, bins=50, color="green", edgecolor="black")

plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

import matplotlib.pyplot as plt
import numpy as np

subjects =np.array ["Math", "Science", "English", "Computer"]
marks =np.array [30, 25, 20, 25]

plt.pie(marks,
        labels=subjects,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Pie chart")

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array[1, 2, 3, 4, 5]
y = np.array[3, 5, 2, 6, 4]

plt.fill_between(x, y, color="lightblue")

plt.title("Area Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()