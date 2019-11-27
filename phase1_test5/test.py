import pandas as pd
a = [1,2,3,4,5]
b = [2,4,6,8,0]
df1 = pd.DataFrame(a)

df2 = pd.DataFrame(b)

df_concat = pd.concat([df1, df2], axis=0)

print(df_concat)