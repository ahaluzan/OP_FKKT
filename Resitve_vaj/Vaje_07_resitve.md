## 1. naloga: V slovar

```
def v_slovar(izdelki):
    cene = {}
    for izdelek, cena, zaloga in izdelki:
        cene[izdelek] = [cena, zaloga]
    return cene
```

## 2. naloga: Število izdelkov

```
def stevilo_izdelkov(zaloga):
    vsota = 0
    for izdelek, vrednost in zaloga.items():
        cena, zaloga = vrednost
        vsota += zaloga
    return vsota
```

## 3. naloga: Nakupovalna košara

```
def nakupovalna_kosara(seznam):
    slovar = {}
    for izdelek in seznam:
        if izdelek not in slovar:
            slovar[izdelek] = 0
        slovar[izdelek] += 1
    return slovar
```

## 4. naloga: Cena

```
def cena(zaloga, slovar_nakupov):
    znesek = 0
    for izdelek, kolicina in slovar_nakupov.items():
        znesek += kolicina * zaloga[izdelek][0]
    return znesek
```

## 5. naloga: Popravek zaloge

```
def popravek_zaloge(zaloga, izdelek, popravek):
    nova_zaloga = zaloga[izdelek][1] + popravek
    if nova_zaloga >= 0:
        zaloga[izdelek][1] = nova_zaloga
        return nova_zaloga
    else:
        return None
```

## 6. naloga: Blagajna

```
def blagajna(zaloga, slovar_nakupov):
    for izdelek, kolicina in slovar_nakupov.items():
        popravek_zaloge(zaloga, izdelek, -kolicina)
    return cena(zaloga, slovar_nakupov)
```

## 7. naloga: Kuhanje

```
def kuhanje(zaloga, jedi, jed):
    cena = 0
    for sestavina, kolicina in jedi[jed].items():
        cena += kolicina * zaloga[sestavina][0]
    return cena
```

## 8. naloga: Obrok

```
def posamezna_jed(jedi, jed, obrokov):
    sestavine = {}
    for sestavina, kolicina in jedi[jed].items():
        sestavine[sestavina] = kolicina * obrokov
    return sestavine
```

## 9. naloga: Nakup

```
def nakup(jedi, obroki):
    sestavine = {}
    for jed, obrokov in obroki:
        for sestavina, kolicina in posamezna_jed(jedi, jed, obrokov).items():
            if sestavina not in sestavine:
                sestavine[sestavina] = 0
            sestavine[sestavina] += kolicina
    return sestavine
```

## 10. naloga: Primanjkljaj

```
def primanjkljaj(zaloga, jedi, obroki):
    sestavine = nakup(jedi, obroki)
    slovar = {}
    for sestavina, kolicina in sestavine.items():
        if zaloga[sestavina][1] < kolicina:
            slovar[sestavina] = kolicina - zaloga[sestavina][1]
    return slovar
```
