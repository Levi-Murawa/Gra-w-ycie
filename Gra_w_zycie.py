from matplotlib import pyplot as plt
import random
import time

tab_zolw = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
tab_blink = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
tab_blink_maly = [[0,0,0],[1,1,1],[0,0,0]]

def zrob_tablice(szer, wys): ##funckja tworząca tablicę w sposób losowy
    data = []
    for i in range(wys):
        data.append([random.randint(a=0, b=1) for x in range(0, szer)])
    return data


def gra(stan):
    wier = []
    tablica = []

    maks_wiersze = len(stan)
    maks_kolumny = len(stan[0])
    for wi in range(maks_wiersze):

        for kol in range(maks_kolumny):
            a = 0

            if (kol>0):
                a = a + stan[wi][kol-1]
            if (kol+1<maks_kolumny):
                a = a + stan[wi][kol+1]
            if (wi>0):
                a = a + stan[wi-1][kol]
            if (wi+1<maks_wiersze):
                a = a + stan[wi+1][kol]

            if (wi>0 and kol>0):
                a = a + stan[wi-1][kol-1]
            if (wi+1<maks_wiersze and kol+1< maks_kolumny):
                a = a + stan[wi+1][kol+1]
            if (wi+1 < maks_wiersze and kol > 0):
                a = a + stan[wi + 1][kol - 1]
            if (wi>0 and kol+1 < maks_kolumny):
                a = a + stan[wi - 1][kol + 1]
            ##print('A równa sie:',a, 'Wartosc rowna sie', stan[wi][kol]) ##wypis w celu debugowania
            if stan[wi][kol] == 1: ##żywa komurka będzie żyć przy dwóch lub trzeh sąsiadach, innaczej umiera
                if (a == 2 or a == 3):
                    wier.append(1)
                else:
                    wier.append(0)
            else: ##jeśli komurka jest martwa, to odrodiz się przy trzech sąsiadach
                if a == 3:
                    wier.append(1)
                else:
                    wier.append(0)
        tablica.append(wier)
        wier = []
    return tablica

def animacja(tab_wejsciowa, ile_okr, czas_okr):
    tab_copy = tab_wejsciowa.copy()
    plt.ion()
    for i in range(ile_okr):
        plt.imshow(tab_copy)
        plt.pause(czas_okr)
        tab_copy = gra(tab_copy)
        plt.clf()


x = 200
y = 200

dat = zrob_tablice(x, y)
animacja(dat, 100, 0.01)
