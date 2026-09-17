## 1. naloga

```
def jeziki(naselje, ulica, hisna_stevilka):
    oznaka = naselje[ulica][hisna_stevilka]
    return set(oznaka)

def sporazumevanje(naselje, naslov1, naslov2):
    x1, y1 = naslov1
    x2, y2 = naslov2
    if naslov2 in [(x1 - 1, y1), (x1, y1 - 1), (x1 + 1, y1), (x1, y1 + 1)]:
        return jeziki(naselje, x1, y1) &  jeziki(naselje, x2, y2)

def najbolj_zastopan_jezik(naselje):
    slovar = {}
    for ulica in naselje:
        for hisa in ulica:
            for jezik in hisa:
                if jezik not in slovar:
                    slovar[jezik] = 0
                slovar[jezik] += 1

    m = max(list(slovar.values()))
    for jezik, st in slovar.items():
        if st == m:
            return jezik
```

## 2. naloga

```
def preberi(datoteka):
    f = open(datoteka, 'r', encoding='utf8')
    tekst = f.readlines()
    f.close()
    slovar = {}
    for vrstica in tekst:
        drzava1, rezultat, drzava2 = vrstica.strip().split(';')
        r1, r2 = rezultat.split(':')
        if drzava1 not in slovar:
            slovar[drzava1] = [0, 0]
        slovar[drzava1][0] += int(r1)
        slovar[drzava1][1] += int(r2)
        if drzava2 not in slovar:
            slovar[drzava2] = [0, 0]
        slovar[drzava2][0] += int(r2)
        slovar[drzava2][1] += int(r1)
    return slovar

def stevilo_zadetih_golov(slovar, drzava):
    return slovar[drzava][0]
``` 