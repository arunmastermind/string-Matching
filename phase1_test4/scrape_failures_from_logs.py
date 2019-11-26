import pandas as pd
import numpy as np
import pprint
import getAllTheFileWithAnExtention as gg
import re
# str = "--------------------------------------------------"
# print(len(str))
files = gg.getFiles('./data/', '.log')
# files = ['output_1.log', 'output_2.log']
with open('result.csv', 'w') as result_file:
    for file in files:
        print('#'*50)
        file = f'./data/{file}'
        with open(file, 'r') as test:
            text = (test.read())
        text = text.replace("\n", " ")
        tests = text.split('-'*50)

        for test in tests:
            test_name = re.search('TEST:(.*)TEST JDK', test)
            regex = re.compile(r"STDOUT", flags=re.I)
            try:
                main_err = regex.split(test)
                error_string = main_err[-1]
                error = re.search(':(.*)STATUS:(.*)rerun:', error_string)
                failure = f'STDOUT:{error.group(1)}'
                status = error.group(2)
                if 'Failed.' in status.strip():
                    print('-' * 50)
                    # print(file)
                    # print(test_name.group(1).strip())
                    test_name = test_name.group(1).strip()
                    # print(failure.strip())
                    failure = failure.strip()
                    print(status.strip())
                    status = status.strip()
                    a = f'{test_name} ~ {file} ~ {status} ~ {failure}\n'
                    print(a)
                    result_file.write(a)
            except:
                pass
