# Student ID: 10890021
# Name : 柯玲萱Cara

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load students.csv file into a DataFrame
df = pd.read_csv('students.csv')

# Line Plot: use pandas line plot to plot the “G3”
G3_series = df['G3']
G3_series.plot(kind='line',title="Line Plot of Students Final Grade by using Python Pandas.",legend=True)
plt.show()

# Line Plot: use python matplotlib to plot the “G3”
plt.plot(df['G3'], color='red')
plt.title("Line Plot of Students Final Grade by using Python Matplotlib")
plt.show()

# Scatter Plot: find the relationship between students’ final grades and absences. (use pandas scatter plot)
df.plot(x='G3', y='absences', kind='scatter', color='black')
plt.xlabel("G3", fontsize=12)
plt.ylabel("absences", fontsize=12)
plt.title("Absences vs. Final Grade, scatter plot by python Pandas.", fontsize=15)
plt.show()

# Scatter Plot: find the relationship between students’ final grades and absences. (use matplotlib scatter plot)
plt.scatter(x=df['absences'], y=df['G3'],color='red')
plt.xlabel("absences", fontsize=12)
plt.ylabel("students’ final grades", fontsize=12)
plt.title("Absences vs. Final Grade, scatter plot by python matplotlib.", fontsize=15)
plt.show()

# Scatter Plot: find the relationship between students’ final grades and absences. (use seaborn scatter plot)
sns.scatterplot(x='G3', y='absences', data=df, color='red')
plt.xlabel("G3", fontsize=12)
plt.ylabel("absences", fontsize=12)
plt.title("Absences vs. Final Grade, scatter plot by python seaborn", fontsize=15)
plt.show()