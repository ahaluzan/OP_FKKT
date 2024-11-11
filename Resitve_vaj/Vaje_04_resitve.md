## 1. naloga: Iskanje minimuma

```
seznam = eval(input('Vpišite seznam števil: '))
minimum = seznam[0]
for elt in seznam:
    if elt < minimum:
        minimum = elt
print(minimum)
```

## 2. naloga: Niz v seznamu

```
seznam = ["beseda", "spremenljivka", "niz", "zanka", "stavek", "slovar"]
niz=input('Vpišite iskani niz: ')
if niz in seznam:
    print('Seznam vsebuje niz "'+niz+'".')
else:
    print('Seznam ne vsebuje niza "'+niz+'".')
```

## 3. naloga: Števila v seznamu

```
seznam = [3, 35, 7, 68, 9, 10, 12, 481, 17, 12, 31, 21, 98, 33]
st=int(input('Vpišite število: '))
if st in seznam:
    print('Seznam vsebuje število',st)
else:
    print('Seznam ne vsebuje števila', st)
```

## 4. naloga: Vsota in povprečje

```
seznam = eval(input("Vpišite seznam števil: "))
vsota = 0
for elt in seznam:
    vsota += elt
print(vsota)
if len(seznam) != 0:
    print(round(vsota/len(seznam), 5))
else:
    print(0)
```

## 5. naloga: Iskanje večkratnikov

```
seznam = eval(input("Vpišite seznam števil: "))
st = int(input("Vnesite število: "))

vsebuje = False
for elt in seznam:
    if elt % st == 0:
        vsebuje = True
        break
if vsebuje:
    print("Vsebuje.")
else:
    print("Ne vsebuje.")
```

## 6. naloga: Samo večkratniki

```
seznam = eval(input("Vpišite seznam števil: "))
st = int(input("Vnesite število: "))

samo_veckratniki = True
for elt in seznam:
    if elt % st != 0:
        samo_veckratniki = False
        break
if samo_veckratniki:
    print("Vsebuje.")
else:
    print("Ne vsebuje.")
```

## 7. naloga: Izris trikotnika

```
n = int(input('Vpiši višino: '))

for i in range(1, n + 1):
    print('*' * i)
```

## 8. naloga: Izris smrekice

```
n = int(input('Vpiši višino: '))

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
```