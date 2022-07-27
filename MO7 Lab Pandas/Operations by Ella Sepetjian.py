Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Operations by Ella Sepetjian
import numpy as np
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4], 'col2':[444,555,666,444], 'col3':['abc','def','ghi','xyz']})
df.head()
   col1  col2 col3
0     1   444  abc
1     2   555  def
2     3   666  ghi
3     4   444  xyz
df['col2'].unique()
array([444, 555, 666], dtype=int64)
len(df['col2'].unique())
3
df['col2'].nunique()
3
df['col2'].value_counts()
444    2
555    1
666    1
Name: col2, dtype: int64
df[df['col2']>2]
   col1  col2 col3
0     1   444  abc
1     2   555  def
2     3   666  ghi
3     4   444  xyz
df['col2']>2
0    True
1    True
2    True
3    True
Name: col2, dtype: bool
df[(df['col2']>2) & (df['col2']==444)]
   col1  col2 col3
0     1   444  abc
3     4   444  xyz
def times2(x):
    return x*2

df['col1'].sum()
10
df['col1'].apply(times2)
0    2
1    4
2    6
3    8
Name: col1, dtype: int64
df['col3']
0    abc
1    def
2    ghi
3    xyz
Name: col3, dtype: object
df['col3'].apply(len)
0    3
1    3
2    3
3    3
Name: col3, dtype: int64
df['col3'].apply(lambda x: x*2)
0    abcabc
1    defdef
2    ghighi
3    xyzxyz
Name: col3, dtype: object
df['col2'].apply(lambda x: x*2)
0     888
1    1110
2    1332
3     888
Name: col2, dtype: int64
df.columns
Index(['col1', 'col2', 'col3'], dtype='object')
df.index
RangeIndex(start=0, stop=4, step=1)
df
   col1  col2 col3
0     1   444  abc
1     2   555  def
2     3   666  ghi
3     4   444  xyz
df.sort_values(by='col2')
   col1  col2 col3
0     1   444  abc
3     4   444  xyz
1     2   555  def
2     3   666  ghi
df.isnull()
    col1   col2   col3
0  False  False  False
1  False  False  False
2  False  False  False
3  False  False  False
data = {'A':['foo', 'foo', 'foo', 'bar', 'bar', 'bar'], 'B':['one','one','two','two','one', 'one'], 'C':['x','y','x','y','x','y'], 'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
df
     A    B  C  D
0  foo  one  x  1
1  foo  one  y  3
2  foo  two  x  2
3  bar  two  y  5
4  bar  one  x  4
5  bar  one  y  1
df.pivot_table()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    df.pivot_table()
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\frame.py", line 8044, in pivot_table
    return pivot_table(
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\reshape\pivot.py", line 95, in pivot_table
    table = __internal_pivot_table(
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\reshape\pivot.py", line 164, in __internal_pivot_table
    grouped = data.groupby(keys, observed=observed, sort=sort)
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\frame.py", line 7718, in groupby
    return DataFrameGroupBy(
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\groupby\groupby.py", line 882, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\groupby\grouper.py", line 910, in get_grouper
    raise ValueError("No group keys passed!")
ValueError: No group keys passed!
df.pivot_table(values = 'D',index=['A','B'],columns=['C'])
C          x    y
A   B            
bar one  4.0  1.0
    two  NaN  5.0
foo one  1.0  3.0
    two  2.0  NaN
