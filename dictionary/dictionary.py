import json

data = json.load(open("../dictionary/data.json"))

def translate(word):
  if word in data:
    return data[word]
  else:
    return "The word doesn't exist"

print(translate("rain"))
print(translate("Noga"))