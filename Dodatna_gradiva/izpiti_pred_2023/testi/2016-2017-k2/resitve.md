## 1. naloga

```
import numpy as np

def skupna_dolzina_meje(meje, drzave, drzava):
    i = drzave.index(drzava)
    return np.nansum(meje, axis = 1)[i]

def dolzina_meje(meje, drzave, par_drzav):
    i, j = drzave.index(par_drzav[0]), drzave.index(par_drzav[1])
    return meje[i][j]

def sosedi(meje, drzave, drzava):
    i = drzave.index(drzava)
    drzave = np.array(drzave)
    mn = drzave[~np.isnan(meje[i])]
    return set(mn)
```

## 2. naloga

```
def preberi(datoteka):
    f = open(datoteka, 'r', encoding='utf8')
    tekst = f.readlines()
    f.close()
    slovar = {}
    for vrstica in tekst:
        naslov, leto, drzava = vrstica.strip().split(';')
        if drzava not in slovar:
            slovar[drzava] = set()
        slovar[drzava].add((naslov, int(leto)))
    return slovar

def najstarejsi_filmi(slovar, drzava):
    min_naslov, min_leto = list(slovar[drzava])[0]
    min_naslov = {min_naslov}
    for naslov, leto in slovar[drzava]:
        if leto < min_leto:
            min_leto = leto
            min_naslov = {naslov}
        elif leto == min_leto:
            min_naslov.add(naslov)
    return min_naslov
``` 