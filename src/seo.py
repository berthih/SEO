
from ngrams import *

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

if __name__ == "__main__":
    main()
