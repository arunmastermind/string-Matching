import pandas as pd
import numpy as np
import difflib
names = ['test_name', 'build', 'failure']
df1 = pd.read_csv('result.csv', sep='~', names=names)

tests = np.sort(df1.test_name.unique())
builds = np.sort(df1.build.unique())
df2 = pd.DataFrame(index=tests, columns=builds)

def diference(case_a, case_b):
    output_list = [li for li in difflib.ndiff(case_a, case_b) if li[0] != ' ']
    return output_list

for test in tests:
    b = df1.where(df1.test_name == test)
    errors = list(b.failure.dropna())
    str1 = errors[0]
    ratio = []
    for error in errors:
        str2 = error
        try:
            ratio_result = diference(str1, str2)
        except:
            ratio_result = np.nan
        ratio.append((ratio_result))
    ratio = (ratio + [0] * 5)[:5] #padding zeros
    df2.loc[test] = ratio

print(df2)



# import os
# case_a = 'arUn'
# case_b = 'Arun'
# # b = os.system(f'diff {case_a} {case_b}')
# # print(b)
#
# print(output_list)