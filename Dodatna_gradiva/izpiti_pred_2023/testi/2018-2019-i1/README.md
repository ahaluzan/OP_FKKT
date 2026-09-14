# 1. pisni izpit pri predmetu Osnove programiranja

Tekom izpita boste analizirali zbirko podatkov o filmih, tako da boste implementirali 
spodaj podane funkcije. Pri tem bodite pozorni, da bo vaša **rešitev splošna**: delovati 
mora za poljubno število filmov ter poljubno število ocenjevalcev.

## 1 Funkcija `preberi_filme(ime_datoteke)`

Napišite funkcijo `preberi_filme(ime_datoteke)`, ki iz podane datoteke prebere imena filmov in ostale podatke: žanr, letnico nastanka ter dolžino filma. Podatki so ločeni z vejicami, ena vrstica predstavlja en film. Podatke o dolžini filma preberite iz datoteke v obliki `uu:mm:ss`. Slednje pretvorite v številčno vrednost, ki predstavlja trajanje v minutah. Trajanje zaokrožite na dve decimalki. Npr. vrednost `1:25:15` se naj pretvori `85.25`. 

* Vhod: `ime_datoteke` s podatki
* Izhod: seznam seznamov oblike `ime filma, žanr, letnica, dolžina filma v minutah`

Primer:


```py
>>> filmi = preberi_filme("data.csv")
>>> filmi
[['Titanic', 'romance', 1997, 194.02],
 ['Matrix', 'scifi', 1993, 136.2],
 ['WALL-E', 'scifi', 2008, 98.65],
 ['Men in Black', 'scifi', 1997, 98.1],
 ['A Beautiful Mind', 'drama', 2001, 135.67],
 ['Star Trek Nemesis', 'scifi', 2002, 116.55],
 ['The godfather', 'drama', 1972, 175.3],
 ['Pirates of the Carribean: Black Pearl', 'adventure', 2003, 143.93],
 ['Sex and the City', 'romance', 2008, 145.73],
 ['Harry Potter and the Deathly Hallows 2', 'adventure', 2011, 130.85],
 ['Life of Brian', 'comedy', 1979, 94.1],
 ['Pulp Fiction', 'drama', 1994, 154.42],
 ['Alien', 'scifi', 1979, 116.47],
 ['Petelinji zajtrk', 'romance', 2007, 124.35],
 ['Rocky', 'drama', 1976, 120.12],
 ['American Pie', 'comedy', 1999, 95.78],
 ["Schindler's List", 'drama', 1993, 195.33],
 ['Ice Age: Dawn of the Dinosaurs', 'adventure', 2009, 94.93]]
```

## 2 Funkcija `povprecna_dolzina(filmi, zanr)`

Napišite funkcijo `povprecna_dolzina(filmi, zanr)`, ki izračuna in vrne povprečno dolžino filmov podanega žanra.
Rezultat zaokrožite na dve decimalni mesti. V primeru, da za podan žanr ni nobenega filma, vrnite vrednost 0.

* Vhod: 
  * `filmi` -- seznam podatkov o filmih kot ga vrne 1. naloga
  * `zanr` -- niz, ki predstavlja ime podanega žanra
* Izhod: povprečna dolžina filma za podani žanr


Primer:

```py
>>> povprecna_dolzina(filmi, "scifi")
113.19
```

## 3 Funkcija `presek(ocene, uporabnik1, uporabnik2)`

Napišite funkcijo `presek(ocene, uporabnik1, uporabnik2)`, ki vrne seznam filmov (predstavljenih kot indeks, torej zaporedno številko v seznamu), ki sta jih ocenila oba podana uporabnika. Podan imate slovar ocen (parameter `ocene`), ki je enake oblike kot je bil slovar iz 5. domače naloge: ključ predstavlja ime uporabnika, vrednost pa seznam 18 ocen filmov. Ocene so od 0 do 5, pri čemer pa ocena 0 pomeni, da uporabnik filma ni ocenil.

