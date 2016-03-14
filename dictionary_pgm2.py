import re
parag=raw_input("Enter the paragraph")
word1=re.findall(r"[\w']+|[.,!?;]", parag )
dict={}
for word in word1:
    try:
    	dict[word] += 1
    except KeyError:
    	dict[word] = 1
print (dict)
