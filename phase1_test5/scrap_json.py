import pandas as pd
import json
import numpy as np
from pandas.io.json import json_normalize
import pprint
import string_matching_fuzzer as smf
import scrape_output as so

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

# df1 = pd.DataFrame(results1['known'])
# df2 = pd.DataFrame(results1['known'])
# df3 = pd.DataFrame(results1['known'])

joined_df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(joined_df.columns)
for i in range(1001):
    # print(joined_df.loc[i]['output'])
    # print(so.getOutput(joined_df.loc[i]['output']))
    try:
        str11 = (joined_df.loc[i]['output'])
        str1 = so.getOutput(joined_df.loc[i]['output'])
        # print(str1)
        # print(f'{"#"*25}\n{joined_df.loc[i]["test"]}\n{joined_df.loc[i]["jira_id"]}')
        if str1 is not 0:
            for j in range(100):
                # print(joined_df.loc[j]['output'])
                str21 = (joined_df.loc[j]['output'])
                str2 = so.getOutput(joined_df.loc[j]['output'])
                if str2 is not 0:
                    ratio_result = smf.stringMatingRatio(str1, str2)

                    # print(f'\n{"*"*50}\nstr1 :: {str1}\n str2 :: {str2}\n')
                    # print(ratio_result)
                    if ratio_result > 95:
                        print(
                            f'\n{joined_df.loc[i]["_id"]}\n{ratio_result}\n{joined_df.loc[i]["test"]}\nTEST: {joined_df.loc[j]["test"]}\n')
                    # if ratio_result > 95:
                    #     # print(ratio_result)
                    #     print(f'\n{joined_df.loc[i]["_id"]}\n{ratio_result}\n{joined_df.loc[i]["test"]}\nTEST: {joined_df.loc[j]["test"]}\njiraID: {joined_df.loc[j]["jira_id"]}\n')

    except:
        pass


# for i in range(100):
#     try:
#         print(joined_df.loc[i]['jira_id'])
#     except:
#         pass