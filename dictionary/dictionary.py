import json

data = json.load(open("../dictionary/data.json"))

def translate(word):
  word = word.lower()
  if word in data:
    return data[word]
  else:
    return "The word doesn't exist"

word = input('Give me word:')

print(translate(word))
