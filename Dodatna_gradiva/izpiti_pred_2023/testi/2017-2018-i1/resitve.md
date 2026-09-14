## 1. naloga

```
def preberi_podatke(datoteke):
    vsi = []
    for datoteka in datoteke:
        f = open(datoteka, encoding = 'utf-8')
        vrstice=f.read().split('\n')
        drzava = vrstice[0]
        vrstice = vrstice[1:]
        for podatki in vrstice:
            podatki = podatki.split(';')
            for i in range(1,4):
                if podatki[i] == '-':
                    podatki[i] = None
                else:
                    podatki[i] = int(podatki[i])
            podatki.append(drzava)
            vsi.append(podatki)
        f.close()
    return vsi
```

## 2. naloga

```
def delez_delujocih_naprav(smucisca):
    deluje = 0
    vsi = 0
    for smucisce in smucisca:
        obratuje = smucisce[4].split('/')
        deluje += int(obratuje[0])
        vsi += int(obratuje[1])
    return deluje/vsi
```

## 3. naloga

```
def najvecja_razlika(smucisca):
    naj_razlika = float('-inf')
    for smucisce in smucisca:
        if smucisce[1] != None and smucisce[2] != None:
            razlika = smucisce[2] - smucisce[1]
            if razlika > naj_razlika:
                naj_razlika = razlika

    imena = set()
    for smucisce in smucisca:
        if smucisce[1] != None and smucisce[2] != None:
            razlika = smucisce[2] - smucisce[1]
            if razlika == naj_razlika:
               imena.add(smucisce[0]) 

    return naj_razlika, imena
```

## 4. naloga

```
def novozapadli_sneg_po_drzavah(smucisca, n):
    novozapadli = {}
    for smucisce in smucisca:
        if smucisce[5] not in novozapadli:
            novozapadli[smucisce[5]] = 0

        if smucisce[3] != None and smucisce[3] >= n:
            novozapadli[smucisce[5]] += 1

    return novozapadli
```

## 5. naloga

```
def dolzina_zasnezeno(visine):
    stevec = 0
    naj = 0
    for visina in visine:
        if visina >= 20:
            stevec+= 1
        else:
            stevec = 0
            
        if stevec > naj:
            naj = stevec
    return naj
```