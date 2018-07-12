from src.ngrams import *
import operator


def main():
    print('parsing directory ressources')
    #../ressources/DE/ for deutsch
    #../ressources/EN/ for english
    #../ressources/FR/ for french

    dirnameEN = '../ressources/EN/'
    dirnameFR = '../ressources/FR/'
    dirnameDE = '../ressources/DE/'

    fr = parseLanguage(dirnameFR)
    en = parseLanguage(dirnameEN)
    de = parseLanguage(dirnameDE)

    # get only 100 most present elt
    fr = sorted(fr.twoGram.items(), key=operator.itemgetter(1))[::-100]
    # print(fr)
    frTwo = []

    listOccur = countOccur(dirnameFR, fr)
    for elt in listOccur:
        print(elt.str + ' ' + str(elt.value) + ' ' + str(elt.nbOccurence))


if __name__ == "__main__":
    main()
