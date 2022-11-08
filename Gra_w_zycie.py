from matplotlib import pyplot as plt
import random
import time

def zrob_tablice(szer, wys): ##funckja tworząca tablicę w sposób losowy
    data = []
    for i in range(wys):
        data.append([random.randint(a=0, b=1) for x in range(0, szer)])
    return data


def gra(stan):
    badanie = []
    wi_badanie = []

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
            wi_badanie.append(a)
        badanie.append(wi_badanie)
        wi_badanie = []
    print(badanie)




plt.ion()
x = 10
y = 10

dat = zrob_tablice(x, y)
gra(dat)
plt.imshow(dat)


#for i in range(10):
#    dat = zrob_tablice(x, y)
#    plt.imshow(dat)
#    plt.pause(0.5)
#    plt.clf()

