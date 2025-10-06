Sledijo trije sklopi nalog. Funkcije v posameznem sklopu shranite v Pythonovo datoteko in jo poimenujte kot piše v navodilih. Testi so na voljo v mapi. Datoteke shranite v ustrezen imenik `vaje05/ime_sklopa`. Teste poženete, kot ponavadi, tako da poženete `test.py` za vsak sklop nalog posebej. Vhodne podatke (v testih enot) najdete v imeniku `public/unit_test`.

# Preproste funkcije

Funkcije shranite v datoteko `preproste_funkcije.py`
  
## 1. naloga: Iskanje minimuma  
  

Napišite funkcijo `minimum(seznam)`, ki poišče in vrne najmanjšo vrednost v podanem seznamu števil (brez uporabe funkcije `min()` ali sortiranja)!

Primer klica funkcije:
```
>>>  s = [23, 42, 87, 34, 1, -3, 2]  
>>>  minimum(s)  
-3
```
## 2. naloga: Trikotniška neenakost

Napišite funkcijo `trikotniska_neenakost(a, b, c)`, ki preveri in vrne odgovor, ali lahko s podanimi dolžinami stranic (a, b in c) tvorimo trikotnik. Spomnite se na [trikotniško neenakost](https://sl.wikipedia.org/wiki/Trikotnik#Trikotni.C5.A1ka_neenakost).  
  
1. primer klica funkcije:

```
>>>  trikotniska_neenakost(3, 4, 5)
True
```

2. primer klica funkcije:
```
>>>  trikotniska_neenakost(2, 3, 8)
False
```
## 3. naloga: Samoglasniki

Napišite funkcijo `samoglasnik(s)`, ki prejme znak (niz dolžine 1) in vrne `True`, če je znak samoglasnik (glede na slovensko abecedo) in `False` drugače.  
  
1. primer klica funkcije:
```
>>>  samoglasnik('a')
True
```
2. primer klica funkcije:
```
>>>  samoglasnik('f')
False
```
## 4. naloga: pH

Napišite funkcijo `pH(koncentracija)`, ki prejme molarno koncentracijo oksonijevih ionov v raztopini (v mol/dm3 oz. mol/L), vrne pa vrednost [pH](https://sl.wikipedia.org/wiki/PH).

Primer klica funkcije:
```
>>>  pH(0.0000001)  
7.0
```
Namig: pomagajte si s knjižnico `math`. Pomoč za knjižnico ali posamezno funkcijo dobite s pomočjo funkcije `help`, npr. `help(math)`, pri čemer morate knjižnico `math` predhodno uvoziti.

## 5. naloga: Prekrivajoča se seznama

Napišite funkcijo `prekrivajoca_seznama(seznam1, seznam2)`, ki sprejme dva seznama in vrne `True`, če imata seznama vsaj en skupen element (torej njun presek ni prazen) in `False` drugače.  
  
1. primer klica funkcije:
```
>>>  prekrivajoca_seznama([1, 2, 3], [4, 5, 6])
False
```
2. primer klica funkcije:
```
>>>  prekrivajoca_seznama(['Ana', 'Peter', 'Miha'], ['Matej', 'Eva', 'Ana'])
True
```
Namig: najprej lahko rešite podproblem, kako ugotoviti, ali se nek podan element nahaja v seznamu; nato to rešitev uporabite za več elementov.  
  

# Razcep na prafaktorje

  
Napisati želimo funkcijo `razcep_na_prafaktorje(n)`, ki nam vrne [razcep števila na prafaktorje](https://sl.wikipedia.org/wiki/Pra%C5%A1tevilski_razcep). Ker gre za dokaj kompleksno nalogo, smo jo razkosali na več podnalog (6. - 9.). Nekatere izmed nalog smo delno rešili že na kakšni od prejšnjih vaj:

Funkcije shranite v datoteko `razcep.py`  
  

## 6. naloga: Praštevilo

Napišite funkcijo `prastevilo(n)`, ki za vnešeno število vrne, ali je praštevilo.  
  
1. primer uporabe:
```
>>>  prastevilo(13)
True
```
2. primer uporabe:
```
>>>  prastevilo(22)
False
```
## 7. naloga: Praštevila

Napišite funkcijo `prastevila(n)`, ki vrne seznam vseh praštevil med `2` in `n` (vključno z `2` in `n`).  
  
1. primer uporabe:
```
>>>  prastevila(59)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
```
2. primer uporabe:
```
>>>  prastevila(42)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
```
Namig: Pomagajte si s funkcijo `prestevilo(n)` iz prejšnje naloge. Za vsako število med `2` in `n` pokličite funkcijo `prestevilo(n)` in če le-ta vrne `True`, dodajte število v seznam praštevil.

## 8. naloga: Deljivost

Napišite funkcijo `deljivost(n, x)`, ki vrne, kolikokrat je `n` deljiv z `x`.  
  
1. primer uporabe:
```
>>>  deljivost(756, 2)
2
```
2. primer uporabe:
```
>>>  deljivost(756, 3)
3
```
3. primer uporabe:
```
>>>  deljivost(756, 5)
0
```
Namig: Dokler je `n` deljiv z `x`, ga delite z `x` in sproti štejte, kolikokrat ste ga deljili. Ne pozabite zmanjševati `n`.

## 9. naloga: Razcep na prafaktorje

Napišite funkcijo `razcep_na_prafaktorje(n)`, ki razcepi število `n` na prafaktorje. Razcep na prafaktorje je zapis števila s produktom praštevil, npr. 252 lahko zapišemo s produktom 22·32·71. Funkcija naj vrne seznam seznamov, ki predstavljajo osnovo in potenco.  
  
1. primer uporabe:
```
>>>  razcep_na_prafaktorje(252)
[[2, 2], [3, 2], [7, 1]]
```
2. primer uporabe:
```
>>>  razcep_na_prafaktorje(1944)
[[2, 3], [3, 5]]
```
Namig: Funkcija naj za vsa praštevila med `2` in `n` (vključno z `2` in `n`) ugotovi, kolikokrat delijo podano število in če ga delijo vsaj enkrat, to doda v seznam. Pomagajte si s funkcijama `prastevila(n)` in `deljivost(n, x)`.

# Fibonaccijevo zaporedje

Funkcije shranite v datoteko `fibonacci.py`

## 10. naloga: Fibonaccijeva števila

Napišite funkcijo `fibonaccijeva_stevila(n)`, ki prejme število `n`, vrne pa seznam [Fibonaccijevih števil](https://sl.wikipedia.org/wiki/Fibonaccijevo_%C5%A1tevilo) manjših od `n`.  
  
Primer uporabe:
```
>>>  fibonaccijeva_stevila(90)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
## 11. naloga: Liha Fibonaccijeva števila

Napišite funkcijo `liha_fibonaccijeva_stevila(n)`, ki prejme število `n`, vrne pa vsoto vseh lihih Fibonaccijevih števil manjših od `n`.  
  
Primer uporabe:
```
>>>  liha_fibonaccijeva_stevila(90)
188
```