Pri reševanju pazite, da se vaši izpisi ujemajo z izpisi v navodilih (vključno s presledki). Testirate s testnimi skriptami, ki jih dobite v mapi `vaje01_testi`.

ZIP-datoteko s testi razpakirajte v enega od imenikov, kjer imate pravice za pisanje. Vsaka naloga ima svoj podimenik, v katerem so testi. Svoj program ustrezno poimenujte in shranite v imenik poleg testne skripte `test.py`. Teste poženete tako, da požnete program test.py (lahko preko IDLE ali konzole).

## 1. naloga: Kako ti je ime?

Napišite program `ime.py`, ki uporabnika povpraša najprej po imenu in na zaslon izpiše dolžino tega imena.  
Primer uporabe:
```
Vpiši ime: Janez 
Dolžina imena Janez je 5
```
## 2. naloga: Pitagorov izrek

Napišite program `pitagorov_izrek.py`, ki uporabnika vpraša po dolžinah katet pravokotnega trikotnika in izpiše dolžino hipotenuze. Program naj omogoča vnos decimalnih števil. Rezultat v izpisu zaokrožite na eno decimalno mesto za decimalno vejico.  
Primer uporabe:
```
Vpiši dolžino prve katete: 3
Vpiši dolžino druge katete: 4
Dolžina hipotenuze: 5.0
```
## 3. naloga: Ploščina pravokotnega trikotnika

Program iz prejšnje naloge spremenite tako, da izračuna in izpiše ploščino pravokotnega trikotnika. Program shranite kot `ploscina.py`. Oba rezultata v izpisu zaokrožite na dve decimalni mesti natančno.

Primer uporabe:
```
Vpiši dolžino prve katete: 3
Vpiši dolžino druge katete: 4  
Dolžina hipotenuze: 5.0
Ploščina trikotnika: 6.0
```
## 4. naloga: Molska masa

Bakrov(II) sulfat je kemijska spojina s formulo CuSO4. Spojina ima pravzaprav več kemijskih formul, ki so odvisne od stopnje hidratacije. Tako je [modra galica](https://sl.wikipedia.org/wiki/Galica) bakrov(II) sulfat pentahidrat s formulo CuSO4·5H2O.  
  
Napišite program `molska_masa.py`, ki na podlagi uporabnikovega vnosa stopnje hidratacije, oz. števila molekul vode (x), izračuna molsko maso za CuSO4(H2O)x ! Podatki o relativnih atomskih masah so sledeči:
```
Cu = 63.5
S = 32.1
O = 16.0
H = 1.0
```
Primer uporabe:
```
Stopnja hidratacije: 5
Molska masa je 249.6 g/mol.
```