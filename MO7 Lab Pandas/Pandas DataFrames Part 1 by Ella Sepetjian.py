Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
df
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
df['W']
A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64
type(df['W'])
<class 'pandas.core.series.Series'>
type(df)
<class 'pandas.core.frame.DataFrame'>
df.W
A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64
df[['W', 'Z']]
          W         Z
A  2.706850  0.503826
B  0.651118  0.605965
C -2.018168 -0.589001
D  0.188695  0.955057
E  0.190794  0.683509
df['new']
Traceback (most recent call last):
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py", line 3621, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 136, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 163, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'new'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df['new']
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\frame.py", line 3505, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py", line 3623, in get_loc
    raise KeyError(key) from err
KeyError: 'new'
df['new'] = df['W'] + df['Y']
df
          W         X         Y         Z       new
A  2.706850  0.628133  0.907969  0.503826  3.614819
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959
C -2.018168  0.740122  0.528813 -0.589001 -1.489355
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542
E  0.190794  1.978757  2.605967  0.683509  2.796762
df.drop('new')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df.drop('new')
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\frame.py", line 4954, in drop
    return super().drop(
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\generic.py", line 4267, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\generic.py", line 4311, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py", line 6644, in drop
    raise KeyError(f"{list(labels[mask])} not found in axis")
KeyError: "['new'] not found in axis"
df.drop('new', axis = 1)
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
df
          W         X         Y         Z       new
A  2.706850  0.628133  0.907969  0.503826  3.614819
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959
C -2.018168  0.740122  0.528813 -0.589001 -1.489355
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542
E  0.190794  1.978757  2.605967  0.683509  2.796762
df.drop('new', axis = 1, inplace = True)
df
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
df.drop('E')
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
df.shape
(5, 4)
df
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
df.loc['A']
  
W    2.706850
X    0.628133
Y    0.907969
Z    0.503826
Name: A, dtype: float64
df.iloc[2]
W   -2.018168
X    0.740122
Y    0.528813
Z   -0.589001
Name: C, dtype: float64
df.loc['B', 'Y']
-0.8480769834036315
df.loc[['A', 'B'], ['W', 'Y']]
          W         Y
A  2.706850  0.907969
B  0.651118 -0.848077
