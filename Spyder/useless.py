import pandas as pd
c11=pd.Series(data=[50,30,70], index=['Science', 'Commerce', 'Humanities'])
c12=pd.Series(data=[77,54,75], index=['Science', 'Commerce', 'Humanities'])
print("Total no. of students")
print(c11+c12)
