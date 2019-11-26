import pandas as pd
import string_matching_fuzzer as smf
import numpy as np
from difflib import SequenceMatcher

names = ['test_name', 'build', 'status', 'failure']
df1 = pd.read_csv('result.csv', sep='~', names=names)

tests = np.sort(df1.test_name.unique())
builds = np.sort(df1.build.unique())
# print(builds)
df2 = pd.DataFrame(index=tests, columns=builds)
df3 = pd.DataFrame(index=tests, columns=builds)
for i in range(0,218):
    print(f'\n\n{"#"*30} FUZZER MATCHING RESULTS {"#"*30}')
    q = df1.where(df1.test_name == tests[i])
    errorss = list(q.failure.dropna())
    str1 = errorss[0]

    for test in tests:
        b = df1.where(df1.test_name == test)
        errors = list(b.failure.dropna())
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

    # print(df2)
    hundred                 = df2.index[df2[builds[0]] == 100].tolist()
    nintyFive_to_hundred    = df2.index[(df2[builds[0]] > 95) & (df2[builds[0]] < 100)].tolist()
    ninty_to_nintyFive      = df2.index[(df2[builds[0]] > 90) & (df2[builds[0]] < 95)].tolist()
    eightyFive_to_ninty     = df2.index[(df2[builds[0]] > 85) & (df2[builds[0]] < 90)].tolist()
    eighty_to_eightyFive    = df2.index[(df2[builds[0]] > 80) & (df2[builds[0]] < 85)].tolist()
    fifty_to_eighty         = df2.index[(df2[builds[0]] > 50) & (df2[builds[0]] < 85)].tolist()
    less_than_fifty         = df2.index[(df2[builds[0]] < 50)].tolist()

    # print(f'hundred:: {hundred}')
    # print(f'ninty:: {nintyFive_to_hundred}')
    # print(ninty_to_nintyFive)
    # print(eightyFive_to_ninty)
    # print(eighty_to_eightyFive)
    # print(fifty_to_eighty)
    # print(less_than_fifty)

    df3 =  pd.DataFrame(columns=['hundred', 'nintyFive_to_hundred', 'ninty_to_nintyFive', 'eightyFive_to_ninty', 'eighty_to_eightyFive', 'fifty_to_eighty', 'less_than_fifty'])

    # (ratio + [0] * len(builds))[:len(builds)]

    df3['hundred']                  = (hundred + [0] * 200)[:200]
    df3['nintyFive_to_hundred']     = (nintyFive_to_hundred + [0] * 200)[:200]
    df3['ninty_to_nintyFive']       = (ninty_to_nintyFive + [0] * 200)[:200]
    df3['eightyFive_to_ninty']      = (eightyFive_to_ninty + [0] * 200)[:200]
    df3['eighty_to_eightyFive']     = (eighty_to_eightyFive + [0] * 200)[:200]
    df3['fifty_to_eighty']          = (fifty_to_eighty + [0] * 200)[:200]
    df3['less_than_fifty']          = (less_than_fifty + [0] * 200)[:200]

    print(df3)

    import pandas as pd
    import numpy as np
    from openpyxl import load_workbook
    # import pandas.core.format

    file = r"matchGrid_with_breakdown.xlsx"
    try:
        book = load_workbook(file)
        writer = pd.ExcelWriter(file)
        writer.book = book
    except:
        writer = pd.ExcelWriter(file)

    df2.to_excel(writer, sheet_name=str(i))
    df3.to_excel(writer, sheet_name=str(i), startrow=220)
    writer.save()
    writer.close()

