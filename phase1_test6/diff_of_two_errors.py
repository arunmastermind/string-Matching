import pandas as pd
import numpy as np
import difflib

names = ['test_name', 'build', 'status', 'failure']
df1 = pd.read_csv('result.csv', sep='~', names=names)

tests = np.sort(df1.test_name.unique())
builds = np.sort(df1.build.unique())

df2 = pd.DataFrame(index=tests, columns=builds)
df3 = pd.DataFrame(index=tests, columns=builds)

outfile = open( 'difftest.html', 'w' )
differ = difflib.HtmlDiff(tabsize=20, wrapcolumn=50)
differ._legend = ''
# print(f'\n\n{"#"*30} FUZZER MATCHING RESULTS {"#"*30}')

ratio_result  = 0
for test in tests:
    b = df1.where(df1.test_name == test)
    errors = list(b.failure.dropna())
    str1 = errors[0].split(' ')
    ratio = []
    for error in errors:
        str2 = error.split(' ')
        breaks = '='*50
        try:
            html = '<br><br>' + test + '<br>' +(differ.make_file(str1, str2, context=True)) + breaks
            if 'No Differences Found' in html:
                continue
            outfile.write(html)
        except:
            pass
outfile.close()