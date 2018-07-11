from src.ngrams import *
import operator
from itertools import islice



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

    fr = sorted(fr.twoGram.items(), key=operator.itemgetter(1))[::-100]
    print(fr)
    frTwo = []

    with open('../ressources/FR/europarl-v7.fr-en.fr') as myfile:
        head = list(islice(myfile, 10000))

    for gram in fr:
        if gram[0] in ''.join(head):
            frTwo.append(gramOccurence(gram[0], gram[1], 1))

if __name__ == "__main__":
    main()
