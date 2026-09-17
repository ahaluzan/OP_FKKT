# Izredni izpitni rok pri predmetu Osnove programiranja

Tokrat se bomo ukvarjali z loterijo. Analizirali boste vplačane loto lističe s tem, da boste implementirali spodaj podane funkcije. Pri tem bodite pozorni, da bo vaša rešitev splošna: delovati mora za poljubne podatke, ki pa seveda ustrezajo predpisanemu formatu.

### 1 Funkcija `preberi_podatke(datoteka)`

Iz datoteke, katere ime je podano kot vhod v funkcijo, preberite podatke o vplačanih loto lističih in jih vrnite kot slovar, kjer je ključ ime in priimek osebe, ki je listič vplačala, vrednost pa je seznam vplačanih lističev. Vsak listič posebej je seznam, ki vsebuje izbrane številke med vključno 1 in 39. Podatki v datoteki so urejeni takole: vsaka vrstica vsebuje podatke o točno enem vplačanem loto lističu in sicer najprej ime lastnika, potem pa zaporedje sedmih številk (urejenih od najmanjše do največje). Vsi podatki v vrstici so ločeni z vejico. Če je nekdo vplačal več kot en listič, se njegovo ime preprosto ponovi v več vrsticah, ki niso nujno ena za drugo.

* Vhod: ime datoteke s podatki

* Izhod: slovar s podatki (glej primer)

Primer rezultata (Margaret je vplačala tri listke, ostali po enega):
```py
>>> vplacila = preberi_podatke("data.csv")
>>> vplacila
{'Christina Coleman': [[3, 11, 23, 26, 31, 33, 38]],
 'Margaret Rentas': [
  [1, 2, 5, 7, 10, 15, 39],
  [3, 5, 10, 11, 21, 22, 30],
  [4, 5, 10, 11, 21, 22, 30]
 ],
 'Romana Hammond': [[3, 9, 10, 12, 18, 19, 26]],
 'Teresa Hoffman': [[6, 10, 19, 25, 26, 29, 35]],
 'Cheryl Sheehan': [[3, 5, 15, 28, 29, 30, 31]],
 'Violet Bishop': [[3, 4, 18, 20, 24, 37, 38]],
 'Ronald Vue': [[1, 3, 16, 17, 23, 27, 28]],
 'Eric Atkins': [[1, 2, 5, 7, 10, 15, 39]],
 'Jerome Figures': [[4, 6, 20, 22, 29, 34, 37]],
 'Edgardo Burke': [[4, 5, 12, 16, 21, 22, 25]]}
```

### 2 Funkcija `statistika_vplacil(vplacila)`

Napišite funkcijo `statistika_vplacil(vplacila)`, ki prešteje koliko lističev je kdo vplačal. Funkcija kot vhod prejme slovar kot ga vrača prva naloga. Vrne naj slovar, kjer je ključ ime loto igralca (plačnika), vrednost pa število lističev, ki jih je ta igralec vplačal. 

* Vhod: slovar kot ga vrača naloga 1
* Izhod: slovar (glej primer)

Primer:

```py
>>> statistika_vplacil(vplacila)
{'Christina Coleman': 1,
 'Margaret Rentas': 3,
 'Romana Hammond': 1,
 'Teresa Hoffman': 1,
 'Cheryl Sheehan': 1,
 'Violet Bishop': 1,
 'Ronald Vue': 1,
 'Eric Atkins': 1,
 'Jerome Figures': 1,
 'Edgardo Burke': 1}
```

### 3 Funkcija `prestej_ujemanja(vplacane_kombinacije, dobitek)`

Napišite funkcijo, ki za vsak vplačan listek prešteje koliko številk se ujema z dobitno kombinacijo. Slednja je podana kot vhod z vsemi vplačanimi kombinaciji. Funkcija naj vrne seznam ujemanj (glej primer).

* Vhod: 
  * `vplacane_kombinacije` -- seznam vplačanih kombinacij
  * `dobitek` -- seznam sedmih urejenih številk, ki predstavlja dobitno kombinacijo
* Izhod: seznam ujemanj (ki je dolg toliko kot je vplačanih lističev; glej primer)

Primer:
```py
>>> vplacane_kombinacije = [
    [1, 2, 5, 7, 10, 15, 39],
    [3, 5, 10, 11, 21, 22, 30],
    [4, 5, 10, 11, 21, 22, 30]]
>>> dobitek = [1, 2, 5, 7, 10, 15, 39]
>>> prestej_ujemanja(vplacane_kombinacije, dobitek)
[7, 2, 2]
```

### 4 Funkcija `prestej_sedmice(vplacila, dobitek)`

Napiši funkcijo, ki prešteje koliko sedmic je bilo vplačanih. Na vhodu dobi vplačane loto lističe in dobitno kombinacijo (urejen seznam sedmih številk), vrne pa število lističev, ki so zadeli dobitno kombinacijo.

* Vhod: 
  * `vplacila` -- slovar vplačanih kombinacij (kot ga vrne naloga 1)
  * `dobitek` -- seznam sedmih urejenih številk, ki predstavlja dobitno kombinacijo
* Izhod: število vplačanih sedmic (dobitnih lističev)

Primer:
```py
>>> prestej_sedmice(vplacila, dobitek)
2
```

### 5 Funkcija `najmanj_pogosta_stevila(vplacila)`

Napiši funkcijo, ki iz podatkov o vplačanih lističih (vhod) izračuna najmanj pogosto uporabljeno število -- torej tisto, ki se najmanjkrat pojavlja na vplačanih loto lističih. Če je teh števil več, je zadosti, če vrne eno izmed njih.

* Vhod: slovar vplačanih kombinacij (kot ga vrne naloga 1)
* Izhod: najmanj pogosto uporabljeno število

Primer:

```py
>>> najmanj_pogosta_stevila(vplacila)
33
```
