import numpy as np
import pandas as pd

var = pd.Series(np.random.randn(5))

df = pd.DataFrame(var, columns = ['Column 1'])
df['Column 2'] = df['Column 1'] * 4
df['Column 3'] = 'Active'
print(df)ch