import pandas as pd
import json
import numpy as np
from pandas.io.json import json_normalize
import pprint

dir = './data/'
file = 'log1.json'
log = f'{dir}{file}'

df = pd.read_json(log)
results1 = (df.loc['JCK-runtime-13']['results'])
results2 = (df.loc['JCK-runtime-11']['results'])
results3 = (df.loc['JCK-runtime-7']['results'])

df1 = pd.DataFrame(results1['unexpected'])
df2 = pd.DataFrame(results1['unexpected'])
df3 = pd.DataFrame(results1['unexpected'])

joined_df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(joined_df)

for i in range(477):
    print(joined_df.loc[i]['output'])