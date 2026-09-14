## Naloge

```
import math

def preberi(datoteka):
    f = open(datoteka, 'r', encoding='utf8')
    tekst = f.readlines()
    f.close()
    slovar = {}
    for vrstica in tekst:
        ime, lokacija = vrstica.strip().split(':')
        x, y = lokacija.strip().split(',')
        slovar[ime] = (int(x), int(y))
    return slovar

def koordinate(slovar, ime):
    return slovar[ime]

def razdalja(slovar, ime, ime2):
    x1, y1 = slovar[ime]
    x2, y2 = slovar[ime2]
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)


def najblizji(slovar, ime):
    razdalja = 100000
    x1, y1 = slovar[ime]
    for plac in slovar:
        if plac != ime:
            x2, y2 = slovar[plac]
            d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            if d < razdalja:
                naj_plac = plac
                razdalja = d
    return naj_plac

def sosedje(slovar, ime, r):
    x1, y1 = slovar[ime]
    mn = set()
    for plac in slovar:
        if plac != ime:
            x2, y2 = slovar[plac]
            d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            if d < r:
                mn.add(plac)
    return mn
```