* Vhod: 
  * `ocene` slovar z ocenami
  * `uporabnik1` ime prvega uporabnika
  * `uporabnik2` ime drugega uporabnika
* Izhod: Seznam indeksov filmov, ki sta jih ocenila oba uporabnika


Primer:
```py
# Slovar ocen (za boljšo preglednost je prikazan je samo del)
>>> ocene = {
 'deki': [4, 5, 0, 4, 0, 0, 4, 3, 1, 1, 0, 4, 0, 0, 3, 3, 5, 3],
 'Janez': [0, 3, 4, 4, 3, 0, 5, 5, 2, 4, 5, 3, 0, 3, 2, 2, 0, 5],
 'Rak': [3, 5, 0, 4, 0, 2, 0, 0, 2, 4, 0, 0, 0, 0, 3, 5, 0, 0],
 'ATom': [4, 5, 5, 5, 5, 3, 5, 5, 0, 0, 5, 0, 4, 0, 0, 1, 5, 4],
 'Enej': [4, 5, 0, 4, 5, 0, 5, 3, 0, 0, 5, 4, 0, 3, 0, 3, 5, 4],
 'Greg': [3, 0, 4, 0, 5, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 3, 0, 4]}
# Klic funkcije
>>> presek(ocene, "Enej", "Greg")
[0, 4, 15, 17]
```

## 4 Funkcija `ocene_po_filmih(ocene, filmi)`

Napiši funkcijo `ocene_po_filmih(ocene, filmi)`, ki vrne slovar ocen in uporabnikov po posameznih filmih. Ključi v vrnjenem slovarju so naslovi filmov, vrednosti pa prav tako slovarji, ki kot ključe vsebujejo imena uporabnikov, ki so ta film ocenili, kot vrednosti pa ocene, ki so jih uporabniki podali. Torej, ključ v notranjem slovarju je ime uporabnika, vrednost pa njegova ocena filma. Pri izgradnji notranjega slovarja izpustite uporabnike, ki imajo za ta film oceno 0.

V seznamu ocen filmov, ki jih je podal nek uporabnik (znotraj slovarja `ocene`) so filmi podani v 
istem vrstnem redu kot filmi v seznamu podatkov o filmih, kot jih vrne prva naloga. Denimo 
zapis `ocene["deki"][1]` predstavlja oceno, ki jo je uporabnik `deki` podal za 
film z indeksom `1` (`film[1]`).

* Vhod: 
  * `ocene` slovar kot je bil v 5. domači nalogi, 
  * `filmi` seznam podatkov o filmih kot ga vrne naloga 1
* Izhod: slovar slovarjev


Primer:
```py
>>> glasovi = ocene_po_filmih(ocene, filmi)
>>> glasovi['Sex and the City']   # izpis ne vsebuje vseh uporabnikov za lažjo preglednost
{'deki': 1,
 'Janez': 2,
 'Rak': 2,
 'ivek': 1,
 'miso': 2,
 'nepoznalec': 1,
 # ....
 'Stickman': 2,
 'Skankhunt42': 5}
```

## 5 Funkcija `najboljsi_film(glasovi)`

Napiši funkcijo `najboljsi_film(glasovi)`, ki vrne film z najboljšo povprečno oceno. 

* Vhod: `glasovi` -- ocene po filmih kot jih vrne naloga 4
* Izhod: `niz` -- naslov filma z najboljšo (najvišjo) povprečno oceno

Primer:
```py
# primer vhodih podatkov
>>> glasovi = {
    'Titanic': {
        'deki': 5,
        'Rak': 4,
        'ATom': 3,
        'ivek': 2,
        'miso': 1},
    'Matrix': {
        'deki': 5,
        'Janez': 5,
    }
}
>>> najboljsi_film(glasovi)
'Matrix'
```
