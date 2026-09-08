# 1. vaje: Python in IDLE

## Naloge

Pri reševanju pazite, da se vaši izpisi ujemajo z izpisi v navodilih
(vključno s presledki).

ZIP-datoteko s testi razpakirajte v enega od imenikov, kjer imate
pravice za pisanje. Vsaka naloga ima svoj podimenik, v katerem so testi.
Svoj program ustrezno poimenujte in shranite v imenik poleg testne
skripte `test.py`. Teste poženete tako, da poženete program `test.py`
(lahko preko IDLE ali konzole).

### Kako ti je ime? 

Napišite program `ime.py`, ki uporabnika povpraša najprej po imenu in na
zaslon izpiše dolžino tega imena.

*Primer pravilnega delovanja programa:*

``` text
Vpiši ime: Janez
Dolžina imena Janez je 5
```

### Pitagorov izrek 

Napišite program `pitagorov_izrek.py`, ki uporabnika vpraša po dolžinah
katet pravokotnega trikotnika in izpiše dolžino hipotenuze. Program naj
omogoča vnos decimalnih števil. Rezultat naj bo zaokrožen na eno
decimalko.

*Primer pravilnega delovanja programa:*

``` text
Vpiši dolžino prve katete: 3
Vpiši dolžino druge katete: 4
Dolžina hipotenuze: 5.0
```

### Ploščina pravokotnega trikotnika 

Program iz prejšnje naloge spremenite tako, da izračuna in izpiše
ploščino pravokotnega trikotnika. Program shranite kot `ploscina.py`.
Oba rezultata v izpisu zaokrožite na dve decimalni mesti natančno.

*Primer pravilnega delovanja programa:*

``` text
Vpiši dolžino prve katete: 3
Vpiši dolžino druge katete: 4  
Dolžina hipotenuze: 5.0
Ploščina trikotnika: 6.0
```

### Molska masa 

Napišite program `molska_masa.py`, ki na podlagi uporabnikovega vnosa
celega števila molekul vode, izračuna molsko maso $CuSO_4(H_2O)_x$.

Pri izračunu uporabite naslednje relativne atomske mase:

``` text
Cu = 63.5
S = 32.1
O = 16.0
H = 1.0
```

Rezultat naj bo zaokrožen na eno decimalko.

*Primer pravilnega delovanja programa:*

``` text
Stopnja hidratacije: 5
Molska masa je 249.6 g/mol.
```

## Rešitve

### Kako ti je ime?

``` {.python breaklines="" bgcolor="UL_lightgray" linenos=""}
ime = input("Vpiši ime: ")
print("Dolžina imena", ime, "je", len(ime))
```

### Pitagorov izrek

``` {.python breaklines="" bgcolor="UL_lightgray" linenos=""}
a = float(input("Vpiši dolžino prve katete: "))
b = float(input("Vpiši dolžino druge katete: "))

c = a ** 2 + b ** 2
c = c ** (1 / 2)

print("Dolžina hipotenuze: ", str(round(c, 1)))
```

### Ploščina pravokotnega trikotnika 

``` {.python breaklines="" bgcolor="UL_lightgray" linenos=""}
a = float(input("Vpiši dolžino prve katete: "))
b = float(input("Vpiši dolžino druge katete: "))

c = a ** 2 + b ** 2
c = c ** (1 / 2)
p = a * b / 2

print("Dolžina hipotenuze:", round(c,2))
print("Ploščina trikotnika:", round(p,2))
```

### Molska masa 

``` {.python breaklines="" bgcolor="UL_lightgray" linenos=""}
hidratacija = int(input('Stopnja hidratacije: '))

Cu = 63.5
S = 32.1
O = 16.0
H = 1.0

mm = Cu + S + 4 * O + hidratacija * (2 * H + O)
mm = round(mm,1)

print('Molska masa je', mm, 'g/mol.')
```

# 2. vaje: Pogojni stavek *if*

## Naloge

### Črka v nizu 

Napišite program `crka_v_nizu.py`, ki ugotovi, ali nek niz vsebuje
podano črko (ali nek drug znak). Vaš program naj uporabnika najprej
vpraša po nizu, nato še po črki. Program naj izpiše, ali je ta črka
vsebovana v nizu. Da bo naloga lažja, naj program velike in male črke
smatra kot različne znake.

*Primer delovanja programa:*

``` {.text breaklines="" bgcolor="gray_light"}
Vpišite niz: fakulteta
Vpišite črko: a
Niz vsebuje črko a.

Vpišite niz: univerza
Vpišite črko: ž
Niz ne vsebuje črke ž.
```

Pri tej nalogi testi niso občutljivi na presledke.

### Največje in najmanjše število

Napišite program `min_maks.py`, ki izpiše največjo in najmanjšo izmed
treh (celih) števil, ki jih vnese uporabnik. Ne uporabite funkcij
`min()` in `max()`.

*Primer delovanja programa:*

``` {.text breaklines="" bgcolor="gray_light"}
Vpišite 1. število: 5
Vpišite 2. število: 8
Vpišite 3. število: 7
Minimum: 5, Maksimum: 8
```

### Pretvarjanje temperatur 

Napišite program `temperature.py`, ki uporabnika vpraša po stopinjah
Celzija in v katero enoto naj jih spremeni (Fahrenheit ali Kelvin).
Program izpiše pretvorjeno vrednost. Če uporabnik vnese napačno enoto,
mu izpiše opozorilo: `Vnesli ste napačno enoto!`.

Pretvorbi izračunamo po formulah: $K = C + 273.15$ in
$F = C\cdot \frac{9}{5} + 32$.

*Primer delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Vpiši temperaturo [°C]: 32
Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)? K
32.0 °C je enako 305.15 K

Vpiši temperaturo [°C]: 23
Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)? F
23.0 °C je enako 73.4 °F

Vpiši temperaturo [°C]: 13
Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)? C
Vnesli ste napačno enoto!
```

### Indeks telesne mase

Napišite program `ITM.py`, ki uporabnika vpraša po telesni višini v in
masi. ITM izračunajte po formuli $ITM = teza / visina^{2}$, pri čemer
vnesete težo v enoti $kg$, višino pa v $m$. Rezultat zaokrožite na dve
decimalni mesti.

Če je indeks manjši od 18,5, uporabniku sporočite, da indeks kaže na
prenizko telesno težo. Če je indeks večji od 25, sporočite, da kaže na
previsoko telesno težo. V nasprotnem primeru sporočite, da kaže na
normalno telesno težo.

*Primer delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Telesna višina [cm]: 189
Teža [kg]: 70
Vaš indeks telesne mase je: 19.6
Indeks kaže na normalno telesno težo.

Telesna višina [cm]: 170
Teža [kg]: 53
Vaš indeks telesne mase je: 18.34
Indeks kaže na prenizko telesno težo.

Telesna višina [cm]: 165
Teža [kg]: 70
Vaš indeks telesne mase je: 25.71
Indeks kaže na previsoko telesno težo.
```

### Kvadratna enačba 

Napišite program `kvadratna_enacba.py`, ki izračuna vse realne rešitve
kvadratne enačbe $ax^2+bx+c=0$ na štiri decimalna mesta za decimalno
vejico. Uporabnik naj vnese vrednosti parametrov $a$, $b$ in $c$.

Pri iskanju rešitev kvadratne enačbe si pomagajte z izračunom
diskriminante: $D = b^2 - 4ac$.

Pri tem velja:

- $D > 0$: kvadratna enačba ima dve realni rešitvi,
  $x_{1,2} = \frac{-b \pm \sqrt{D}}{2a}$,

- $D = 0$: kvadratna enačba ima natanko eno realno rešitev,
  $x = \frac{-b}{2a}$ in

- $D < 0$: kvadratna enačba nima realnih rešitev.

