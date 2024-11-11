## 1. naloga: Črka v nizu

```
niz = input('Vpišite niz: ')
crka = input('Vpišite črko: ')
if crka in niz:
    print('Niz vsebuje črko '+crka+'.')
else:
    print('Niz ne vsebuje črke '+crka+'.')                                                     
```

## 2. naloga: Največje in najmanjše število

```
st1 = int(input("Vpišite 1. število: "))
st2 = int(input("Vpišite 2. število: "))
st3 = int(input("Vpišite 3. število: "))
maksimum = st1
minimum = st1
if st2 > maksimum:
    maksimum = st2
if st3 > maksimum:
    maksimum = st3
if st2 < minimum:
    minimum = st2
if st3 < minimum:
    minimum = st3
print("Minimum:", str(minimum)+", Maksimum:", maksimum)
```

## 3. naloga: Pretvarjanje temperatur

```
temp_C = float(input('Vpiši temperaturo [°C]: '))
pretvorba = input('Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)? ')
if pretvorba == 'K':
    temp_K = temp_C + 273.15
    print(str(temp_C) + '°C je enako ' + str(temp_K) + ' K')
elif pretvorba == 'F':
    temp_F = temp_C * 9/5 + 32
    print(str(temp_C) + '°C je enako ' + str(temp_F) + ' °F')
else:
    print('Vnesli ste napačno enoto!')
```

## 4. naloga: Indeks telesne mase

```
visina = float(input("Telesna višina [cm]: "))
teza = float(input("Teža [kg]: "))
indeks = teza / (visina/100) ** 2
print("Vaš indeks telesne mase je: ", round(indeks,2))
if indeks > 25:
    print("Treba se bo več gibati in jesti bolj zdravo!")
elif indeks < 18.5:
    print("Pojejte kakšen kos torte več! ;)")
else:
    print("Super, nadaljujte s svojim življenjskim stilom!")
```

## 5. naloga: Kvadratna enačba

```
a = float(input('Vpiši a: '))
b = float(input('Vpiši b: '))
c = float(input('Vpiši c: '))

d = b**2 - 4 * a * c
if d < 0:
    print('Enačba nima realnih rešitev.')
elif d == 0:
    x = -b / (2 * a)
    print('Enačba ima eno realno rešitev:', x)
else:
    x1 = (-b + pow(d, 1/2)) / (2 * a)
    x2 = (-b - pow(d, 1/2)) / (2 * a)
    print('Enačba ima dve realni rešitvi:', round(x1, 4), 'in', round(x2, 4))
```