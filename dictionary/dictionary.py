import json
from difflib import get_close_matches

data = json.load(open("../dictionary/data.json"))

def translate(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif word.capitalize() in data:
    return data[word.capitalize()]
  elif word.upper() in data:
    return data[word.upper()]
  elif len(get_close_matches(word, data.keys())) > 0:
    close_match_list = get_close_matches(word, data.keys(), 3)
    print("Do you mean?")
    [print("%s) %s"%(i, a)) for i, a in enumerate(close_match_list)]
    print("3) something else")
    choose = input("Choose option:")
    if choose in ["0", "1", "2"]:
      return data[close_match_list[int(choose)]]
    elif choose == "3":
      return "Something else... Sorry hear that. Try again"
    else:
      return "Invalid input. Try again"
  else:
    return "The word doesn't exist"

word = input('Give me word:')

output = translate(word)

if type(output) ==list:
  [print("%s) %s"%(i, a)) for i, a in enumerate(output)]
else:
  print(output)