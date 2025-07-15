# ID : 10890021
# Name : 柯玲萱 Cara

# Step 1 : install pandas on python environment
from audioop import mul
import pandas as pd;

# Step 2 : the students.csv data set file into a dataframe with pandas
df=pd.read_csv('./students.csv')

# Step 3 : Display the first five rows and the last five rows
# 1. The first five rows
print("The first five rows :")
print(df.head(5))
print("#"*100)
print()
# 2. The last five rows
print("The last five rows :")
print(df.tail(5))
print("#"*100)
print()

# Step 4 :　Display the values of columns and index of students DataFrame
# 1. Columns values
print("Columns values :")
print(df.columns.values)
print("#"*100)
print()
# 2. Index values
print("Index values :")
print(df.index)
print("#"*100)
print()

# Step 5：Display the shape of students DataFrame
print("Check the shape :")
print(df.shape)
print("#"*100)
print()

# Step 6 : Display the columns data types of students DataFrame
print("The columns data type :")
print(df.dtypes)
print("#"*100)
print()

# Step 7 : Display the data types counts of columns of students DataFrame
print("The data types counts of columns :")
print(df.dtypes.value_counts())
print("#"*100)
print()

# Step 8 : Select the column of “school” as a Series by using two different methods.
# Method1: index operator
print("Method1: index operator")
print(df['school'].head(10))
print("#"*100)
print()

# Method2: dot notation 
print("Method2: dot notation ")
print(df.school.head(10))
print("#"*100)
print()

# Step 9 : Convert the school Series into a DataFrame
#          Show the first five rows of records of new DataFrame
school = df['school']
df_school = school.to_frame()
print("Convert the school Series :")
print(df_school.head(5))
print("#"*100)
print()

# Step 10 : Display the school name value counts
print("The school name value counts :")
print(school.value_counts())
print("#"*100)
print()

# Step 11 : Return numbers of non-missing values of school column
school_filled = school.fillna(0)
print("Numbers of non-missing values :")
print(school_filled.count())
print("#"*100)
print()

# Step 12 : Select the column of “G3”, and display basics statistics of this column
#           Such as min, max, mean, median, standard deviations(std), sum
G3 = df['G3']
print("The maximum G3 is {}".format(G3.max()))
print("The minimum G3 1 is {}".format(G3.min()))
print("The mean value of G3 is {}".format(G3.mean()))
print("The median value of G3 is {}".format(G3.median()))
print("The standard deivation  of G3 is {}".format(G3.std()))
print("The sum of G3 is {}".format(G3.sum()))
print("#"*100)
print()

# Step 13 : Display the quantile values of 0.1, 0.3, 0.5, 0.7, 0.9 of the column of “G3”.
print(G3.quantile([0.1, 0.3, 0.5, 0.7, 0.9]))
print("#"*100)
print()

# Step 14 : Show any missing values contained in the column of “G3”
print(G3.isnull())

# Step 15 : Create a new column of “G3_by_10”, which the values of this column is 
#           equal to column “G3” multiply by 10. And display the first five records of 
#           columns “G3” and “G3_by_10”
G3_by_10 = df['G3']
print("The top 5 rows of G3_by_10 are")
print("G3  first five columns :",G3.head(5))
print("G3_by_10 first five columns :",G3_by_10.mul(10).head(5))
print("#"*100)
print()

# Step 16 : Display the top 5 final grade of “G3” with the most occurrences by using 
#           the chained value_counts() and head() methods. 
print("Top 5 final grade of “G3” with the most occurrences :")
G3_most_occurrences = G3.value_counts()
print(G3_most_occurrences.head(5))
print("#"*100)
print()
# Step 17 :  Create a new DataFrame students2 with setting the “school” as the index 
#            by using two different methods. 
# Method 1 :
print(students2 = df['school'])
# Method 2 :
print(students2 = df.school)

# Step 18 :  Delete the column of “address” of student2 DataFrame, and display the 
#            columns values after deleting the column. 
student2 = df
student2 =student2.drop('address', axis=1)
print(student2.columns)

