import pandas as pd
import string_matching_fuzzer as smf
import numpy as np
from difflib import SequenceMatcher

names = ['test_name', 'build', 'status', 'failure']
df1 = pd.read_csv('result.csv', sep='~', names=names)

tests = np.sort(df1.test_name.unique())
builds = np.sort(df1.build.unique())
# print(tests)
df2 = pd.DataFrame(index=tests, columns=builds)
df3 = pd.DataFrame(index=tests, columns=builds)

print(f'\n\n{"#"*30} FUZZER MATCHING RESULTS {"#"*30}')
# q = df1.where(df1.test_name == tests[0])
# errorss = list(q.failure.dropna())
# str1 = errorss[0]

for test in tests:
    b = df1.where(df1.test_name == test)
    errors = list(b.failure.dropna())
    str1 = errors[0]
    ratio = []
    for error in errors:
        str2 = error
        try:
            ratio_result = smf.stringMatingRatio(str1, str2)
        except:
            ratio_result = np.nan
        ratio.append((ratio_result))
    ratio = (ratio + [0] * len(builds))[:len(builds)] #padding zeros
    df2.loc[test] = ratio

print(df2)

print(f'\n\n{"#"*30} BASIC STRING MATCHING {"#"*30}')
for test in tests:
    b = df1.where(df1.test_name == test)
    errors = list(b.failure.dropna())
    str1 = errors[0]
    ratio = []
    for error in errors:
        str2 = error
        try:
            if str1 == str2:
                ratio_result = 100
            else:
                ratio_result = 0
        except:
            ratio_result = np.nan
        ratio.append((ratio_result))
    ratio = (ratio + [0] * len(builds))[:len(builds)]  # padding zeros
    df3.loc[test] = ratio

print(df3)
#
from pandas import ExcelWriter
from pandas import ExcelFile
# writer = ExcelWriter('StringMatching.xlsx')
writer = ExcelWriter('test.xlsx')
df2.to_excel(writer,'1')
df3.to_excel(writer,'2')
writer.save()