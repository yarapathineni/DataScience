# DataFrames in python

#while importing the package from python, use the below syntax
import pandas as pd

dictionary1 ={"Name": ['RAM','Ravi','Rani'],"Age": ['25','27','20'],"SEX":['M','M','F']}

df = pd.DataFrame(dictionary1);
df.shape
df.info
print(df);

#output is as follows.

'''

  ...: df = pd.DataFrame(dictionary1);
df.shape
df.info
print(df);
  Age  Name SEX
0  25   RAM   M
1  27  Ravi   M
2  20  Rani   F

'''

print(df.count)
print(df.columns)
print(df.values)
print(df.shape) # returns a tuple with no of columns and rows.
print(df.size)
print(df.describe)
print(df.head) # Retrieves only first 5 rows.
print(df.tail) # retrives last 5 rows from dataframe.

#output is as follows.

'''
print(df.count)
print(df.columns)
print(df.values)
print(df.shape) # returns a tuple with no of columns and rows.
print(df.size)
print(df.describe)
print(df.head) # Retrieves only first 5 rows.
print(df.tail) # retrives last 5 rows from dataframe.
<bound method DataFrame.count of   Age  Name SEX
0  25   RAM   M
1  27  Ravi   M
2  20  Rani   F>
Index(['Age', 'Name', 'SEX'], dtype='object')
[['25' 'RAM' 'M']
 ['27' 'Ravi' 'M']
 ['20' 'Rani' 'F']]
(3, 3)
9
<bound method NDFrame.describe of   Age  Name SEX
0  25   RAM   M
1  27  Ravi   M
2  20  Rani   F>
<bound method NDFrame.head of   Age  Name SEX
0  25   RAM   M
1  27  Ravi   M
2  20  Rani   F>
<bound method NDFrame.tail of   Age  Name SEX
0  25   RAM   M
1  27  Ravi   M
2  20  Rani   F>

'''
