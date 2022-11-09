from matplotlib import pyplot as plt
import random
import tkinter as tk

tab_zolw = [[0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]]
tab_blink = [[0, 0, 0],
             [1, 1, 1],
             [0, 0, 0]]
szybowiec = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 1],
             [0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1, 0]]
datkota = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]


# funckja tworząca tablicę w sposób losowy
def zrob_tablice(szer, wys):
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

            if kol > 0:
                a = a + stan[wi][kol - 1]
                if wi > 0:
                    a = a + stan[wi - 1][kol - 1]
            if kol + 1 < maks_kolumny:
                a = a + stan[wi][kol + 1]
                if wi + 1 < maks_wiersze:
                    a = a + stan[wi + 1][kol + 1]
            if wi > 0:
                a = a + stan[wi - 1][kol]
                if kol + 1 < maks_kolumny:
                    a = a + stan[wi - 1][kol + 1]
            if wi + 1 < maks_wiersze:
                a = a + stan[wi + 1][kol]
                if kol > 0:
                    a = a + stan[wi + 1][kol - 1]


# Żywa komurka będzie żyć przy dwóch lub trzeh sąsiadach, innaczej umiera
            if stan[wi][kol] == 1:
                if a == 2 or a == 3:
                    wier.append(1)
                else:
                    wier.append(0)
# jeśli komurka jest martwa, to odrodiz się przy trzech sąsiadach
            else:
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
        plt.axis('off')
        plt.pause(czas_okr)
        tab_copy = gra(tab_copy)
        plt.clf()


def test():
    dat = zrob_tablice(100, 100)
    animacja(dat, 100, 0.1)


if __name__ == '__main__':
    def symulacja():
        ilosc_cykli = int(e1.get())
        czas_cyklu = float(e2.get())
        roz_x = int(e4.get())
        roz_y = int(e5.get())
        try:
            tryb = e3.get(e3.curselection())
        except:
            tryb = "Losowanie"
        if tryb == "Losowanie":
            tab = zrob_tablice(roz_x, roz_y)
            animacja(tab, ilosc_cykli, czas_cyklu)
        elif tryb == "Żółw":
            animacja(tab_zolw, ilosc_cykli, czas_cyklu)
        elif tryb == "Blink":
            animacja(tab_blink, ilosc_cykli, czas_cyklu)
        elif tryb == "Szybowiec":
            animacja(szybowiec, ilosc_cykli, czas_cyklu)
        elif tryb == "Dakota":
            animacja(datkota, ilosc_cykli, czas_cyklu)


    master = tk.Tk()
    master.title("Symulacja gry w życie")
    tk.Label(master, text="Liczba okresów").grid(row=0)
    tk.Label(master, text="Czas pojedyńczego okresu").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e1.insert(10, 500)
    e2.insert(10, 0.05)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Label(master, text="Wybór trybu").grid(row=2)
    e3 = tk.Listbox(master, height = 5, selectmode = 'SINGLE')
    e3.insert(1, "Losowanie")
    e3.insert(2, "Żółw")
    e3.insert(3, "Blink")
    e3.insert(4, "Szybowiec")
    e3.insert(5, "Dakota")

    e3.grid(row=2, column=1)

    tk.Label(master, text="Rozmiar X (tylko dla losowania)").grid(row=3)
    tk.Label(master, text="Rozmiar Y (tylko dla losowania)").grid(row=4)

    e4 = tk.Entry(master)
    e5 = tk.Entry(master)
    e4.insert(10, 100)
    e5.insert(10, 100)

    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)

    tk.Button(master,
              text='Wyjdź (naciśnij dwa razy)',
              command=master.quit).grid(row=5,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master, text='Symulacja', command=symulacja).grid(row=5,
                                                           column=1,
                                                           sticky=tk.W,
                                                           pady=4)

    master.mainloop()

    tk.mainloop()
