import numpy as np
import datetime as dt
import pandas as pd

days = np.busday_count(('2021-02-01', '2021-03-01', '2021-04-01'), 
                        ('2021-03-01', '2021-04-01','2021-05-01'), 
                        weekmask='1111100')
data = {'year': [2021, 2021, 2021], 
        'month': ['february', 'march', 'april']} 
 
df = pd.DataFrame(data)
 
df.insert(2, "work_day", days) 

print(df)
