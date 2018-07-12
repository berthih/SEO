from src.ngrams import *
import operator
import marshal

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
    # fr = sorted(fr.twoGram.items(), key=operator.itemgetter(1))[::-100]
    # print(fr)
    frTwo = []

    save(fr, de, en)


def load():
    # saving the n-gram struct from each languages on the disk
    frF_oneGram = open('../saved_data/French_oneGram', 'ab')
    frF_twoGram = open('../saved_data/French_twoGram', 'ab')
    frF_threeGram = open('../saved_data/French_threeGram', 'ab')

    deF_oneGram = open('../saved_data/Deutsch_oneGram', 'ab')
    deF_twoGram = open('../saved_data/Deutsch_twoGram', 'ab')
    deF_threeGram = open('../saved_data/Deutsch_threeGram', 'ab')

    enF_oneGram = open('../saved_data/English_oneGram', 'ab')
    enF_twoGram = open('../saved_data/English_twoGram', 'ab')
    enF_threeGram = open('../saved_data/English_threeGram', 'ab')

    fr_oneGram = marshal.load(frF_oneGram)
    fr_twoGram = marshal.load(frF_twoGram)
    fr_threeGram = marshal.load(frF_threeGram)

    de_oneGram = marshal.load(deF_oneGram)
    de_twoGram = marshal.load(deF_twoGram)
    de_threeGram = marshal.load(deF_threeGram)

    en_oneGram = marshal.load(enF_oneGram)
    en_twoGram = marshal.load(enF_twoGram)
    en_threeGram = marshal.load(enF_threeGram)

    # closing the file used by marshal saving
    frF_oneGram.close()
    frF_twoGram.close()
    frF_threeGram.close()

    deF_oneGram.close()
    deF_oneGram.close()
    deF_oneGram.close()

    enF_oneGram.close()
    enF_oneGram.close()
    enF_oneGram.close()
    return fr_oneGram, fr_twoGram, fr_threeGram, de_oneGram, de_twoGram, de_threeGram, en_oneGram, en_twoGram, en_threeGram

def save(fr, de, en):
    # saving the n-gram struct from each languages on the disk
    frF_oneGram = open('../saved_data/French_oneGram', 'ab')
    frF_twoGram = open('../saved_data/French_twoGram', 'ab')
    frF_threeGram = open('../saved_data/French_threeGram', 'ab')

    deF_oneGram = open('../saved_data/Deutsch_oneGram', 'ab')
    deF_twoGram = open('../saved_data/Deutsch_twoGram', 'ab')
    deF_threeGram = open('../saved_data/Deutsch_threeGram', 'ab')

    enF_oneGram = open('../saved_data/English_oneGram', 'ab')
    enF_twoGram = open('../saved_data/English_twoGram', 'ab')
    enF_threeGram = open('../saved_data/English_threeGram', 'ab')

    fr_oneGram = sorted(fr.oneGram.items(), key=operator.itemgetter(1))[::-100]
    fr_twoGram = sorted(fr.twoGram.items(), key=operator.itemgetter(1))[::-100]
    fr_threeGram = sorted(fr.threeGram.items(), key=operator.itemgetter(1))[::-100]
    marshal.dump(fr_oneGram, frF_oneGram)
    marshal.dump(fr_twoGram, frF_twoGram)
    marshal.dump(fr_threeGram, frF_threeGram)

    de_oneGram = sorted(de.oneGram.items(), key=operator.itemgetter(1))[::-100]
    de_twoGram = sorted(de.twoGram.items(), key=operator.itemgetter(1))[::-100]
    de_threeGram = sorted(de.threeGram.items(), key=operator.itemgetter(1))[::-100]
    marshal.dump(de_oneGram, deF_oneGram)
    marshal.dump(de_twoGram, deF_twoGram)
    marshal.dump(de_threeGram, deF_threeGram)

    en_oneGram = sorted(en.oneGram.items(), key=operator.itemgetter(1))[::-100]
    en_twoGram = sorted(en.twoGram.items(), key=operator.itemgetter(1))[::-100]
    en_threeGram = sorted(en.threeGram.items(), key=operator.itemgetter(1))[::-100]
    marshal.dump(en_oneGram, enF_oneGram)
    marshal.dump(en_twoGram, enF_twoGram)
    marshal.dump(en_threeGram, enF_threeGram)

    # closing the file used by marshal saving
    frF_oneGram.close()
    frF_twoGram.close()
    frF_threeGram.close()

    deF_oneGram.close()
    deF_oneGram.close()
    deF_oneGram.close()

    enF_oneGram.close()
    enF_oneGram.close()
    enF_oneGram.close()

if __name__ == "__main__":
    main()
