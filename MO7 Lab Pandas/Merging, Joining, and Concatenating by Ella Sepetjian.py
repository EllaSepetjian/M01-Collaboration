Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Merging, Joining, and Concatenating by Ella Sepetjian
import pandas as pd
df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']},index = [0,1,2,3])
df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],'B':['B4','B5','B6','B7'],'C':['C4','C5','C6','C7'],'D':['D4','D5','D6','D7']},index = [4,5,6,7])
df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],'B':['B8','B9','B10','B11'],'C':['C8','C9','C10','C11'],'D':['D8','D9','D10','D11']},index = [8,9,10,11])
df1
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
df2
    A   B   C   D
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
df3
      A    B    C    D
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
pd.concat([df1,df2,df3])
      A    B    C    D
0    A0   B0   C0   D0
1    A1   B1   C1   D1
2    A2   B2   C2   D2
3    A3   B3   C3   D3
4    A4   B4   C4   D4
5    A5   B5   C5   D5
6    A6   B6   C6   D6
7    A7   B7   C7   D7
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
pd.concat([df1,df2,df3], axis = 1)
      A    B    C    D    A    B    C    D    A    B    C    D
0    A0   B0   C0   D0  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
1    A1   B1   C1   D1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
2    A2   B2   C2   D2  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
3    A3   B3   C3   D3  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
4   NaN  NaN  NaN  NaN   A4   B4   C4   D4  NaN  NaN  NaN  NaN
5   NaN  NaN  NaN  NaN   A5   B5   C5   D5  NaN  NaN  NaN  NaN
6   NaN  NaN  NaN  NaN   A6   B6   C6   D6  NaN  NaN  NaN  NaN
7   NaN  NaN  NaN  NaN   A7   B7   C7   D7  NaN  NaN  NaN  NaN
8   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A8   B8   C8   D8
9   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A9   B9   C9   D9
10  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A10  B10  C10  D10
11  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A11  B11  C11  D11
left = pd.DataFrame({'Key':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'Key':['K0','K1','K2','K3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
left
  Key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
right
  Key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
pd.merge(left,right,how = 'inner',on = 'key')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pd.merge(left,right,how = 'inner',on = 'key')
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\reshape\merge.py", line 107, in merge
    op = _MergeOperation(
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\reshape\merge.py", line 700, in __init__
    ) = self._get_merge_keys()
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\reshape\merge.py", line 1097, in _get_merge_keys
    right_keys.append(right._get_label_or_level_values(rk))
  File "C:\Users\ellas\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\generic.py", line 1840, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'key'
pd.merge(left,right,how = 'inner',on = 'Key')
  Key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
left = pd.DataFrame({'Key1':['K0','K0','K1','K2'],'Key2':['K0','K1','K0','K1'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'Key1':['K0','K1','K1','K2'],'Key2':['K0','K0','K0','K0'],,'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
SyntaxError: invalid syntax
right = pd.DataFrame({'Key1':['K0','K1','K1','K2'],'Key2':['K0','K0','K0','K0'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
pd.merge(left, right, on = ['Key1', 'Key2'])
  Key1 Key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
pd.merge(left,right,how = 'outer',on = ['Key1', 'Key2'])
  Key1 Key2    A    B    C    D
0   K0   K0   A0   B0   C0   D0
1   K0   K1   A1   B1  NaN  NaN
2   K1   K0   A2   B2   C1   D1
3   K1   K0   A2   B2   C2   D2
4   K2   K1   A3   B3  NaN  NaN
5   K2   K0  NaN  NaN   C3   D3
pd.merge(left,right,how = 'right',on = ['Key1', 'Key2'])
  Key1 Key2    A    B   C   D
0   K0   K0   A0   B0  C0  D0
1   K1   K0   A2   B2  C1  D1
2   K1   K0   A2   B2  C2  D2
3   K2   K0  NaN  NaN  C3  D3
pd.merge(left,right,how = 'left',on = ['Key1', 'Key2'])
  Key1 Key2   A   B    C    D
0   K0   K0  A0  B0   C0   D0
1   K0   K1  A1  B1  NaN  NaN
2   K1   K0  A2  B2   C1   D1
3   K1   K0  A2  B2   C2   D2
4   K2   K1  A3  B3  NaN  NaN
left = pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2'],index = ['K0','K1','K2'])
                    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
left = pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2']},index = ['K0','K1','K2'])
                    
right = pd.DataFrame({'C':['C0','C2','C3'],'D':['D0','D2','D3']},index = ['K0','K2','K3'])
                    
left.join(right)
                    
     A   B    C    D
K0  A0  B0   C0   D0
K1  A1  B1  NaN  NaN
K2  A2  B2   C2   D2
left.join(right, how = 'outer')
                    
      A    B    C    D
K0   A0   B0   C0   D0
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3  NaN  NaN   C3   D3
