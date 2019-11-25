from fuzzywuzzy import fuzz
from urllib.request import urlopen
link1 = "http://release.azulsystems.com/home/qatest/JCK_13/UNS/get_output.php?object_id=5d9708a09df3c6a8e4283266"
link2 = "http://release.azulsystems.com/home/qatest/JCK_13/UNS/get_output.php?object_id=5d9708a09df3c6a8e4283266"
# link2 = "http://release.azulsystems.com/home/qatest/JCK_13/UNS/get_output.php?object_id=5d9708a09df3c6a8e4283273"
f1 = urlopen(link1)
f2 = urlopen(link2)
str1 = f1.read().decode('utf-8')
str2 = f2.read().decode('utf-8')
a = fuzz.ratio(str1, str2)
print(a)