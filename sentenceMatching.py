from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer
from itertools import product
import numpy
from urllib.request import urlopen
########################### Various test strings ##########################
#str1 = "Hi, how are you?"
#str2 = "Hi, are you fine?"

# str1 = "Arun is a student"
# str2 = "Arun is studying"

# str1 = "Cat is drinking tea."
# str2 = "Lions eat fruit."

# str1 = "Arun is a good boy."
# str2 = "Arun is a very good boy."

# str1 = "He loves to play cricket."
# str2 = "cricket is his favourite sport."

# str1 = "I was given a pen by her in the garden."
# str2 = "In the garden, she gave me a pen."

######################## Strig from error/Failure ####################################

link1 = "http://release.azulsystems.com/home/qatest/JCK_13/UNS/get_output.php?object_id=5d9708a09df3c6a8e4283266"
#link2 = "http://release.azulsystems.com/home/qatest/JCK_13/UNS/get_output.php?object_id=5d9708a09df3c6a8e4283266"
link2 = "http://release.azulsystems.com/home/qatest/JCK_13/UNS/get_output.php?object_id=5d9708a09df3c6a8e4283273"
f1 = urlopen(link1)
f2 = urlopen(link2)
str1 = f1.read().decode('utf-8')
str2 = f2.read().decode('utf-8')

###########################################################
stop_words = set(stopwords.words("english"))

filtered_sentence1 = []
filtered_sentence2 = []
lemm_sentence1 = []
lemm_sentence2 = []
sims = []
temp1 = []
temp2 = []
simi = []
final = []
same_sent1 = []
same_sent2 = []

lemmatizer  =  WordNetLemmatizer()

for words1 in word_tokenize(str1):
    if words1 not in stop_words:
        if words1.isalnum():
            filtered_sentence1.append(words1)

for i in filtered_sentence1:
    lemm_sentence1.append(lemmatizer.lemmatize(i))

for words2 in word_tokenize(str2):
    if words2 not in stop_words:
        if words2.isalnum():
            filtered_sentence2.append(words2)

for i in filtered_sentence2:
    lemm_sentence2.append(lemmatizer.lemmatize(i))

for word1 in lemm_sentence1:
    simi =[]
    for word2 in lemm_sentence2:
        sims = []
        syns1 = wordnet.synsets(word1)
        syns2 = wordnet.synsets(word2)
        for sense1, sense2 in product(syns1, syns2):
            d = wordnet.wup_similarity(sense1, sense2)
            if d != None:
                sims.append(d)

        if sims != []:        
           max_sim = max(sims)
           simi.append(max_sim)
             
    if simi != []:
        max_final = max(simi)
        final.append(max_final)

similarity_index = numpy.mean(final)
similarity_index = round(similarity_index , 2)
print("ORIGINAL Sentence 1: ",str1)
print("ORIGINAL Sentence 2: ",str2)

print("ARRAY Sentence 1: ",lemm_sentence1)
print("ARRAY Sentence 2: ",lemm_sentence2)

print("Similarity index value : ", similarity_index)

if similarity_index>0.8:
    print("Similar")
elif similarity_index>=0.6:
    print("Somewhat Similar")
else:
    print("Not Similar")
