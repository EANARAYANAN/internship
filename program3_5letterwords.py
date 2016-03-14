import re
parag=raw_input("Enter the paragraph")
word1=re.findall(r"[\w']+|[.,!?;]", parag )
word2=[]
for item in word1:
	if len(item)>5:
		word2.append(item)
print word2
