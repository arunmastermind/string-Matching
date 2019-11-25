##
from fuzzywuzzy import fuzz
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer
from itertools import product
from urllib.request import urlopen
import getAllTheFileWithAnExtention as gex
import numpy

# git clone git://github.com/seatgeek/fuzzywuzzy.git fuzzywuzzy
# cd fuzzywuzzy
# python setup.py install

#pip3 install fuzzywuzzy[speedup]
##
# str1 = 'abc is a good one'
# str2 = 'bc'
# print('-'*50)
# print(f'STRING 1: {str1}')
# print(f'STRING 2: {str2}')

##
dir = "data3"
filepath = f'./{dir}/'
extention = '.txt'
files = gex.getFiles(filepath, extention)
print('-'*50)
print(f' FILE NAMES: {files}')

##
def tokeniseString(str):
    filtered_sentence = []
    stop_words = set(stopwords.words("english"))
    for words in word_tokenize(str):
        if words not in stop_words:

            # if words.isalnum():
                # print(words)
            filtered_sentence.append(words)
    return filtered_sentence
##
# print(type(files[19]))
f1 = open(f'./{dir}/{files[0]}', 'r')
str1 = f1.read()
for file in files:
    with open(f'./{dir}/{file}', "r") as f:
        str2 = f.read()
        filtered_sentence1 = tokeniseString(str1)
        filtered_sentence2 = tokeniseString(str2)
        # print('-'*50)
        # print(f'TOKENIZED STRING 1: {filtered_sentence1}')
        # print(f'TOKENIZED STRING 2: {filtered_sentence2}')

        # if(len(filtered_sentence1) != len(filtered_sentence2)):
        #     # print('-' * 50)
        #     print(f"{file} failure doesn't matches")
        #     # exit()
        # else:
        #     print(f'{file} matched')

        a = fuzz.ratio(str1, str2)

        if a>60:
            print('-' * 50)
            print(f'RATIO:: {a}')
            print(f'{file} MATCHED')

f1.close()
##
# a = fuzz.ratio(str1, str2)
# print(a)

