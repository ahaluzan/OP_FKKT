## 1. naloga

```
def preberi(datoteka):
    f = open(datoteka, 'r', encoding='utf8')
    tekst = f.readlines()
    f.close()
    slovar = {}
    for vrstica in tekst:
        kategorija, nominiranci = vrstica.strip().split(':')
        nominiranci = nominiranci.strip().split(';')
        slovar[kategorija] = nominiranci
    return slovar

def stevilo_nominirancev(slovar, kategorija):
    return len(slovar[kategorija])

def velikost_kategorij(slovar, stevilo):
    kategorije = set()
    for kategorija, nominiranci in slovar.items():
        if len(slovar[kategorija]) == stevilo:
            kategorije.add(kategorija)
    return kategorije

def stevilo_nominacij(slovar, film):
    st_nominacij = 0
    for kategorija, nominiranci in slovar.items():
        for nominiranec in nominiranci:
            if film in nominiranec:
                st_nominacij += 1
    return st_nominacij
```

## 2. naloga

```
def radioaktivnost(k):
    dt = 1
    N = 1000
    N2 = N / 2
    i = 0
    while N > N2:
        dN = -k * N * dt
        N += dN
        i += dt
    return i
```