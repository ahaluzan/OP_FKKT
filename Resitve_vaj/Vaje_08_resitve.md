## 1. naloga: Besede z a-ji

```
def aa_besede(s):
    mn = set()
    for beseda in s.replace('.','').split():
        if beseda.lower().count('a') > 1:
            mn.add(beseda)
    return mn
```

## 2. naloga: Najdaljše besede

```
def najdaljse_besede(s):
    najdaljsa = 0
    besede = s.replace('.','').replace(',','').split()
    for beseda in besede:
        if len(beseda) > najdaljsa:
            najdaljsa = len(beseda)

    mn = set()
    for beseda in besede:
        if len(beseda) == najdaljsa:
            mn.add(beseda) 
    return mn
```

## 3. naloga: Inicialke

```
def velike_zacetnice(s):
    seznam = []
    for beseda in s.split():
        if len(beseda.replace('.','').replace(',','')) > 2:
            beseda = beseda.capitalize()
        seznam.append(beseda)
    return " ".join(seznam)
```

Če niste našli funkcije capitalize, lahko rešite tudi tako: `beseda = beseda[0].upper()+beseda[1:]`

## 4. naloga: Unikaten seznam

```
def razlicne_skladbe(seznam):
    return len(set(seznam))
```

## 5. naloga: Prijatelji

```
def skupne(seznam1, seznam2):
    return set(seznam1) & set(seznam2)
```

## 6. naloga: Repertuar

```
def repertuar(seznam1, seznam2):
    return set(seznam1) | set(seznam2)
```

## 7. naloga: Unikati

```
def unikatna_predvajanja(seznam1, seznam2):
    return set(seznam1) ^ set(seznam2)
```

## 8. naloga: Ponavljajoči se znaki

```
def ponavljajoci_znaki(niz):
    mn = set()
    for znak in niz:
        c=niz.count(znak)
        if c > 1:
            mn.add((znak,c))
    return mn
```

## 9. naloga: Onesnaženost z delci PM10

```
def najveckrat_onesnazena_mesta(podatki, kraji):
    mesta = [0] * len(kraji)
    for dan,postaje in podatki:
        for i in range(len(postaje)):
            if postaje[i] is not None and postaje[i] >= 50:
                mesta[i] += 1
    naj = max(mesta)
    if naj == 0:
        return(set())
    else:
        maksimumi = set()
        for i in range(len(kraji)):
            if mesta[i] == naj:
                maksimumi.add(kraji[i])
        return maksimumi
```
