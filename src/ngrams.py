import string
import re
import sys
import os

class language:
    oneGram = {}
    twoGram = {}
    threeGram = {}

    def __init__(self, oneGram, twoGram, threeGram):
      self.oneGram = oneGram
      self.twoGram = twoGram
      self.threeGram = threeGram

def ngrams(input, n, output):
  if (input == ''):
    return output
  input = input.split(' ')
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output

# output = {}
# for i in range(3):
#     print(ngrams("salut ça va? je vais, bien? \n salut. ça va et toi ?", i, output))
# print()
# for i in range(3):
#     print(ngrams("salut ça. va je vais bien? \n salut ça va. et toi?", i, output))


def parseLanguage(dirname):
    lang = language({}, {}, {})
    for filename in os.listdir(dirname):
        print(filename + '\n')
        file = open(dirname + filename, 'r')
        i = 0
        for line in file:
            lang.oneGram = ngrams(line, 1, lang.oneGram)
            lang.twoGram = ngrams(line, 2, lang.twoGram)
            lang.threeGram = ngrams(line, 3, lang.threeGram)
            # because potato pc, taking only 20 lines
            if (i > 20):
                break
            i += 1
    return lang
