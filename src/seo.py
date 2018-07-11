
import sys
import os
from src.ngrams import *
import operator


def main():
    print('parsing directory ressources')
    #../ressources/DE/ for deutsch
    #../ressources/EN/ for english
    #../ressources/FR/ for french
    dirname = '../ressources/FR/'

    fr = parseLanguage('../ressources/FR/')
    dirname = '../ressources/EN/'
    en = parseLanguage(dirname)
    dirname = '../ressources/DE/'
    de = parseLanguage(dirname)

    print(fr.threeGram)
    print('\n')
    print(de.threeGram)
    print('\n')
    print(en.threeGram)
# reversed(sorted(oneGram.items(), key=operator.itemgetter(1)))

if __name__ == "__main__":
    main()
