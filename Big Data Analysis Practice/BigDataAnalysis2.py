# Name :柯玲萱 Cara
# Student ID : 10890021

# 2. Load the SuperStoreSales.csv as a DataFrame by using the Python Pandas and
#    set the column “State” as the index of DataFrame
import pandas as pd

df_SuperStoreSales = pd.read_csv('./SuperStoreSales.csv', index_col='State',encoding ="ISO-8859-1")

# 3. Please reduce memory usages of DataFrame by changing data types of columns. 
#    Please change the data type of columns of “Row ID”, “Postal Code”, and “Quantity” to integer 8. 
#    Please change the data type of “Sales”, “Discount”, and “Profit” to float 16. 
#    And please show how much memory usage is reduced 
#    by comparing the new DataFrame data types with original DataFrame data types.

print("Before reduce memory : ")
print(df_SuperStoreSales.info(memory_usage='deep'))

print("Please change the data type of columns of “Row ID”, “Postal Code”, and “Quantity” to integer 8")

print("######## Row ID ######## ")
print("Beore change data type : ")
print(df_SuperStoreSales['Row ID'].dtype)
df_SuperStoreSales['Row ID']  =  df_SuperStoreSales['Row ID'] .astype('int8')
print("After change data type : ")
print(df_SuperStoreSales['Row ID'].dtype)

print("######## Quantity ######## ")
print("Beore change data type : ")
print(df_SuperStoreSales['Quantity'].dtype)
df_SuperStoreSales['Quantity'] = df_SuperStoreSales['Quantity'] .astype('int8')
print("After change data type : ")
print(df_SuperStoreSales['Quantity'].dtype)

print("######## Postal Code ######## ")
print("Beore change data type : ")
print(df_SuperStoreSales['Postal Code'].dtype)
df_SuperStoreSales['Postal Code'] =  df_SuperStoreSales['Postal Code'] .astype('int8')
print("After change data type : ")
print(df_SuperStoreSales['Postal Code'].dtype)

print("Please change the data type of “Sales”, “Discount”, and “Profit” to float 16. ")
print("######## Sales ######## ")
print("Beore change data type : ")
print(df_SuperStoreSales['Sales']  .dtype)
df_SuperStoreSales['Sales']  = df_SuperStoreSales['Sales'].astype('float16')
print("After change data type : ")
print(df_SuperStoreSales['Sales']  .dtype)

print("######## Discount ######## ")
print("Beore change data type : ")
print(df_SuperStoreSales['Discount'].dtype)
df_SuperStoreSales['Discount'] =df_SuperStoreSales['Discount'].astype('float16')
print("After change data type : ")
print(df_SuperStoreSales['Discount'].dtype)

print("######## Profit ######## ")
print("Beore change data type : ")
print(df_SuperStoreSales['Profit'].dtype)
df_SuperStoreSales['Profit'] =df_SuperStoreSales['Discount'].astype('float16')
print("After change data type : ")
print(df_SuperStoreSales['Profit'].dtype)

print("After reduce memory : ")
print(df_SuperStoreSales.info(memory_usage='deep'))

print("-"*100)
# 4. Please use the data analysis method of selecting the smallest of the largest to 
#    find the 5 lowest profits Product Name from the top 1000 sales of products
#    (This means that these 5 products are the most unpopular in the market and 
#    should adjust product sales strategies or improve products)

print("Find the 5 lowest profits Product Name from the top 1000 sales of products")
top_1000_sales = df_SuperStoreSales.nlargest(1000,'Sales')
producets = top_1000_sales.nsmallest(5,'Profit')
print(producets)
print("5."+"-"*100)

# 5. Please select the “City” column as a Series with the indexing operator. 
#    After that, please select the City Series data with .iloc[] and .loc[] method respectively. 
#    Please select the city at the position 10 when using .iloc[] operator,
#    your result shoud be city of “Los Angeles”. 
#    Please achieve the same result byusing the .loc[] operator.
print("Please select the “City” column as a Series with the indexing operator.")
city = df_SuperStoreSales['City']
print(city.head(5))
print("Please select the city at the position 10 when using .iloc[] operator")
print(city.iloc[9])
print("Please achieve the same result byusing the .loc[] operator.")
print(city.loc[df_SuperStoreSales.City=="Los Angeles"].head(10))
print("-"*100)

# 6. Please select the DataFrame rows with the .iloc[] and .loc[] indexers.  
#    Please select the row No.100 by using the .iloc[] indexer. 
#    Please achieve the same result by using the .loc[] indexers.
print("Please select the row No.100 by using the .iloc[] indexer. ")
print(df_SuperStoreSales.iloc[99])
print(df_SuperStoreSales.loc['Illinois'])
# 7. Please select the DataFrame rows and columns simultaneously. 
#    Please select all rows of four columns “Category”, “Sub-Category”, “Sales”, and “Profit”
#    by using .iloc[] and .loc[] respectively. 
#    Your two operations results should be the same.
print("Please select the DataFrame rows and columns simultaneously.")
print("Please select all rows of four columns “Category”, “Sub-Category”, “Sales”, and “Profit”")
print(df_SuperStoreSales.iloc[:,[13,14,16,19]])
print("-"*100)
print(df_SuperStoreSales.loc[:,['Category','Sub-Category','Sales','Profit']])
print("-"*100)

# 8. Please use the data analysis method of calculating Boolean statistics to find
#    the number of profits that are more than 2000 dollars.
print("the number of profits that are more than 2000 dollars")
print((df_SuperStoreSales['Profit'] > 2000).head(10))
print("-"*100)

# 9. Please use the data analysis method of translating SQLWhere Clauses 
#    to find the products that meeting with four criteria. 
#    (1) state is California. (2) Category is Technology 
#    (3) Sales are greater than 4000 dollars. (4) Profits are greater than 5000 dollars.
df_SuperStoreSales = pd.read_csv('./SuperStoreSales.csv',encoding ="ISO-8859-1")
criteria_1 = df_SuperStoreSales.State == 'California'
criteria_2 = df_SuperStoreSales.Category == 'Technology'
criteria_3 = (df_SuperStoreSales.Sales > 4000) | (df_SuperStoreSales.Profit > 5000)
criteria_sum = criteria_1 & criteria_2 & criteria_3
print(criteria_sum.head(5))