*Primer pravilnega delovanja programa:*

``` {.text breaklines="" bgcolor="gray_light"}
Vpiši a: 1
Vpiši b: 2
Vpiši c: 1
Enačba ima eno realno rešitev: -1.0

Vpiši a: 1
Vpiši b: 2
Vpiši c: 0
Enačba ima dve realni rešitvi: 0.0 in -2.0

Vpiši a: 1
Vpiši b: 2
Vpiši c: 2
Enačba nima realnih rešitev.
```

## Rešitve

### Črka v nizu

``` python
niz = input('Vpišite niz: ')
crka = input('Vpišite črko: ')
if crka in niz:
    print('Niz vsebuje črko '+crka+'.')
else:
    print('Niz ne vsebuje črke '+crka+'.')                                                     
```

### Največje in najmanjše število 

``` python
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

### Pretvarjanje temperatur 

``` python
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

### Indeks telesne mase 

``` python
visina = float(input("Telesna višina [cm]: "))
teza = float(input("Teža [kg]: "))
indeks = teza / (visina/100) ** 2
print("Vaš indeks telesne mase je: ", round(indeks,2))
if indeks > 25:
    print("Indeks kaže na previsoko telesno težo.")
elif indeks < 18.5:
    print("Indeks kaže na prenizko telesno težo.")
else:
    print("Indeks kaže na normalno telesno težo.")
```

### Kvadratna enačba 

``` python
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

# 3. vaje: Zanka *while*

## Naloge

### Poštevanka 

Napišite program `postevanka.py`, ki uporabnika pozove k vnosu števila,
nato pa na zaslon izpiše večkratnike podanega števila do 10.

*Primer delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Vnos števila: 5
5
10
15
20
25
30
35
40
45
50
```

### Vse po pet 

Napišite program `vse_po_pet.py`, ki zahteva, da morajo stranke v
trgovini vedno kupiti natanko pet artiklov. Program uporabnika vpraša po
petih cenah; ko jih uporabnik vnese, program izpiše vsoto.

*Primer delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Cena artikla: 6
Cena artikla: 3
Vsota: 16
```

### Konkurenca

Program ,,vse po pet" popravite tako, da blagajnika najprej vpraša,
koliko izdelkov je v košarici, nato vpraša po cenah teh izdelkov in na
koncu izpiše vsoto. Program poimenujte `konkurenca.py`.

*Primer delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Število izdelkov: 3
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Vsota: 7
```

### Top shop 

Popravite program ,,konkurenca" tako, da ta uporabnika sprašuje po cenah
toliko časa, dokler mu uporabnik ne vnese ničle. Program poimenujte
`top_shop.py`.

*Primer delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Cena artikla: 0
Vsota: 7
```

### Povprečna cena

Popravite program `top_shop.py` tako, da bo izpisal tudi povprečno ceno.
To zaokrožite na 5 decimalnih mest. Program poimenujte
`povprecna_cena.py`.

*Primer delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Cena artikla: 0
Vsota: 7
Povprečna cena: 2.33333
```

### Trojni stop 

Napišite program `trojni_stop.py`, ki mu uporabnik vnaša cene in ki se
neha izvajati, ko uporabnik vnese 0 (ne bo več kupoval), ko je vnešenih
deset števil ali ko vsota cen doseže ali preseže 100 evrov.

Primer delovanja, ko uporabnik vnese 0:

``` {.text breaklines="" bgcolor="gray_light"}
Cena: 10
Cena: 5
Cena: 0
Porabili boste 15 EUR za 2 stvari.
```

Primer delovanja, ko uporabnik preseže 100 evrov:

``` {.text breaklines="" bgcolor="gray_light"}
Cena: 10
Cena: 5
Cena: 90
Porabili boste 105 EUR za 3 stvari.
```

Primer delovanja, ko uporabnik kupi 10 artiklov:

``` {.text breaklines="" bgcolor="gray_light"}
Cena: 1
Cena: 1
Cena: 1
Cena: 1
Cena: 1
Cena: 1
Cena: 1
Cena: 1
Cena: 1
Cena: 1
Porabili boste 10 EUR za 10 stvari.
```

### Tekoči račun 

Napišite bančni program, poimenovan `tekoci_racun.py`, kamor uporabniki
vtipkavajo prejemke in izdatke v obliki pozitivnih in negativnih zneskov
na svojem tekočem računu. Program jim sproti izpisuje stanje in se
ustavi, ko je uporabnik v minusu za 100 evrov ali več.

*Primer delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Sprememba: 23
Stanje: 23
Sprememba: 15
Stanje: 38
Sprememba: -30
Stanje: 8
Sprememba: 10
Stanje: 18
Sprememba: 100
Stanje: 118
Sprememba: -200
Stanje: -82
Sprememba: -50
Stanje: -132
Bankrot!
```

## Rešitve nalog

### Poštevanka

``` python
st = int(input("Vnos števila: "))
i = 1
while i <= 10:
    print(i * st)
    i += 1
```

### Vse po pet 

``` python
vsota = 0
i = 0
while i < 5:
    vsota += int(input('Cena artikla: '))
    i += 1
print('Vsota:', vsota)
```

Rešitev z zanko *for*:

``` python
vsota = 0
for i in range(5):
    vsota += int(input('Cena artikla: '))
print('Vsota:', vsota)
```

### Konkurenca 

``` python
vsota = 0
i = int(input('Število izdelkov: '))
while i > 0:
    vsota += int(input('Cena artikla: '))
    i -= 1
print('Vsota:', vsota)
```

Rešitev z zanko *for*:

``` python
vsota = 0
for i in range(int(input('Število izdelkov: '))):
    vsota += int(input('Cena artikla: '))
print('Vsota:', vsota)
```

### Top shop 

``` python
vsota = 0
# Spremenljivko cena najprej nastavimo na 1, da se zanka sploh začne izvajati.
cena = 1
while cena != 0:
    cena = int(input('Cena artikla: '))
    vsota += cena
print('Vsota:', vsota)
```

### Povprečna cena 

``` python
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

### Trojni stop

``` python
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

### Tekoči račun

``` python
stanje = 0
while stanje > -100:
    stanje += int(input('Sprememba: '))
    print('Stanje:', stanje)
print('Bankrot!')
```

# 4. vaje: Seznami in zanka *for*

## Naloge

### Iskanje minimuma

Napišite program `iskanje_minimuma.py`, ki poišče in izpiše najmanjši
element v seznamu celih števil brez uporabe funkcije `min()` ali
sortiranja! Seznam števil naj poda uporabnik, pri čemer lahko za
interpretacijo vhodnega niza kot seznam uporabite funkcijo `eval()`, ki
omogoča avtomatsko prepoznavo vnesenega podatkovnega tipa (v primeru seznamov je nujno treba vnesti tudi oklepaje).

Primer delovanja:

``` {.text breaklines="" bgcolor="gray_light"}
Vpišite seznam števil: [23, 42, 87, 34, 1, -3, 2]
-3
```

### Niz v seznamu 

Napišite program `niz_v_seznamu.py`, ki ugotovi, ali je nek niz vsebovan
v predhodno definiranem seznamu nizov, definiranem kot:\
`seznam = ["beseda", "spremenljivka", "niz", "zanka", "stavek", "slovar"]`.

Program naj uporabnika vpraša po nizu, ki ga išče, nato pa izpiše, ali
je ta niz vsebovan v seznamu.

Nalogo poskusite rešiti z uporabo zanke in brez nje.

*Primera delovanja programa:*

``` {.text breaklines="" bgcolor="gray_light"}
Vpišite iskani niz: zanka
Seznam vsebuje niz "zanka".

