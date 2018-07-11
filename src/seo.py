import sys
import os
from ngrams import *

def main():
    print('parsing directory ressources')
    #../ressources/DE/ for deutsch
    #../ressources/EN/ for english
    #../ressources/FR/ for french
    dirname = '../ressources/FR/'
    for filename in os.listdir(dirname):
        print(filename + '\n')
        file = open(dirname + filename, 'r')
        i = 0
        oneGram = {}
        twoGram = {}
        threeGram = {}
        for line in file:
            #print(line + '\n')
            oneGram = ngrams(line, 1, oneGram)
            twoGram = ngrams(line, 2, twoGram)
            threeGram = ngrams(line, 3, threeGram)
            if (i > 20):
                break
            i += 1
        print('1-gram :\n')
        print(oneGram)
        print('2-gram :\n')
        print(twoGram)
        print('3-gram :\n')
        print(threeGram)

if __name__ == "__main__":
    main()
