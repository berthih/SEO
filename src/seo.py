import sys
import os
from ngrams import *

def main():
    print('parsing directory ressources')

    dirname = '../ressources/'
    for filename in os.listdir(dirname):
        print(filename + '\n')
        file = open(dirname + filename, 'r')
        for line in file:
            #print(line + '\n')
            oneGram = ngrams(line, 1)
            twoGram = ngrams(line, 2)
            threeGram = ngrams(line, 3)
            fourGram = ngrams(line, 4)

if __name__ == "__main__":
    main()
