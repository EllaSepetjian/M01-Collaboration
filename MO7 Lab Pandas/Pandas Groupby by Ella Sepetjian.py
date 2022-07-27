Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Pandas - Groupby by Ella Sepetjian
import numpy as np
import pandas as pd
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
df
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
df.groupby('Company')
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000021CD0D75FF0>
byComp = df.groupby('Company')
byComp
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000021CD0D76050>
byComp.mean()
         Sales
Company       
FB       296.5
GOOG     160.0
MSFT     232.0
byComp.sum()
         Sales
Company       
FB         593
GOOG       320
MSFT       464
byComp.std()
              Sales
Company            
FB        75.660426
GOOG      56.568542
MSFT     152.735065
byComp.sum().loc['FB']
Sales    593
Name: FB, dtype: int64
df.groupby('Company').sum().loc['FB']
Sales    593
Name: FB, dtype: int64
df.groupby('Company').count()
         Person  Sales
Company               
FB            2      2
GOOG          2      2
MSFT          2      2
df.groupby('Company').max()
          Person  Sales
Company                
FB         Sarah    350
GOOG         Sam    200
MSFT     Vanessa    340
df.groupby('Company').min()
          Person  Sales
Company                
FB          Carl    243
GOOG     Charlie    120
MSFT         Amy    124
df.groupby('Company').describe()
        Sales                                                        
        count   mean         std    min     25%    50%     75%    max
Company                                                              
FB        2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0
GOOG      2.0  160.0   56.568542  120.0  140.00  160.0  180.00  200.0
MSFT      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0
df.groupby('Company').describe().transpose()
Company              FB        GOOG        MSFT
Sales count    2.000000    2.000000    2.000000
      mean   296.500000  160.000000  232.000000
      std     75.660426   56.568542  152.735065
      min    243.000000  120.000000  124.000000
      25%    269.750000  140.000000  178.000000
      50%    296.500000  160.000000  232.000000
      75%    323.250000  180.000000  286.000000
      max    350.000000  200.000000  340.000000
df.groupby('Company').describe().transpose()['FB']
Sales  count      2.000000
       mean     296.500000
       std       75.660426
       min      243.000000
       25%      269.750000
       50%      296.500000
       75%      323.250000
       max      350.000000
Name: FB, dtype: float64
