# Student ID : 10890021
# Name : 柯玲萱 Cara

from glob import glob1
import pandas as pd;
#2. The students.csv data set file into a dataframe with pandas
df=pd.read_csv('./students.csv')

#3. First 10 rows
print("The first ten rows :")
print(df.head(10))
print("#"*50)
print()

#3. Last 10 rows
print("The last ten rows :")
print(df.tail(10))
print("#"*50)
print()

#4. Display the values of columns and indexex of students DataFrame

# 1. Columns values
print("Columns values :")
print(df.columns.values)
print("#"*50)
print()
# 2. Index values
print("Index values :")
print(df.index)
print("#"*50)
print()

#5. Display the data types of all columns of students DataFrame
print("Display the data types of all columns of students DataFrame")
print(df.dtypes)
print("#"*50)
print()

#6. Dispaly the dimensionality (shape) of the students DataFrame
print("Dispaly the dimensionality (shape) of the students DataFrame")
print(df.shape)
print("#"*50)
print()

#7. Display the counts of missing values of all columns of the students DataFrame
print(df.count())
print("#"*50)
print()
#8. Please select the column of "absences" as a Series by using two different methods
print("Please select the column of absences as a Series by using two different methods")
print("Method1: index operator")
print(df['absences'].head(10))
print("#"*50)
print()

# Method2: dot notation 
print("Method2: dot notation ")
print(df.absences.head(10))
print("#"*50)
print()

#9. Please dispaly 
# the total numbers of students' absences, 
# the minimum value of students' absences,
# the maximumvalue of students' absences, 
# and the mean value of students' absences 

absences = df['absences']
print("The total is {}".format(absences.sum()))
print("The minimum is {}".format(absences.min()))
print("The maximum  is {}".format(absences.max()))
print("The mean value is {}".format(absences.mean()))
print("#"*50)
print()

#10. Please creat a new column of "Average_Grade" for the students' of column "G1","G2","G3".
#that means the Average_Grade = (G1+G2+G3)/3.
#Display the first five records of columns "G1","G2","G3", and "Average_Grade"
G1= df['G1']
print("G1 :",G1.head(5))
G2= df['G2']
print("G2 :",G2.head(5))
G3= df['G3']
print("G3 :",G3.head(5))
Average_Grade = (G1+G2+G3)/3.
print("Average_Grade :",Average_Grade.head(5))
