# Spremenljivost

## 1. naloga: Korenjenje v seznamu (1)

```
def koreni_seznam(seznam):
    for i in range(len(seznam)):
        if seznam[i] >= 0:
            seznam[i] = seznam[i] ** 0.5
        else:
            seznam[i] = None
```

## 2. naloga: Korenjenje v seznamu (2)

```
def koreni_seznam2(seznam):
    s=[]
    for elt in seznam:
        if elt >= 0:
            s.append(elt ** 0.5)
        else:
            s.append(None)
    return s
```

## 3. naloga: Unikaten seznam

```
def unikaten_seznam(s):
    unikati = []
    for elt in s:
        if elt not in unikati:
            unikati += [elt]
    return unikati
```

# IMDb
 
## 4. naloga: IMDb

```
def ocene(serije):
    seznam = []
    for naslov, ocena, leto in serije:
        if ocena >= 9.0:
            seznam.append(naslov)
    return seznam
```

## 5. naloga: Najstarejša serija

```
def najstarejsa(serije):
    naj_naslov, naj_ocena, naj_leto =serije[0]
    for naslov, ocena, leto in serije:
        if leto < naj_leto:
            naj_naslov = naslov
            naj_leto = leto
    return naj_naslov
```

## 6. naloga: Povprečna ocena

```
def povprecna_ocena(serije):
    if len(serije) == 0:
        return 0
    suma = 0
    for naslov, ocena, leto in serije:
        suma += ocena
    return suma / len(serije)
```

## 7. naloga: Dolga imena serij

```
def dolga_imena(serije):
    seznam = []
    for naslov, ocena, leto in serije:
        if len(naslov.split()) > 2:
            seznam.append(naslov)
    return seznam
```

## 8. naloga: Krajšanje

```
def krajsanje(serije):
    seznam = []
    for naslov, ocena, leto in serije:
        seznam.append((naslov, ocena))
    return seznam 
```

## 9. naloga: Najnovejše serije

```
def najnovejse(serije):
    naj_naslov = []
    if len(serije) == 0:
        return naj_naslov
    
    naj_leto =serije[0][2]
    for serija in serije:
        if serija[2] > naj_leto:
            naj_leto = serija[2]
            
    for naslov, ocena, leto in serije:
        if leto == naj_leto:
            naj_naslov.append(naslov)

    return naj_naslov
```