Vpišite iskani niz: vrednost
Seznam ne vsebuje niza "vrednost".
```

Testi pri tej nalogi niso občutljivi na presledke.

### Števila v seznamu 

Napišite program `stevilo_v_seznamu.py`, ki ugotovi, ali je število, ki
ga vpiše uporabnik, v predhodno definiranem seznamu celih števil. Ta
seznam je:
`seznam = [3, 35, 7, 68, 9, 10, 12, 481, 17, 12, 31, 21, 98, 33]`.

Nalogo poskusite rešiti z uporabo zanke in brez nje.

*Primera delovanja programa:*

``` {.text breaklines="" bgcolor="gray_light"}
Vpišite število: 9
Seznam vsebuje število 9

Vpišite število: 4
Seznam ne vsebuje števila 4
```

### Vsota in povprečje 

Napišite program `vsota_in_povprecje.py`, ki za podani seznam izračuna
vsoto (brez uporabe funkcije `sum`) in povprečje elementov, zaokroženo
na 5 decimalk. Seznam števil naj vnese uporabnik.

*Primer delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Vpišite seznam števil: [23, 42, 87, 34, 1, -3, 2]
186
26.57143
```

### Iskanje večkratnikov

Napišite program `iskanje_veckratnikov.py`, ki preveri, ali seznam
vsebuje vsaj en večkratnik izbranega števila. Seznam in izbrano število
poda uporabnik. Nalogo poskusite rešiti tudi z uporabo `break`.

*Primera delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Vpišite seznam števil: [23, 42, 87, 34, 1, -3, 2]
Vnesite število: 3
Vsebuje.

Vpišite seznam števil: [23, 42, 87, 34, 1, -3, 2]
Vnesite število: 8
Ne vsebuje.
```

### Samo večkratniki 

Program `iskanje_veckratnikov.py` spremenite tako, da bo preverjal, ali
seznam vsebuje zgolj večkratnike izbranega števila. Seznam in izbrano
število poda uporabnik, nalogo pa poskusite rešiti tudi z uporabo
`break`.

*Primera delovanja:*

``` {.text breaklines="" bgcolor="gray_light"}
Vpišite seznam števil: [27, 21, 3, 33, 60, -3]
Vnesite število: 3
Vsebuje.

Vpišite seznam števil: [27, 21, 3, 33, 60, -3]
Vnesite število: 9
Ne vsebuje.
```

### Izris trikotnika

Po programerski tradiciji je eden prvih programov, ki jih napišemo v
določenem programskem jeziku, izris trikotnika iz zvezdic. Napišite
program `izris_trikotnika.py`, ki vpraša uporabnika po višini
trikotnika, nato pa izpiše takšen trikotnik iz zvezdic:

``` {.text breaklines="" bgcolor="gray_light"}
Vpiši višino: 4
 *
 * *
 * * *
 * * * *
```

### Izris smrekice

Napišite program `izris_smrekice.py`, ki bo namesto trikotnikov
izrisoval ,,smrekice".

*Namig: prazni prostori in zvezdice so povezani s formulo za opis
zaporedja.*

``` {.text breaklines="" bgcolor="gray_light"}
Vpiši višino: 4
       *
     * * *
   * * * * *
 * * * * * * *
```

Testi so občutljivi na presledke, zato jih ne uporabljajte tam, kjer
niso potrebni.

## Rešitve nalog

### Iskanje minimuma 

``` python
seznam = eval(input('Vpišite seznam števil: '))
minimum = seznam[0]
for elt in seznam:
    if elt < minimum:
        minimum = elt
print(minimum)
```

### Niz v seznamu

``` python
seznam = ["beseda", "spremenljivka", "niz", "zanka", "stavek", "slovar"]
niz=input('Vpišite iskani niz: ')
if niz in seznam:
    print('Seznam vsebuje niz "'+niz+'".')
else:
    print('Seznam ne vsebuje niza "'+niz+'".')
```

### Števila v seznamu

``` python
seznam = [3, 35, 7, 68, 9, 10, 12, 481, 17, 12, 31, 21, 98, 33]
st=int(input('Vpišite število: '))
if st in seznam:
    print('Seznam vsebuje število',st)
else:
    print('Seznam ne vsebuje števila', st)
```

### Vsota in povprečje

``` python
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

### Iskanje večkratnikov

``` python
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

### Samo večkratniki 

``` python
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

### Izris trikotnika 

``` python
n = int(input('Vpiši višino: '))

for i in range(1, n + 1):
    print('*' * i)
```

### Izris smrekice 

``` python
n = int(input('Vpiši višino: '))

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
```

# 5. vaje: Funkcije

## Naloge

### Preproste funkcije 

Vse funkcije iz tega sklopa pišite v datoteko `preproste_funkcije.py`.

**Iskanje minimuma**

Napišite funkcijo `minimum(seznam)`, ki poišče in vrne najmanjšo
vrednost v podanem seznamu števil, brez da uporabite funkcijo `min()`
ali sortiranje.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> s = [23, 42, 87, 34, 1, -3, 2]
>>> minimum(s)
-3
```

**Trikotniška neenakost**

Napišite funkcijo `trikotniska_neenakost(a, b, c)`, ki preveri, ali
lahko s podanimi dolžinami stranic ($a$, $b$ in $c$) tvorimo trikotnik.
Trikotniška neenakost pravi, da trikotnik obstaja, če je vsota dolžin
poljubnih dveh stranic večja od dolžine tretje stranice.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> trikotniska_neenakost(3, 4, 5)
True
>>> trikotniska_neenakost(2, 3, 8)
False
```

**Samoglasniki**

Napišite funkcijo `samoglasnik(s)`, ki prejme znak, tj. niz dolžine 1,
in vrne `True`, če je znak samoglasnik, v nasprotnem primeru pa `False`.

*Primera pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> samoglasnik('a')
True
>>> samoglasnik('f')
False
```

**pH**

Napišite funkcijo `pH(koncentracija)`, ki prejme molarno koncentracijo
oksonijevih ionov v raztopini, vrne pa vrednost pH, izračunano po
formuli: $pH = -log_{10}(koncentracija)$.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> pH(0.0000001)
7.0
```

Izračun desetiškega logaritma omogoča funkcije `log()`, ki se nahaja v
knjižnici `math`. Knjižnico na začetku datoteke uvozite z vrstico:
`import math`.

**Prekrivajoča se seznama**

Napišite funkcijo `prekrivajoca_seznama(seznam1, seznam2)`, ki kot
argumenta sprejme dva seznama in vrne `True`, če imata seznama vsaj en
skupen element. V nasprotnem primeru naj funkcija vrača `False`.

*Primera pravilnega delovanja funkcije:*

``` text
>>> prekrivajoca_seznama([1, 2, 3], [4, 5, 6])
False
>>> prekrivajoca_seznama(['Ana', 'Peter', 'Miha'], ['Matej', 'Eva', 'Ana'])
True
```

Namig: najprej razmislite, kako ugotoviti, ali se nek podan element
nahaja v seznamu.

### Razcep na prafaktorje 

Vse funkcije iz tega sklopa pišite v datoteko `razcep.py`.

Napisati želimo funkcijo `razcep_na_prafaktorje(n)`, ki vrača razcep
števila na prafaktorje. Do celotne funkcije bomo prišli z uporabo več
pomožnih funkcij.

**Praštevilo**

Napišite funkcijo `prastevilo(n)`, ki za vnešeno število vrne, ali je
praštevilo. Število 1 ni praštevilo.

*Primera pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> prastevilo(13)
True
>>> prastevilo(22)
False
```

**Praštevila**

Napišite funkcijo `prastevila(n)`, ki vrne seznam vseh praštevil med `2`
in `n`, vključno z `2` in `n`. Pri tem si pomagajte s funkcijo
`prastevilo(n)` iz prejšnje naloge.

*Primera pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> prastevila(59)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
>>> prastevila(42)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
```

