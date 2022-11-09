# Gra w życie

Gra w życie to jedna z najbardziej znanych automatów komórkowych.
Powyższy kod zawiera funckje umożliwiające przeprowadzenie, wyświetlenie oraz wylosowanie danych do gry w życie. Wyświetlanie odbywa się dzięki bibliotece matplotlib a wersja z interfejsem użytkownika została stworzona dzięki bibliotece Tkinter.

Funkcje zawarte w skrypcie:
zrob_tablice(szer, wys) - funckja generuje tabilcje zawierającą zera i jedynku, rozkład zer i jedynek jest losowy. Rozmiar tablicy można regulować za pomocą wartości szer i wys.
gra(stan) - funckja odpowiedzialna za symulację, zwraca ona tablicę równą rozmiarami tablicy wejściowej po jednym tiku symulacji gry w życie.
animacja(tab_wejsciowa, ile_okr, czas_okr) - funckja wyświetla przy pomocy biblioteki matplotlib dane wejściowe po czym poddaje jej działaniu funckji gra() po czym aktualizuje wyświetlane dane. ile_okr - decyduje o liczbie powtórzeń całego procesu, czas_okr - odpowiada za czas wyświetlania jednego zestawu danych.
