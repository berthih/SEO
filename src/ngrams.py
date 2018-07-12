import string
import re
import sys
import os
from itertools import islice


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


# return the n-gram of a string
def ngrams(input, n, output):
  if (input == ''):
    return output
  input = input.split(' ')
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output


# return the 1-gram, 2-gram and 3-gram of all the files in a directory (that represents a language)
def parseLanguage(dirname):
    lang = language({}, {}, {})
    for filename in os.listdir(dirname):
        file = open(dirname + filename, 'r')
        lang = parseFile(file, lang)
    return lang


def parseFile(file, lang):
    i = 0
    for line in file:
        lang.oneGram = ngrams(line, 1, lang.oneGram)
        lang.twoGram = ngrams(line, 2, lang.twoGram)
        lang.threeGram = ngrams(line, 3, lang.threeGram)
        # because potato pc, taking only 20 lines
        if (i > 50000):
            break
        i += 1
    return lang


# count occurence given a directory and a n-gram
def countOccur(dirname, ngram):
    occurList = []
    for elt in ngram:
        occur = 0
        for filename in os.listdir(dirname):
            with open(dirname + filename, 'r') as myfile:
                head = list(islice(myfile, 10000))
            if elt[0] in ''.join(head):
                occur += 1
        occurList.append(gramOccurence(elt[0], elt[1], occur))
        # update value as tf-idf?
    return occurList


def detectLanguage(text, fr1, fr2, fr3, de1, de2, de3, en1, en2, en3):
    countfr = 0
    counten = 0
    countde = 0
    for i in text.oneGram:
        if i in fr1:
            print(i)
            countfr += 1
        if i in en1:
            print(i)
            counten += 1
        if i in de1:
            print(i)
            countde += 1
        #search in french, english and deutch one gram and return the highest rate
    for i in text.twoGram:
        if i in fr2:
            print(i)
            countfr += 2
        if i in en2:
            print(i)
            counten += 2
        if i in de2:
            print(i)
            countde += 2
        # search in french, english and deutch two gram and return the highest rate
    for i in text.threeGram:
        if i in fr3:
            countfr += 3
        if i in en3:
            print(i)
            counten += 3
        if i in de3:
            print(i)
            countde += 3
        # search in french, english and deutch three gram and return the highest rate
    print("fr:", countfr, "en:", counten, "de:", countde)
    lang = max(countde, counten, countfr)
    if lang == countfr:
        return fr1, fr2, fr3
    if lang == countde:
        return de1, de2, de3
    if lang == counten:
        return en1, en2, en3
    #compare all rates and return langage detected

def predictWord(text, lang1, lang2, lang3):
    #print(lang3)
    keyList = list(text.twoGram.keys())
    last2Gram = keyList[len(keyList) - 1]
    # to remove \n
    last2Gram = last2Gram[:-1]
    print(last2Gram)
    for i in list(lang3.keys()):
        if last2Gram in i:
            print('A match is: ' + i)



