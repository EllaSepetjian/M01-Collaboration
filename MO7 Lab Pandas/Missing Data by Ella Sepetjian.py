Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Missing Data by Ella Sepetjian
import numpy as np
import pandas as pd
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
df
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
df.dropna()
     A    B  C
0  1.0  5.0  1
df.dropna(axis =1)
   C
0  1
1  2
2  3
df.dropna(thresh = 2)
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
df.fillna(value ='FILL VALUE')
            A           B  C
0         1.0         5.0  1
1         2.0  FILL VALUE  2
2  FILL VALUE  FILL VALUE  3
df['A'].fillna(value=df['A'].mean())
0    1.0
1    2.0
2    1.5
Name: A, dtype: float64
