## 1. naloga: Poštevanka

```
st = int(input("Vnos števila: "))
i = 1
while i <= 10:
    print(i * st)
    i += 1
```

# Naloge iz trgovine

## 2. naloga: Blagajna "vse po pet"

```
vsota = 0
i = 0
while i < 5:
    vsota += int(input('Cena artikla: '))
    i += 1
print('Vsota:', vsota)
     Rešitev z zanko for:

vsota = 0
for i in range(5):
    vsota += int(input('Cena artikla: '))
print('Vsota:', vsota)
```

## 3. naloga: Blagajna "konkurenca"

```
vsota = 0
i = int(input('Število izdelkov: '))
while i > 0:
    vsota += int(input('Cena artikla: '))
    i -= 1
print('Vsota:', vsota)
     Rešitev z zanko for:

vsota = 0
for i in range(int(input('Število izdelkov: '))):
    vsota += int(input('Cena artikla: '))
print('Vsota:', vsota)
```

## 4. naloga: Blagajna "top shop"

```
vsota = 0
# Spremenljivko cena najprej nastavimo na 1, da se zanka sploh začne izvajati.
cena = 1
while cena != 0:
    cena = int(input('Cena artikla: '))
    vsota += cena
print('Vsota:', vsota)
```

## 5. naloga: Državna agencija za varstvo potrošnikov

```
artiklov = -1
vsota = 0
cena = 1
while cena != 0:
    cena = int(input('Cena artikla: '))
    vsota += cena
    artiklov += 1
print('Vsota:', vsota)
if artiklov > 0:
    povprecje = vsota / artiklov
else:
    povprecje = 0.0
print('Povprečna cena:', round(povprecje, 5))
```

## 6. naloga: Klub anonimnih potrošnikov

```
artiklov = 0
vsota = 0
cena = 1
while cena != 0 and vsota < 100 and artiklov < 10:
    cena = int(input('Cena: '))
    vsota += cena
    artiklov += 1

if cena == 0:
    artiklov -= 1

print('Porabili boste', vsota, 'evrov za', artiklov, 'stvari.')
```

## 7. naloga: Tekoči račun

```
stanje = 0
while stanje > -100:
    stanje += int(input('Sprememba: '))
    print('Stanje:', stanje)
print('Bankrot!')
```