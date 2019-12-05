import pandas as pd
import string_matching_fuzzer as smf
import numpy as np

names = ['test_name', 'build', 'status', 'failure']
df1 = pd.read_csv('result.csv', sep='~', names=names)

tests = np.sort(df1.test_name.unique())
builds = np.sort(df1.build.unique())

df2 = pd.DataFrame(index=tests, columns=builds)
df3 = pd.DataFrame(index=tests, columns=builds)

for i in range(0,700):
    try:
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
            ratio = (ratio + [0] * len(builds))[:len(builds)]
            df2.loc[test] = ratio

        hundred                 = [tests[i]]
        nintyFive_to_hundred    = df2.index[(df2[builds[0]] > 95) & (df2[builds[0]] < 100)].tolist()

        df3 =  pd.DataFrame(columns=['test', 'nintyFive_to_hundred'])

        df3['test']                  = (hundred + [0] * len(nintyFive_to_hundred))[:len(nintyFive_to_hundred)]
        df3['nintyFive_to_hundred']     = nintyFive_to_hundred

        if df3.empty:
            continue
        print(df3)

        # import pandas as pd
        # import numpy as np
        # from openpyxl import load_workbook
        #
        # file = r"ninetyFive_to_hundred.xlsx"
        # try:
        #     book = load_workbook(file)
        #     writer = pd.ExcelWriter(file)
        #     writer.book = book
        # except:
        #     writer = pd.ExcelWriter(file)
        #
        # df3.to_excel(writer, startrow=len(df3)+2, index=False)
        # writer.save()
        # writer.close()
    except:
        pass

