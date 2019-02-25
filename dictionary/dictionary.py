import json

data = json.load(open("../dictionary/data.json"))

def translate(word):
  return data[word]

print(translate("rain"))