import collections
from collections import Counter
from collections import OrderedDict
code=input("Enter text: ")
if len(code)>500:
    print("Only 500 characters accepted")
else:
    cnt = Counter(code)
    od = OrderedDict(cnt.most_common())
    print("\nRepeated Characters:")
    sum=0
    for key, value in sorted(od.items(),reverse=True):
        print(key,":", value)
        if(od[key]>1):
            sum+=1
    print("Total repeating characters =",sum)
    words = code.split()
    word_counts = collections.Counter(words)
    print("\nRepeated Words:")
    wordrem=""
    wordadd=""
    resultadd=""
    sum=0
    for word, count in sorted(word_counts.items(),reverse=True):
        print('%s : %d' % (word, count))
        if(word_counts[word]>1):
            sum+=1
        wordrem+=" "+''.join([i for i in word if word_counts[word]>5])
        resultrem = ' '.join([i for i in words if i not in wordrem])
        wordadd+=" "+''.join([i for i in word if word_counts[word]!=1])
        if len(resultadd)<=500:
            resultadd = ' '.join([i for i in words if i not in wordadd])
    print("Total repeating words =",sum)
    print("The string without duplicate entries more than 5 is: ",resultrem)
    print("The string with adding the words occuring once is: ",resultrem+" "+resultadd)
