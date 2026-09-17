## 1. naloga

```
def preberi_podatke(datoteke):
    s = {}
    for datoteka in datoteke:
        f = open(datoteka, encoding='utf-8')
        vrstice=f.readlines()
        f.close()
        merilno_mesto=vrstice[0].strip()
        s2 = {}
        for vrstica in vrstice[1:]:
            podatki=vrstica.split(';')
            p=podatki[0].split('.')
            s2[(int(p[2]),int(p[1]),int(p[0]))] = float(podatki[1])
        s[merilno_mesto]=s2
    return s
```

## 2. naloga

```
def najvecji_pretok(podatki,datum):
    ime = ''
    vrednost = -1
    for mm in podatki:
        if podatki[mm][datum]>vrednost:
            vrednost = podatki[mm][datum]
            ime = mm
    return ime
```

## 3. naloga

```
def dosezen_mejni_pretok(podatki, mejne):
    mn = set()
    for mm in podatki:
        for dan in podatki[mm]:
            if podatki[mm][dan] >= mejne[mm]:
                mn.add(mm)
                break
    return mn
```

## 4. naloga

```
def najvecji_skok_pritoka(s):
    naj = 0
    for i in range(1,len(s)):
        razlika = s[i]-s[i-1]
        if razlika > naj:
            naj = razlika

    if naj == 0:
        return None
    else:
        return naj
```

## 5. naloga

```
def zaporedno_narascanje(s):
    naj = 0
    zaporedno = 0
    for i in range(1, len(s)):
        if s[i]> s[i-1]:
            zaporedno+=1
        else:
            zaporedno = 0
        if zaporedno > naj:
            naj = zaporedno

    return naj
```