**Deljivost**

Napišite funkcijo `deljivost(n, x)`, ki vrne, kolikokrat je `n` deljiv z
`x`.

*Primeri pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> deljivost(756, 2)
2
\begin{minted}[breaklines, bgcolor=gray_light]{text}
>>> deljivost(756, 3)
3
>>> deljivost(756, 5)
0
```

Namig: Dokler je `n` deljiv z `x`, ga delite z `x` in sproti štejte,
kolikokrat ste ga delili. Ne pozabite zmanjševati `n`.

**Razcep na prafaktorje**

Napišite funkcijo `razcep_na_prafaktorje(n)`, ki razcepi število `n` na
prafaktorje. Razcep na prafaktorje je zapis števila s produktom
praštevil, npr. 252 lahko zapišemo s produktom
$2^2 \cdot 3^2 \cdot 7^1$. Funkcija naj vrne seznam seznamov, ki
predstavljajo osnovo in potenco. Pri pisanju si pomagajte s funkcijama
`prastevila(n)` in `deljivost(n, x)`.

*Primera pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> razcep_na_prafaktorje(252)
[[2, 2], [3, 2], [7, 1]]
>>> razcep_na_prafaktorje(1944)
[[2, 3], [3, 5]]
```

Namig: Funkcija naj za vsa praštevila med `2` in `n` (vključno z `2` in
`n`) ugotovi, kolikokrat delijo podano število in če ga delijo vsaj
enkrat, to doda v seznam.

### Fibonaccijevo zaporedje

Vse funkcije iz tega sklopa pišite v datoteko `fibonacci.py`.

**Fibonaccijeva števila**

Napišite funkcijo `fibonaccijeva_stevila(n)`, ki prejme število `n`,
vrne pa seznam Fibonaccijevih števil manjših od `n`.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> fibonaccijeva_stevila(90)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

**Liha Fibonaccijeva števila**

Napišite funkcijo `liha_fibonaccijeva_stevila(n)`, ki prejme število
`n`, vrne pa vsoto vseh lihih Fibonaccijevih števil manjših od `n`.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> liha_fibonaccijeva_stevila(90)
188
```

## Rešitve

### Preproste funkcije

**Iskanje minimuma**

``` python
def minimum(seznam):
    minimum = seznam[0]
    for elt in seznam:
        if elt < minimum:
            minimum = elt
    return minimum
