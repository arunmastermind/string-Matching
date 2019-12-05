import re

def getOutput(str1):
    splitString = str1.split(r'#')
    for i in splitString:
        # print(f'{i}\n{"*" * 20}')
        stripedString = i.replace('\n', "")
        # print(f'{stripedString}\n{"*" * 20}')
        out = re.match('output:out2(.*)', stripedString)
        # print(f'{out}\n{"*" * 20}')
        if out:
            # print(f'{out.groups()}\n{"*" * 20}')
            return i
        # else:
        #     return 0