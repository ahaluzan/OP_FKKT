
## 1. naloga: Kako ti je ime?

```
ime = input("Vpiši ime: ")
print("Dolžina imena", ime, "je", len(ime))
```

## 2. naloga: Pitagorov izrek

```
a = float(input("Vpiši dolžino prve katete: "))
b = float(input("Vpiši dolžino druge katete: "))

c = a ** 2 + b ** 2
c = c ** (1 / 2)

print("Dolžina hipotenuze: ", str(round(c, 1)))
```

## 3. naloga: Ploščina pravokotnega trikotnika

```
a = float(input("Vpiši dolžino prve katete: "))
b = float(input("Vpiši dolžino druge katete: "))

c = a ** 2 + b ** 2
c = c ** (1 / 2)
p = a * b / 2

print("Dolžina hipotenuze:", round(c,2))
print("Ploščina trikotnika:", round(p,2))
```

## 4. naloga: Molska masa

```
hidratacija = float(input('Stopnja hidratacije: '))

Cu = 63.5
S = 32.1
O = 16.0
H = 1.0
mm = Cu + S + 4 * O + hidratacija * (2 * H + O)
print('Molska masa je', mm, 'g/mol.')
```