```

**Trikotniška neenakost**

``` python
def trikotniska_neenakost(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False
```

**Samoglasniki**

``` python
def samoglasnik(s):
    if s.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
```

**pH**

``` python
from math import log10

def pH(koncentracija):
    return -log10(koncentracija)
```

**Prekrivajoča se seznama**

``` python
def prekrivajoca_seznama(seznam1, seznam2):
    for elt in seznam1:
        if elt in seznam2:
            return True
    return False
```

### Razcep na prafaktorje 

**Praštevilo**

``` python
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

**Praštevila**

Pomagamo si s funkcijo prestevilo(n) iz prejšnje naloge.

``` python
def prastevila(n):
    seznam_prastevil = []
    for i in range(2, n + 1):
        if prastevilo(i):
            seznam_prastevil += [i]
    return seznam_prastevil
```

**Deljivost**

``` python
def deljivost(n, x):
    stevec = 0
    while n % x == 0:
        n /= x
        stevec += 1
    return stevec
```

**Razcep na prafaktorje**

Pomagamo si s funkcijama prastevila(n) in deljivost(n, x).

``` python
def razcep_na_prafaktorje(n):
    seznam = []
    seznam_prastevil = prastevila(n)
    for prastevilo in seznam_prastevil:
        deli = deljivost(n, prastevilo)
        if deli > 0:
            seznam += [[prastevilo, deli]]
    return seznam
```

### Fibonaccijevo zaporedje 

**Fibonaccijeva števila**

``` python
def fibonaccijeva_stevila(n):
    f1 = 1
    f2 = 1
    stevila = [1, 1]
    while f1 + f2 < n:
        stevila += [f1 + f2]
        f2, f1 = f1, f1 + f2
    return stevila
```

**Liha Fibonaccijeva števila**

``` python
def liha_fibonaccijeva_stevila(n):
    stevila = fibonaccijeva_stevila(n)
    suma = 0
    for st in stevila:
        if st % 2 == 1:
            suma += st
    return suma
```

# 6. vaje: (Ne)spremenljivi podatkovni tipi in terke

## Naloge

### Spremenljivost 

Vse funkcije tega sklopa pišite v datoteko `spremenljivost.py`

**Korenjenje v seznamu (1)**

Napišite funkcijo `koreni_seznam(seznam)`, ki prejme seznam in spremeni
vse vrednosti v seznamu v njihove korene. Če je vrednost pod korenom
negativna, jo v seznamu prepiše v `None`.

*Primera pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> s = [0, 1, 4, 9, 16, 25]
>>> koreni_seznam(s)
>>> s
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
>>> s1 = [400, -100, 256, -1089]
>>> koreni_seznam(s1)
>>> s1
[20.0, None, 16.0, None]
```

**Korenjenje v seznamu (2)**

Napišite funkcijo `koreni_seznam2(seznam)`, ki prejme seznam in vrne
seznam korenov vrednosti podanega seznama. Če je vrednost pod korenom
negativna, naj doda v seznam vrednost `None`.

1\. primer uporabe:

``` {.text breaklines="" bgcolor="gray_light"}
>>> s = [0, 1, 4, 9, 16, 25]
>>> s2 = koreni_seznam2(s)
>>> s2
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
>>> s
[0, 1, 4, 9, 16, 25]
>>> s3 = [400, -100, 256, -1089]
>>> s4 = koreni_seznam2(s3)
>>> s4
[20.0, None, 16.0, None]
```

**Unikaten seznam**

Napišite funkcijo `unikaten_seznam(seznam)`, ki prejme seznam elementov,
vrne pa seznam, ki vsebuje elemente prvega seznama samo po enkrat.
Vrstni red elementov naj bo isti, kot je vrstni red prve pojavitve v
podanem seznamu.

*Primeri pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> unikaten_seznam([1, 2, 3, 3, 3, 3, 4, 5])
[1, 2, 3, 4, 5]
>>> unikaten_seznam([1, 2, 3, 4, 5, 1, 3, 5])
[1, 2, 3, 4, 5]
>>> unikaten_seznam([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]
```

### Terke 

Vse funkcije tega sklopa pišite v datoteko `IMDb.py`.

Podan je seznam serij, ki poleg imena serije vsebuje tudi njeno oceno na
IMDb-ju ter leto začetka predvajanja:

``` text
serije = [('Friends', 9.0, 1994),
    ('The Big Bang Theory', 8.4, 2007),
    ('Game of Thrones', 9.5, 2011),
    ('Mr. Robot', 8.7, 2015),
    ('Humans', 8.1, 2015)]
```

**Ocene**

Napišite funkcijo `ocene(serije)`, ki sprejme seznam `serije` in vrne
seznam naslovov serij, ki imajo oceno večjo ali enako 9.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> ocene(serije)
['Friends', 'Game of Thrones']
```

Naslove vrnite v istem vrstnem redu, kot so podatki v podanem seznamu.

**Najstarejša serija**

Napišite funkcijo `najstarejsa(serije)`, ki vrne ime najstarejše serije.
Predpostavite, da so vsi testni podatki taki, da je najstarejša serija
samo ena.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> najstarejsa(serije)
'Friends'
```

**Povprečna ocena**

Napišite funkcijo `povprecna_ocena(serije)`, ki vrne povprečno oceno
vseh serij v seznamu.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> povprecna_ocena(serije)
8.74
```

**Dolga imena serij**

Napišite funkcijo `dolga_imena(serije)`, ki vrne seznam imen serij, ki
so daljša od dveh besed.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> dolga_imena(serije)
['The Big Bang Theory', 'Game of Thrones']
```

Namig: pomagajte si z metodo `split()`, ki niz razbije po presledkih na
seznam nizov.

*Primer delovanja metode `split()`:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> niz = 'The Big Bang Theory'
>>> niz.split()
['The', 'Big', 'Bang', 'Theory']
```

**Krajšanje**

Napišite funkcijo `krajsanje(serije)`, ki vrne seznam terk oblike:
`(naslov, ocena)`.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> krajsanje(serije)
[('Friends', 9.0), ('The Big Bang Theory', 8.4), ('Game of Thrones', 9.5), ('Mr. Robot', 8.7), ('Humans', 8.1)]
```

**Najnovejše serije**

Napišite funkcijo `najnovejse(serije)`, ki vrne seznam imen najnovejših
serij iz podanega seznama serij. Naslovi serij naj bodo v istem vrstnem
redu kot v seznamu serij.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> najnovejse(serije)
['Mr. Robot', 'Humans']
```

## Rešitve

### Spremenljivost 

**Korenjenje v seznamu (1)**

``` python
def koreni_seznam(seznam):
    for i in range(len(seznam)):
        if seznam[i] >= 0:
            seznam[i] = seznam[i] ** 0.5
        else:
            seznam[i] = None
```

**Korenjenje v seznamu (2)**

``` python
def koreni_seznam2(seznam):
    s=[]
    for elt in seznam:
        if elt >= 0:
            s.append(elt ** 0.5)
        else:
            s.append(None)
    return s
```

**Unikaten seznam**

``` python
def unikaten_seznam(s):
    unikati = []
    for elt in s:
        if elt not in unikati:
            unikati += [elt]
    return unikati
```

### Terke 

**Ocene**

``` python
def ocene(serije):
    seznam = []
    for naslov, ocena, leto in serije:
        if ocena >= 9.0:
            seznam.append(naslov)
    return seznam
```

**Najstarejša serija**

``` python
def najstarejsa(serije):
    naj_naslov, naj_ocena, naj_leto =serije[0]
    for naslov, ocena, leto in serije:
        if leto < naj_leto:
            naj_naslov = naslov
            naj_leto = leto
    return naj_naslov
```

**Povprečna ocena**

``` python
def povprecna_ocena(serije):
    if len(serije) == 0:
        return 0
    suma = 0
    for naslov, ocena, leto in serije:
        suma += ocena
    return suma / len(serije)
```

**Dolga imena serij**

``` python
def dolga_imena(serije):
    seznam = []
    for naslov, ocena, leto in serije:
        if len(naslov.split()) > 2:
            seznam.append(naslov)
    return seznam
```

**Krajšanje**

``` python
def krajsanje(serije):
    seznam = []
    for naslov, ocena, leto in serije:
        seznam.append((naslov, ocena))
    return seznam 
```

**Najnovejše serije**

``` python
def najnovejse(serije):
    naj_naslov = []
    if len(serije) == 0:
        return naj_naslov
    
    naj_leto =serije[0][2]
    for serija in serije:
        if serija[2] > naj_leto:
            naj_leto = serija[2]
            
    for naslov, ocena, leto in serije:
        if leto == naj_leto:
            naj_naslov.append(naslov)

    return naj_naslov
```

# 7. vaje: Slovarji

## Naloge

Funkcije shranite v datoteko `trgovina.py`.

Podan je seznam izdelkov v trgovini, ki poleg imena izdelka vsebuje tudi
njegovo ceno in zalogo:

``` {.text breaklines="" bgcolor="gray_light"}
izdelki = [('mleko', 0.86, 128),
    ('jogurt', 0.49, 56),
    ('piškoti', 2.99, 73),
    ('sok', 1.79, 104),
    ('jajce', 0.1, 103),
    ('moka', 1.39, 99),
    ('makaroni', 1.89, 67),
    ('paradižnik', 0.23, 35),
    ('kruh', 2.19, 43),
    ('hrenovka', 1.99, 28),
    ('gorgonzola', 2.69, 32)]
```

### V slovar 

Napišite funkcijo `v_slovar`, ki kot argument sprejme seznam `izdelki`.
Funkcija naj vrača slovar, kjer kot ključi nastopajo imena izdelkov,
vrednosti pa so seznami oblike `[cena, zaloga]`.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> v_slovar(izdelki)
{'mleko': [0.86, 128], 'hrenovka': [1.99, 28], 'jogurt': [0.49, 56], 'sok': [1.79, 104], 'moka': [1.39, 99], 'paradižnik': [0.23, 35], 'gorgonzola': [2.69, 32], 'makaroni': [1.89, 67], 'kruh': [2.19, 43], 'piškoti': [2.99, 73], 'jajce': [0.1, 103]}
```

### Število izdelkov 

Napišite funkcijo `stevilo_izdelkov(zaloga)`, ki kot argument sprejme
slovar, kot ga vrača funkcija `v_slovar` (tj. slovar `zaloga`). Funkcija
naj vrne število vseh izdelkov v trgovini.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> zaloga = v_slovar(izdelki)
>>> stevilo_izdelkov(zaloga)
768
```

### Nakupovalna košara

Napišite funkcijo `nakupovalna_kosara`, ki kot argument prejme seznam
vsebine nakupovalne košare. Funkcija naj vrača slovar, kjer so ključi
imena izdelkov, vrednosti pa število izdelkov.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> seznam = ['jogurt', 'mleko', 'jogurt', 'jogurt', 'piškoti']
>>> nakupovalna_kosara(seznam)
{'jogurt': 3, 'mleko': 1, 'piškoti': 1}
```

### Cena 

Napišite funkcijo `cena`, ki sprejme dva argumenta: slovar zaloge, kot
ga vrača funkcija `v_slovar` (tj. slovar `zaloga`) in slovar nakupov,
kot ga vrača funkcija `nakupovalna_kosara`. Funkcija `cena` naj vrne
znesek, ki ga mora plačati kupec.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> zaloga = v_slovar(izdelki)
>>> seznam = ['jogurt', 'mleko', 'jogurt', 'jogurt', 'piškoti']
>>> slovar_nakupov = nakupovalna_kosara(seznam)
>>> cena(zaloga, slovar_nakupov)
5.32
```

### Popravek zaloge 

Napišite funkcijo `popravek_zaloge(zaloga, izdelek, popravek)`, ki
spremeni slovar `zaloga` tako, da zalogo izdelka, podanega v argumentu
`izdelek`, spremeni glede na argument `popravek` in vrne novo vrednost
zaloge. Popravek je lahko negativen ali pozitiven. Če bi popravek
spremenil zalogo na negativno, naj funkcija zaloge ne spremeni in vrne
`None`.

*Primera pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> zaloga = v_slovar(izdelki)
>>> popravek_zaloge(zaloga, 'sok', 100)
204
>>> zaloga
{'mleko': [0.86, 128], 'hrenovka': [1.99, 28], 'moka': [1.39, 99], 'sok': [1.79, 204], 'makaroni': [1.89, 67], 'kruh': [2.19, 43], 'jogurt': [0.49, 56], 'paradižnik': [0.23, 35], 'piškoti': [2.99, 73], 'gorgonzola': [2.69, 32], 'jajce': [0.1, 103]}
```

``` {.text breaklines="" bgcolor="gray_light"}
>>> zaloga = v_slovar(izdelki)
>>> popravek_zaloge(zaloga, 'jogurt', -60)
>>>
```

### Blagajna 

Napišite funkcijo `blagajna`, ki kot argumenta sprejme slovar zaloge,
kot ga vrača funkcija `v_slovar` in slovar nakupov, kot ga vrača
funkcija `nakupovalna_kosara`. Funkcija `blagajna` naj spremeni slovar
`zaloga` glede na količino izdelkov v slovarju nakupov in hkrati vrne
znesek, ki ga mora plačati kupec. Kupec ne more kupiti več izdelkov kot
jih je v zalogi.

Pomagajte si s funkcijami, ki ste jih napisali do sedaj.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> zaloga = v_slovar(izdelki)
>>> seznam = ['jogurt', 'mleko', 'jogurt', 'jogurt', 'piškoti']
>>> slovar_nakupov = nakupovalna_kosara(seznam)
>>> blagajna(zaloga, slovar_nakupov)
5.32
>>> zaloga
{'paradižnik': [0.23, 35], 'kruh': [2.19, 43], 'mleko': [0.86, 127], 'jajce': [0.1, 103], 'piškoti': [2.99, 72], 'moka': [1.39, 99], 'jogurt': [0.49, 53], 'hrenovka': [1.99, 28], 'sok': [1.79, 104], 'makaroni': [1.89, 67], 'gorgonzola': [2.69, 32]}
```

### Kuhanje 

V slovarju `jedi` kot ključi nastopajo imena jedi, vrednosti pa so
slovarji z imenom sestavine in potrebno količino za pripravo 1 obroka:

``` {.text breaklines="" bgcolor="gray_light"}
jedi = {    "palačinke": {"jajce": 3, "mleko": 1, "moka": 1},
    "šmorn": {"jajce": 3, "mleko": 1, "moka": 1},
    "hrenovke": {"hrenovka": 2, "kruh": 1},
    "makaroni": {"makaroni": 1, "paradižnik": 3, "gorgonzola": 1},
    "piškoti": {"piškoti": 1}}
```

Napišite funkcijo `kuhanje(zaloga, jedi, jed)`, ki vrne ceno izdelkov
potrebnih za pripravo izbrane jedi.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> zaloga = v_slovar(izdelki)
>>> kuhanje(zaloga, jedi, 'palačinke')
2.55
```

### Obrok 

Napišite funkcijo `posamezna_jed(jedi, jed, obrokov)`, ki kot argumente
sprejme slovar receptov jedi (tj. `jedi`), ime jedi (argument `jed` v
obliki niza (`str`)), ki jo želimo pripraviti in število obrokov v
obliki števila (`int`). Funkcija naj vrača slovar s potrebnimi
količinami sestavin za izbrano jed.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> posamezna_jed(jedi, "šmorn", 4)
{'moka': 4, 'mleko': 4, 'jajce': 12}
```

### Nakup 

Napišite funkcijo `nakup(jedi, obroki)`, ki kot argumenta sprejme slovar
jedi (tj. `jedi`) in število obrokov. Funkcija naj vrača slovar, kjer
kot ključi nastopajo potrebne sestavine, kot vrednosti pa količine teh
sestavin, potrebnih za pripravo vseh obrokov.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> obroki = [("makaroni", 20), ("palačinke", 15), ("šmorn", 10), ("hrenovke", 5)]
>>> nakup(jedi, obroki)
{'paradižnik': 60, 'gorgonzola': 20, 'moka': 25, 'kruh': 5, 'hrenovka': 10, 'jajce': 75, 'makaroni': 20, 'mleko': 25}
```

### Primanjkljaj

Napišite funkcijo `primanjkljaj(zaloga, jedi, obroki)`, ki kot argumente
sprejme zalogo trgovine, seznam jedi in količino obrokov. Funkcija naj
vrača slovar, v katerem kot ključi nastopajo sestavine, kot vrednosti pa
pripadajoče količine sestavin, ki jih morajo v trgovini dokupiti glede
na obroke.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> zaloga = v_slovar(izdelki)
>>> obroki = [("makaroni", 20), ("palačinke", 15), ("šmorn", 10), ("hrenovke", 25)]
>>> primanjkljaj(zaloga, jedi, obroki)
{'hrenovka': 22, 'paradižnik': 25}
```

## Rešitve nalog

### V slovar 

``` python
def v_slovar(izdelki):
    cene = {}
    for izdelek, cena, zaloga in izdelki:
        cene[izdelek] = [cena, zaloga]
    return cene
```

### Število izdelkov 

``` python
def stevilo_izdelkov(zaloga):
    vsota = 0
    for izdelek, vrednost in zaloga.items():
        cena, zaloga = vrednost
        vsota += zaloga
    return vsota
```

### Nakupovalna košara 

``` python
def nakupovalna_kosara(seznam):
    slovar = {}
    for izdelek in seznam:
        if izdelek not in slovar:
            slovar[izdelek] = 0
        slovar[izdelek] += 1
    return slovar
```

### Cena 

``` python
def cena(zaloga, slovar_nakupov):
    znesek = 0
    for izdelek, kolicina in slovar_nakupov.items():
        znesek += kolicina * zaloga[izdelek][0]
    return znesek
```

### Popravek zaloge 

``` python
def popravek_zaloge(zaloga, izdelek, popravek):
    nova_zaloga = zaloga[izdelek][1] + popravek
    if nova_zaloga >= 0:
        zaloga[izdelek][1] = nova_zaloga
        return nova_zaloga
    else:
        return None
```

### Blagajna 

``` python
def blagajna(zaloga, slovar_nakupov):
    for izdelek, kolicina in slovar_nakupov.items():
        popravek_zaloge(zaloga, izdelek, -kolicina)
    return cena(zaloga, slovar_nakupov)
```

### Kuhanje 

``` python
def kuhanje(zaloga, jedi, jed):
    cena = 0
    for sestavina, kolicina in jedi[jed].items():
        cena += kolicina * zaloga[sestavina][0]
    return cena
```

### Obrok 

``` python
def posamezna_jed(jedi, jed, obrokov):
    sestavine = {}
    for sestavina, kolicina in jedi[jed].items():
        sestavine[sestavina] = kolicina * obrokov
    return sestavine
```

### Nakup 

``` python
def nakup(jedi, obroki):
    sestavine = {}
    for jed, obrokov in obroki:
        for sestavina, kolicina in posamezna_jed(jedi, jed, obrokov).items():
            if sestavina not in sestavine:
                sestavine[sestavina] = 0
            sestavine[sestavina] += kolicina
    return sestavine
```

### Primanjkljaj 

``` python
def primanjkljaj(zaloga, jedi, obroki):
    sestavine = nakup(jedi, obroki)
    slovar = {}
    for sestavina, kolicina in sestavine.items():
        if zaloga[sestavina][1] < kolicina:
            slovar[sestavina] = kolicina - zaloga[sestavina][1]
    return slovar
```

# 8. vaje: Množice in metode

## Naloge

Funkcije shranite v datoteko `metode.py`.

### Besede z a-ji

Napišite funkcijo `aa_besede`, ki kot argument sprejme niz, vrne pa
množico besed iz niza, ki vsebujejo vsaj dve črki `a`. Funkcija naj ne
bo občutljiva na velikost črk, v množici naj ne bo ločil. Predpostavite
lahko, da bo edino ločilo v testnih primerih pika (`.`).

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> aa_besede('Anja je v trgovini kupila ananas in jabolka.')
{'ananas', 'Anja', 'jabolka'}
```

### Najdaljše besede 

Napišite funkcijo `najdaljse_besede`, ki kot argument sprejme niz, vrne
pa množico najdaljših besed v podanem nizu. Predpostavite lahko, da
bosta edini ločili v testnih nizih pika (`.`) in vejica (`,`).

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> najdaljse_besede('Univerza v Ljubljani')
{'Ljubljani'}
```

### Inicialke 

Napišite funkcijo `velike_zacetnice`, ki kot argument sprejme niz.
Funkcija naj vrača spremenjen niz, v katerem vsem besedam, daljšim od
dveh znakov, spremeni prvo črko v veliko začetnico.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> velike_zacetnice('V trgovini je kupila ananas in jabolka.')
'V Trgovini je Kupila Ananas in Jabolka.'
```

### Unikaten seznam 

Napišite funkcijo `razlicne_skladbe`, ki kot argument sprejme seznam
poslušanih skladb in vrne število različnih skladb.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> razlicne_skladbe(['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me', 'Imagine', 'Stairway To Heaven', 'One', 'Imagine'])
6
```

### Prijatelji 

Napišite funkcijo `skupne`, ki kot argumenta sprejme dva seznama.
Seznama vsebujeta naslove poslušanih skladb dveh prijateljev. Funkcija
naj vrne množico skladb, ki so na obeh seznamih.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> skupne(['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me'], ['Imagine', 'Stairway To Heaven', 'One', 'Imagine'])
{'Imagine', 'One'}
```

### Repertoar 

Napišite funkcijo `repertoar`, ki kot argumenta sprejme dva seznama
predvajanj dveh prijateljev. Funkcija naj vrača množico skladb, ki so na
enem ali drugem ali obeh seznamih.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> repertuar(['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me'], ['Imagine', 'Stairway To Heaven', 'One', 'Imagine'])
{'Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me', 'Stairway To Heaven'}
```

### Unikati

Napišite funkcijo `unikatna_predvajanja(seznam1, seznam2)`, ki sprejme
seznama predvajanj dveh prijateljev. Funkcija naj vrne množico skladb,
ki so na enem ali drugem seznamu, ne pa na obeh.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> unikatna_predvajanja(['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me'], ['Imagine', 'Stairway To Heaven', 'One', 'Imagine'])
{'Let It Be', 'The River', 'Stand By Me', 'Stairway To Heaven'}
```

### Ponavljajoči se znaki 

Napišite funkcijo `ponavljajoci_znaki`, ki kot argument sprejme niz.
Funkcija naj vrne množico terk oblike: `(znak, število)`, pri čemer
`število` ponazarja število ponovitev znaka v izbranem nizu. Funkcija
naj vrne le tiste znake, ki se pojavijo več kot enkrat. Prav tako naj bo
občutljiva na velikost črk.

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> ponavljajoci_znaki('otorinolaringologija')
{('l', 2), ('i', 3), ('r', 2), ('a', 2), ('g', 2), ('o', 5), ('n', 2)}
```

### Onesnaženost z delci PM10 

Agencija Republike Slovenije za okolje (ARSO) nas je prosila, da
naredimo analizo onesnaženosti z delci PM10 v treh največjih slovenskih
mestih (Ljubljana, Maribor in Celje) ter primerjamo podatke z merilno
postajo Iskrba[^3].

Napišite funkcijo `najveckrat_onesnazena_mesta`, ki sprejme dva
argumenta: seznam mesečnih podatkov o onesnaženosti (podan kot seznam
terk z dnevnimi meritvami merilnih postaj) in seznam krajev. Funkcija
naj vrne množico vseh krajev, v katerih je bila največkrat dosežena
oz. presežena mejna vrednost 50 $\mu$g/m$^3$. Takih krajev je lahko več
ali pa jih sploh ni -- v tem primeru naj funkcija vrne prazno množico.

Seznam dnevnih meritev za en mesec vsebuje 28, 30 ali 31 terk, vsaka
izmed njih pa predstavlja podatke za en dan v mesecu. Vsaka terka ima
dva elementa: dan v mesecu in terko, v kateri so podatki o povprečni
dnevni koncentraciji delcev PM10 merilnih postaj Ljubljana, Maribor,
Celje ter Iskrba. Podatki so vedno podani v tem vrstnem redu postaj.
Podatki so podani v enotah $\mu$g/m$^3$. Lahko se zgodi, da kakšne
meritve manjkajo, kar je v terki označeno z `None`.

Primer podatkov za januar 2017:

``` {.text breaklines="" bgcolor="gray_light"}
kraji = ["Ljubljana", "Maribor", "Celje", "Iskrba"]
januar = [
    (1, (126, 88, None, 12)),
    (2, (53, 68, 77, 13)),
    (3, (34, 81, 96, 8)),
    (4, (None, 69, 117, 12)),
    (5, (31, 19, 51, 6)),
    (6, (13, 16, 16, 5)),
    (7, (22, 34, 42, 11)),
    (8, (39, 50, 58, 8)),
    (9, (66, 71, 90, 16)),
    (10, (41, 50, 52, 28)),
    (11, (62, 67, 82, 18)),
    (12, (73, 77, 29, 5)),
    (13, (12, 15, 19, 3)),
    (14, (34, 14, 57, 8)),
    (15, (48, 18, 82, 11)),
    (16, (32, 23, 72, 12)),
    (17, (15, 24, 28, 19)),
    (18, (23, 34, 36, 22)),
    (19, (38, 56, 65, 27)),
    (20, (51, 72, None, 17)),
    (21, (67, 101, None, 25)),
    (22, (70, 138, 142, 40)),
    (23, (78, 170, 146, 67)),
    (24, (96, 106, 105, 82)),
    (25, (56, 74, 73, 26)),
    (26, (31, 51, 75, 22)),
    (27, (40, 62, 66, 22)),
    (28, (81, 94, 116, 29)),
    (29, (101, 100, 109, 68)),
    (30, (83, 99, 102, 42)),
    (31, (110, 146, 115, 5))
]
```

*Primer pravilnega delovanja funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> najveckrat_onesnazena_mesta(januar, kraji)
{'Maribor', 'Celje'}
```

## Rešitve nalog

### Besede z a-ji 

``` python
def aa_besede(s):
    mn = set()
    for beseda in s.replace('.','').split():
        if beseda.lower().count('a') > 1:
            mn.add(beseda)
    return mn
```

### Najdaljše besede 

``` python
def najdaljse_besede(s):
    najdaljsa = 0
    besede = s.replace('.','').replace(',','').split()
    for beseda in besede:
        if len(beseda) > najdaljsa:
            najdaljsa = len(beseda)

    mn = set()
    for beseda in besede:
        if len(beseda) == najdaljsa:
            mn.add(beseda) 
    return mn
```

### Inicialke 

``` python
def velike_zacetnice(s):
    seznam = []
    for beseda in s.split():
        if len(beseda.replace('.','').replace(',','')) > 2:
            beseda = beseda.capitalize()
        seznam.append(beseda)
    return " ".join(seznam)
```

Če niste našli metode `capitalize`, lahko nalogo rešite tudi tako:\
`beseda = beseda[0].upper()+beseda[1:]`

### Unikaten seznam 

``` python
def razlicne_skladbe(seznam):
    return len(set(seznam))
```

### Prijatelji 

``` python
def skupne(seznam1, seznam2):
    return set(seznam1) & set(seznam2)
```

### Repertoar

``` python
def repertuar(seznam1, seznam2):
    return set(seznam1) | set(seznam2)
```

### Unikati

``` python
def unikatna_predvajanja(seznam1, seznam2):
    return set(seznam1) ^ set(seznam2)
```

### Ponavljajoči se znaki 

``` python
def ponavljajoci_znaki(niz):
    mn = set()
    for znak in niz:
        c=niz.count(znak)
        if c > 1:
            mn.add((znak,c))
    return mn
```

### Onesnaženost z delci PM10 
``` python
def najveckrat_onesnazena_mesta(podatki, kraji):
    mesta = [0] * len(kraji)
    for dan,postaje in podatki:
        for i in range(len(postaje)):
            if postaje[i] is not None and postaje[i] >= 50:
                mesta[i] += 1
    naj = max(mesta)
    if naj == 0:
        return(set())
    else:
        maksimumi = set()
        for i in range(len(kraji)):
            if mesta[i] == naj:
                maksimumi.add(kraji[i])
        return maksimumi
```

# 9. vaje: Datoteke

## Naloge

### Filmi

Vse funkcije tega sklopa shranite v datoteko `filmi.py`.

Datoteka `filmi.txt` se nahaja v podimeniku `podatki` imenika s testi.

**Preberi**

Napišite funkcijo `preberi`, ki kot argument sprejme ime datoteke v
obliki niza (`str`). Funkcija naj prebere datoteko in vrne niz, zapisan
v njej.

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> print(preberi('podatki/filmi.txt'))
The Godfather;9.2;Kriminalka;1972
Schindler's List;8.9;Drama;1993
Casablanca;8.6;Drama;1942
Forrest Gump;8.8;Komedija;1994
The Sound of Music;8.0;Glasbena biografija;1965
Gladiator;8.5;Akcija;2000
Titanic;7.7;Romantična drama;1997
Saving Private Ryan;8.6;Akcija;1998
```

**V seznam**

Napišite funkcijo `v_seznam(datoteka)`, ki prebere datoteko in vrne
vsebino v obliki seznama seznamov oblike: `[naslov, ocena, zanr, leto]`.

Pri tem naj bosta spremenljivki `naslov` in `zanr` v obliki niza
(`str`), spremenljivka `ocena` naj bo decimalno število (`float`),
`leto` pa v obliki celega števila (`int`).

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> v_seznam('podatki/filmi.txt')
[['The Godfather', 9.2, 'Kriminalka', 1972], ["Schindler's List", 8.9, 'Drama', 1993], ['Casablanca', 8.6, 'Drama', 1942], ['Forrest Gump', 8.8, 'Komedija', 1994], ['The Sound of Music', 8.0, 'Glasbena biografija', 1965], ['Gladiator', 8.5, 'Akcija', 2000], ['Titanic', 7.7, 'Romantična drama', 1997], ['Saving Private Ryan', 8.6, 'Akcija', 1998]]
```

**V slovar**

Napišite funkcijo `v_slovar`, ki kot argument sprejme ime datoteke.
Funkcija naj vrne slovar, kjer so ključi žanr filma, vrednosti pa seznam
naslovov, ki ustrezajo temu žanru.

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> v_slovar('podatki/filmi.txt')
{'Romantična drama': ['Titanic'], 'Kriminalka': ['The Godfather'], 'Akcija': ['Gladiator', 'Saving Private Ryan'], 'Drama': ["Schindler's List", 'Casablanca'], 'Komedija': ['Forrest Gump'], 'Glasbena biografija': ['The Sound of Music']}
```

**Najljubši film**

Napišite funkcijo `najljubsi(datoteka_pisanja)`, ki vpraša uporabnika po
najljubšem filmu in v novo datoteko, poimenovano `datoteka_pisanja`,
zapiše naslov tega filma.

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> najljubsi('podatki/najljubsi_film.txt')
Najljubši film: Forrest Gump
```

V datoteki `najljubsi_film.txt` je sedaj viden zapis:

``` text
Forrest Gump
```

**Zapis**

Napišite funkcijo `zapis(datoteka_branja, datoteka_pisanja)`, ki kot
argumenta sprejme dva niza z imenoma datoteke branja in datoteke
pisanja. Funkcija naj prebere vsebino datoteke branja in v novo
datoteko, tj. datoteko pisanja, zapiše naslove filmov, urejene po
abecedi.

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> zapis('podatki/filmi.txt', 'podatki/imena_filmov.txt')
```

V datoteki `imena_filmov.txt` je sedaj viden zapis:

``` text
Casablanca
Forrest Gump
Gladiator
Saving Private Ryan
Schindler's List
The Godfather
The Sound of Music
Titanic
```

**CSV**

Datoteka `ratings.csv` vsebuje podatke o ocenah več filmov s strani več
tisoč ocenjevalcev.

Primer vsebine datoteke `ratings.csv`:

``` text
userId,movieId,rating,timestamp
1,2,3.5,1112486027
1,29,3.5,1112484676
1,32,3.5,1112484819
1,47,3.5,1112484727
1,50,3.5,1112484580
1,112,3.5,1094785740
1,151,4.0,1094785734
1,223,4.0,1112485573
1,253,4.0,1112484940
```

Napišite funkcijo `ocena_filma`, ki kot argumenta sprejme id_filma,
zapisanega kot `int` in ime csv_datoteke. Funkcija naj za podani film
vrne njegovo povprečno oceno.

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> ocena_filma(2, 'podatki/ratings.csv')
3.2296978281397544
```

### Oliver Twist 

Vse naloge tega sklopa shranite v datoteko `knjiga.py`.

Za reševanje potrebujete datoteko [`OliverTwist.txt`](http://www.gutenberg.org/ebooks/730).

**Število besed**

Napišite funkcijo `stevilo_besed(datoteka)`, ki prebere izbrano datoteko
in vrne število besed, ki se pojavijo v knjigi. Besedilo lahko le ločite
po presledkih, odstranjevanje drugih ločil ni potrebno.

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> stevilo_besed('OliverTwist.txt')
158041
```

**Različni znaki**

Napišite funkcijo `razlicni_znaki(datoteka)`, ki prebere izbrano
datoteko in vrne število različnih znakov, ki se pojavijo v knjigi.

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> razlicni_znaki('OliverTwist.txt')
70
```

**Najpogostejši znak**

Napišite funkcijo `najpogostejsi_znak(datoteka)`, ki prebere datoteko in
vrne **znak**, ki se v datoteki pojavi največkrat.

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> najpogostejsi_znak('OliverTwist.txt')
' '
```
 (Vrnjen znak je presledek.)

**Hapax legomenon**

Napišite funkcijo `hapax(datoteka)`, ki prebere izbrano datoteko in vrne
število besed, ki se v knjigi Oliver Twist pojavijo natanko enkrat.
Besedilo lahko le ločite po presledkih, odstranjevanje drugih ločil ni
potrebno.

*Primer pravilne izvedbe funkcije:*

``` {.text breaklines="" bgcolor="gray_light"}
>>> hapax('OliverTwist.txt')
11851
```

## Rešitve nalog

### Filmi 

**Preberi**

``` python
def preberi(datoteka):
    f = open(datoteka, 'r', encoding='utf8')
    tekst = f.read()
    f.close()
    return tekst
```

**V seznam**

``` python
def v_seznam(datoteka):
    seznam = []
    for vrstica in open(datoteka, 'r', encoding='utf8'):
        film, ocena, zanr, leto = vrstica.split(';')
        seznam.append([film, float(ocena), zanr, int(leto)])
    return seznam
```

**V slovar**

``` python
def v_slovar(datoteka):
    slovar = {}
    for vrstica in open(datoteka, 'r', encoding='utf8'):
        film, ocena, zanr, leto = vrstica.split(';')
        if zanr not in slovar:
            slovar[zanr] = []
        slovar[zanr].append(film)
    return slovar
```

**Najljubši film**

``` python
def najljubsi(datoteka_pisanja):
    naj = input("Najljubši film: ")
    f = open(datoteka_pisanja, 'w', encoding='UTF-8')
    print(naj, file=f)
    f.close()
```

**Zapis**

``` python
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

**CSV**

``` python
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

### Oliver Twist 

**Število besed**

``` python
def stevilo_besed(datoteka):
    f = open(datoteka, 'r', encoding='UTF-8')
    tekst = f.read()
    f.close()
    return len(tekst.split())
```

**Različni znaki**

``` python
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

**Najpogostejši znak**

``` python
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

**Hapax legomenon**

``` python
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
