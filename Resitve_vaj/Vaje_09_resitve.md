# Filmi

## 1. naloga: Preberi 

```
def preberi(datoteka):
    f = open(datoteka, 'r', encoding='utf8')
    tekst = f.read()
    f.close()
    return tekst
```

## 2. naloga: V seznam

```
def v_seznam(datoteka):
    seznam = []
    for vrstica in open(datoteka, 'r', encoding='utf8'):
        film, ocena, zanr, leto = vrstica.split(';')
        seznam.append([film, float(ocena), zanr, int(leto)])
    return seznam
```

## 3. naloga: V slovar

```
def v_slovar(datoteka):
    slovar = {}
    for vrstica in open(datoteka, 'r', encoding='utf8'):
        film, ocena, zanr, leto = vrstica.split(';')
        if zanr not in slovar:
            slovar[zanr] = []
        slovar[zanr].append(film)
    return slovar
```

## 4. naloga: Najljubši film

```
def najljubsi(datoteka_pisanja):
    naj = input("Najljubši film: ")
    f = open(datoteka_pisanja, 'w', encoding='UTF-8')
    print(naj, file=f)
    f.close()
```

## 5. naloga: Zapis

```
def zapis(datoteka_branja, datoteka_pisanja):
    seznam = []
    for vrstica in open(datoteka_branja, 'r', encoding='utf8'):
        film, ocena, zanr, leto = vrstica.split(';')
        seznam.append(film)
    f = open(datoteka_pisanja, 'w', encoding = 'UTF-8')
    for ime in sorted(seznam):
        print(ime, file = f)
    f.close()
```

## 6. naloga: CSV

```
def ocena_filma(id_filma, csv_datoteka):
    f = open(csv_datoteka, "r", encoding = "utf-8")
    stevec = 0
    vsota = 0
    for vrstica in f:
        userId, movieId, rating, timestamp = vrstica
        if movieId == str(id_filma):
            vsota += float(rating)
            stevec += 1
    return vsota / stevec
```

# Oliver Twist

## 7. naloga: Število besed

```
def stevilo_besed(datoteka):
    f = open(datoteka, 'r', encoding='UTF-8')
    tekst = f.read()
    f.close()
    return len(tekst.split())
```

## 8. naloga: Različni znaki

```
def razlicni_znaki(datoteka):
    f = open(datoteka, 'r', encoding = 'UTF-8')
    tekst = f.read()
    f.close()
    slovar = {}
    for znak in tekst:
        if znak not in slovar:
            slovar[znak] = 0
        slovar[znak] += 1
    return len(slovar)
```

## 9. naloga: Najpogostejši znak

```
def najpogostejsi_znak(datoteka):
    f = open(datoteka, 'r', encoding = 'UTF-8')
    tekst = f.read()
    f.close()
    slovar = {}
    for znak in tekst:
        if znak not in slovar:
            slovar[znak] = 0
        slovar[znak] += 1
    maksi = max(slovar.values())
    for znak, st in slovar.items():
        if st == maksi:
            return znak
```

## 10. naloga: Hapax legomenon

```
def hapax(datoteka):
    f = open(datoteka, 'r', encoding = 'UTF-8')
    tekst = f.read()
    tekst_split = tekst.split()
    f.close()
    slovar = {}
    for beseda in tekst_split:
        if beseda not in slovar:
            slovar[beseda] = 0
        slovar[beseda] += 1
    seznam = []
    for beseda, st in slovar.items():
        if st == 1:
            seznam.append(beseda)
    return len(seznam)
```
