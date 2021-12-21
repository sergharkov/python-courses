sentence0 = "Some random sentence"
sentence=sentence0
# write your program here  
from collections import Counter
sentence = sentence.lower()
sentence = sentence.split()
print(Counter(sentence))

#shoterest
sentence2=sentence0
print(Counter(sentence2.lower().split()))
