import pandas as pd
import string_matching_fuzzer as smf

names = ['test_name', 'build', 'status', 'failure']
df1 = pd.read_csv('result.csv', sep='~', names=names)
tests = df1.test_name.unique()
builds = df1.build.unique()
# print(df1['failure'])
for test in tests:
    b = df1.where(df1.test_name==test)
    print(f'\n\n{"#"*30} {test} {"#"*30}\n')
    # print(f'{b.failure.dropna()}')
    x = list(b.failure.dropna())
    str1 = x[0]
    for i in x:
        str2 = i
        ratio_result = smf.stringMatingRatio(str1, str2)
        print(f'STRING1: {str1[:100]}\nSTRING2: {str2[:100]}\nRATIO:{ratio_result}\n{" "*20}{"-"*50}')

#
# df2 = pd.DataFrame(index=tests, columns=builds)
# print(df2)