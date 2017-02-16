# Code that transliterates Latin to Cyrillic based on context, etc.

# Program asks for input text in transliterated Russian, including soft and hard signs, if present.

# The program goes through the text replacing each letter with its correct Cyrillic equivalent. In ambiguous cases, the program makes educated guesses based on context, and sometimes asks the user what Cyrillic letter was meant.

# The program then goes through to correct errors in the transliterated Cyrillic that do not correspond to correct Russian orthography, e.g. йа ---> я, цх ---> ч etc. Sometimes it may ask the user for clarification as of to the Cyrillic letter that was meant.

import re # Used to do a case insensitive search

# Some of the mappings below were inspired by http://translit.cc

mapping = {
  "a"    : "а",
  "b"    : "б",
  "c"    : "ц",
  "d"    : "д",
  "e"    : "е",
  "f"    : "ф",
  "g"    : "г",
  "h"    : "х",
  "i"    : "и",
  "j"    : "й",
  "k"    : "к",
  "l"    : "л",
  "m"    : "м",
  "n"    : "н",
  "o"    : "о",
  "p"    : "п",
  "q"    : "", # "q" can't map to much...
  "r"    : "р",
  "s"    : "с",
  "t"    : "т",
  "u"    : "у",
  "v"    : "в",
  "w"    : "в", # "w" is the same as "v"
  "x"    : "х", # They look the same but there is nothing "x" can map to..
  "y"    : "ы",
  "z"    : "з",
  "'"    : "ь",
  '"'    : "ъ",
  "''"   : "Ь", # Uppercase
  '""'   : "Ъ", # Uppercase
  "jo"   : "ё",
  "yo"   : "ё",
  "ya"   : "я",
  "zh"   : "ж",
  "sh"   : "ш",
  "shh"  : "щ",
  "shch" : "щ"
}

# We should do the longest sequences first
keys = sorted(mapping.keys(), key=lambda item: -len(item))

# Let's define our function

def eng_to_ru(english):
  for key in keys:
    english = english.replace(key, mapping[key]) # lower => lower
    english = english.replace(key.upper(), mapping[key].upper()) # CAPS => CAPS
    english = re.compile(key, re.IGNORECASE).sub(mapping[key], english) # MiXeD => lower
  return english

# Demonstartion of capabilities
print(eng_to_ru("privet"))
print(eng_to_ru("PrIvEt"))
print(eng_to_ru("Mne skol'koto let. Ponyatno?"))
print(eng_to_ru(input(eng_to_ru("Pozhaluysta, vvedite angliyskiy")))) # Testing user input
