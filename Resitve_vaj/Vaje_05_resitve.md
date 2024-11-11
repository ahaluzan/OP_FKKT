## 1. naloga: Iskanje minimuma

```
def minimum(seznam):
    minimum = seznam[0]
    for elt in seznam:
        if elt < minimum:
            minimum = elt
    return minimum
```

## 2. naloga: Trikotniška neenakost

```
def trikotniska_neenakost(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False
```

## 3. naloga: Samoglasniki

```
def samoglasnik(s):
    if s.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
```

## 4. naloga: pH

```
from math import log10

def pH(koncentracija):
    return -log10(koncentracija)
```

## 5. naloga: Prekrivajoča se seznama

```
def prekrivajoca_seznama(seznam1, seznam2):
    for elt in seznam1:
        if elt in seznam2:
            return True
    return False
```

# Razcep na prafaktorje

Napisati želimo funkcijo razcep_na_prafaktorje(n), ki nam vrne razcep števila na prafaktorje. Ker gre za dokaj kompleksno nalogo, smo jo razkosali na več podnalog (6. - 9.).

## 6. naloga: Praštevilo

```
def prastevilo(n):
    if n == 1:
        return False
    prastevilo = True
    for j in range(2, n//2 + 1):
        if n % j == 0:
            prastevilo = False
            return prastevilo
    return prastevilo
```

## 7. naloga: Praštevila

Pomagamo si s funkcijo prestevilo(n) iz prejšnje naloge. 

```
def prastevila(n):
    seznam_prastevil = []
    for i in range(2, n + 1):
        if prastevilo(i):
            seznam_prastevil += [i]
    return seznam_prastevil
```

## 8. naloga: Deljivost

```
def deljivost(n, x):
    stevec = 0
    while n % x == 0:
        n /= x
        stevec += 1
    return stevec
```

## 9. naloga: Razcep na prafaktorje

Pomagamo si s funkcijama prastevila(n) in deljivost(n, x). 

```
def razcep_na_prafaktorje(n):
    seznam = []
    seznam_prastevil = prastevila(n)
    for prastevilo in seznam_prastevil:
        deli = deljivost(n, prastevilo)
        if deli > 0:
            seznam += [[prastevilo, deli]]
    return seznam
```

# Fibonaccijevo zaporedje

## 10. naloga: Fibonaccijeva števila

```
def fibonaccijeva_stevila(n):
    f1 = 1
    f2 = 1
    stevila = [1, 1]
    while f1 + f2 < n:
        stevila += [f1 + f2]
        f2, f1 = f1, f1 + f2
    return stevila
```

## 11. naloga: Liha Fibonaccijeva števila

```
def liha_fibonaccijeva_stevila(n):
    stevila = fibonaccijeva_stevila(n)
    suma = 0
    for st in stevila:
        if st % 2 == 1:
            suma += st
    return suma
```
