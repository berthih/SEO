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

class gramOccurence:
    str = ""
    value = 0
    nbOccurence = 0

    def __init__(self, str, value, occurence):
        self.str = str
        self.nbOccurence = occurence
        self.value = value

def ngrams(input, n, output):
  if (input == ''):
    return output
  input = input.split(' ')
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output

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
            if (i > 10000):
                break
            i += 1
    return lang


