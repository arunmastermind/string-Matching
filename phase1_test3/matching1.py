from fuzzywuzzy import fuzz
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords,wordnet
import getAllTheFileWithAnExtention as gex

dir = "data3"
filepath = f'./{dir}/'
extention = '.txt'
files = gex.getFiles(filepath, extention)
print('-'*50)
print(f' FILE NAMES: {files}')

def tokeniseString(str):
    filtered_sentence = []
    stop_words = set(stopwords.words("english"))
    for words in word_tokenize(str):
        if words not in stop_words:
            filtered_sentence.append(words)
    return filtered_sentence

    filtered_sentence1 = tokeniseString(str1)
    filtered_sentence2 = tokeniseString(str2)
    a = fuzz.ratio(str1, str2)
    if a>60:
        print('-' * 50)
        print(f'RATIO:: {a}')
        print(f'{file} MATCHED')



