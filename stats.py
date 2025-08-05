from itertools import *

def get_num_words(filepath):
    with open(filepath) as f:
        words = f.read().split()
        #print(words)
#        print(f"{len(words)} words found in the document")
    
        return words

def get_num_chars(words):
    chars = {}
    wordNo = 0
    for word in words:
      wordNo += 1
      for i in word:
        lowered = i.lower()
        if chars.get(lowered):
            chars[lowered]["num"] += 1
        else:
            chars[lowered] = {
                "num":1,
                "char":lowered
            }
    return chars, wordNo

def get_sorted_num_chars(chars):
    li = list(chars.values())
    li.sort(reverse = True, key=sort_on)
    return li

def sort_on(items):
    return items["num"]