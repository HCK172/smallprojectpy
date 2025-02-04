
import pprint

with open('context.txt', 'r') as file: 
    text = file.read()

characterCount = {}
wordCount = {}
for character in text : 
     characterCount.setdefault(character,0)
     characterCount[character] = characterCount[character] + 1

text = text.split(' ')
totalWordCount = len(text)

for word in text: 
     wordCount.setdefault(word, 0)
     wordCount[word] = wordCount[word] + 1 

print(len(totalWordCount))
pprint.pprint(characterCount)
print(pprint.pformat(wordCount))
