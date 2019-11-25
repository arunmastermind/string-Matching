from fuzzywuzzy import fuzz

def stringMatingRatio(str1, str2):
    ratio = fuzz.ratio(str1, str2)
    return ratio

def pstringMatingRatio(str1, str2):
    ratio = fuzz.partial_ratio(str1, str2)
    return ratio