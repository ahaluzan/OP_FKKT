# 1. vaje - Python in IDLE

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

# 2. vaje: Pogojni stavek *if*

Datoteka s testi je v isti mapi kot pričujoča navodila. Mapo s testi razpakirajte v enega od imenikov, kjer imate pravice za pisanje. Vsaka naloga ima svoj podimenik, v katerem so testi. Svoj program ustrezno poimenujte in shranite v imenik poleg testne skripte `test.py`. Teste poženete tako, da požnete program test.py (lahko preko IDLE ali konzole).

## 1. naloga: Črka v nizu

Napišite program `crka_v_nizu.py`, ki ugotovi, ali nek niz vsebuje podano črko (ali nek drug znak). Vaš program naj uporabnika najprej vpraša po nizu, nato še po črki. Program naj izpiše, ali je ta črka vsebovana v nizu. Da bo naloga lažja, naj program velike in male črke smatra kot različne znake.

Primer delovanja programa: 

```
Vpišite niz: fakulteta  
Vpišite črko: a
Niz vsebuje črko a.
```

Še en primer:

```
Vpišite niz: univerza  
Vpišite črko: ž
Niz ne vsebuje črke ž.
```

Pri tej nalogi testi ne bodo občutljivi na presledke.  
  

## 2. naloga: Največje in najmanjše število

Napišite program `min_maks.py`, ki izpiše največjo in najmanjšo izmed treh (celih) števil, ki jih vnese uporabnik. Ne uporabite funkcij `min()` in `max()`.  
Primer delovanja programa:

```
Vpišite 1. število: 5
Vpišite 2. število: 8
Vpišite 3. število: 7
Minimum: 5, Maksimum: 8
```

## 3. naloga: Pretvarjanje temperatur

Napišite program `temperature.py`, ki uporabnika vpraša po stopinjah Celzija in v katero enoto naj jih spremeni (Fahrenheit ali Kelvin). Program izpiše pretvorjeno vrednost. Če uporabnik vnese napačno enoto, mu izpiše opozorilo.  
Iz Celzijev v Kelvine pretvarjamo tako, da stopinjam prištejemo 273,15. Iz Celzijev v Fahrenheite pa pretvarjamo tako, da stopinje pomnožimo z 9/5 in prištejemo 32.  
Primer delovanja programa:

```
Vpiši temperaturo [°C]: 32
Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)?K
32.0 °C je enako 305.15 K

Vpiši temperaturo [°C]: 23
Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)? F
23.0 °C je enako 73.4 °F

Vpiši temperaturo [°C]: 13
Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)? C
Vnesli ste napačno enoto!
```

## 4. naloga: Indeks telesne mase

Napišite program `ITM.py`, ki uporabnika vpraša po telesni višini in masi ter izračuna [indeks telesne mase](https://sl.wikipedia.org/wiki/Indeks_telesne_mase). Če je indeks manjši od 18.5, uporabniku sporočite, da je presuh in mu priporočite, da naj poje kakšen kos torte. Če je indeks telesne teže večji od 25, spodbudite uporabnika, da se začne več gibati in jesti bolj zdravo. Drugače pa uporabniku sporočite, da naj kar nadaljuje s svojim življenjskim stilom.  
Primer delovanja programa:

```
Telesna višina [cm]: 189
Teža [kg]: 70
Vaš indeks telesne mase je: 19.6
Super, nadaljujte s svojim življenjskim stilom!

Telesna višina [cm]: 170
Teža [kg]: 53
Vaš indeks telesne mase je: 18.34
Pojejte kakšen kos torte več! ;)

Telesna višina [cm]: 165
Teža [kg]: 70
Vaš indeks telesne mase je: 25.71
Treba se bo več gibati in jesti bolj zdravo!
```

## 5. naloga: Kvadratna enačba

Napišite program `kvadratna_enacba.py`, ki [izračuna vse realne rešitve kvadratne enačbe](https://sl.wikipedia.org/wiki/Kvadratna_ena%C4%8Dba) (`ax^2 + bx + c = 0`) na štiri decimalna mesta za decimalno vejico. Vrednosti parametrov a, b in c naj vnese uporabnik. Vaš program naj se obnaša kot je prikazano v spodnjih primerih:

```
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
# 3. vaje: Zanka *`while`*  

## 1. naloga: Poštevanka  

Napišite program, ki prebere število z vhoda (kakor je izpisano v spodnjem primeru) ter izpiše (z zanko `while`) njegovo "poštevanko" (večkratnike podanega števila do 10). Program poimenujte `postevanka.py`.  
Primer delovanja:

```
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

## Naloge iz trgovine

 ##   2. naloga: Blagajna "vse po pet" 

V trgovini "vse po pet" morajo stranke vedno kupiti natanko pet artiklov. Za blagajne zato potrebujejo programsko opremo, ki uporabnika (blagajnika) vpraša po petih cenah; ko jih le-ta vnese, program izpiše vsoto. Program poimenujte `vse_po_pet.py`.  
Primer delovanja:

```
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Cena artikla: 6
Cena artikla: 3
Vsota: 16
```

 ## 3. naloga: Blagajna "konkurenca" 

Konkurenčna trgovina za vogalom se je odločila za posebno ponudbo: kupec lahko kupi toliko izdelkov, kolikor želi. Popravite gornji program tako, da blagajnika najprej vpraša, koliko izdelkov je v košarici, nato vpraša po cenah teh izdelkov in na koncu spet izpiše vsoto. Program poimenujte `konkurenca.py`.  
Primer delovanja:

```
Število izdelkov: 3
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Vsota: 7
```

 ## 4. naloga: Blagajna "top shop" 

Tretja trgovina se je odločila, da bo konkurirala drugi tako, da bo imela na blagajnah krajše vrste kot druga, pri kateri se plačevanje odvija počasi zato, ker morajo blagajniki prešteti izdelke preden lahko začnejo vnašati njihove cene. Popravite program tako, da ne vpraša po številu izdelkov, temveč sprašuje po cenah toliko časa, dokler mu blagajnik ne vnese ničle. Program poimenujte `top_shop.py`.  
Primer delovanja:

```
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Cena artikla: 0
Vsota: 7
```

 ##  5. naloga: Državna agencija za varstvo potrošnikov 

Zaradi poplave sumljivih trgovin za vogali se je Državna agencija za varstvo potrošnikov odločila nadzorovati povprečne cene izdelkov v košaricah strank. Popravite zadnji ali predzadnji program tako, da bo izpisal tudi povprečno ceno (ceno pri izpisu zaokrožite na 5 decimalk). Program poimenujte `varstvo_potrosnikov.py`.  
Primer delovanja:

```
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Cena artikla: 0
Vsota: 7
Povprečna cena: 2.33333
```

 ## 6. naloga: Klub anonimnih potrošnikov 

Razpas trgovin je pripeljal do zasvojenosti z nakupovanjem. Ena od metod zdravljenja temelji na inteligentnih košaricah, ki sprejmejo največ deset artiklov, potem pa se zaklenejo in jih lahko kupec le še odnese na blagajno. Prav tako se zaklenejo, če cena artiklov doseže (ali preseže) 100 evrov.

Napišite program `anonimni_potrosniki.py`, ki mu uporabnik vnaša cene in ki se neha izvajati, ko uporabnik vnese 0 (ne bo več kupoval), ko je vnešenih deset števil ali ko vsota cen doseže ali preseže 100 evrov.  
Primer delovanja, ko uporabnik vnese 0 (Pazite, uporabnik je kupil dve stvari, čeprav je vnesel tri cene!):

```
Cena: 10
Cena: 5
Cena: 0
Porabili boste 15 evrov za 2 stvari.
```

Primer delovanja, ko uporabnik preseže 100 evrov:

```
Cena: 10
Cena: 5
Cena: 90
Porabili boste 105 evrov za 3 stvari.
```

Primer delovanja, ko uporabnik kupi 10 artiklov:

```
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
Porabili boste 10 evrov za 10 stvari.
```

Da ne bo naloga predolga, vam pri izpisu ni treba paziti na sklanjanje besed "evrov" in "stvari" (napišite kar v množini).  
  

 ## 7. naloga: Tekoči račun 

Državna agencija za varstvo potrošnikov je razpisala projekt za izdelavo programa, s katerim bodo lahko potrošniki nadzorovali svoje tekoče račune. V program uporabniki vtipkavajo prejemke in izdatke (kot pozitivne in negativne zneske) na svojem tekočem računu. Program jim sproti izpisuje stanje in se ustavi, ko je uporabnik v minusu za 100 evrov ali več. Program poimenujte `tekoci_racun.py`.

Primer delovanja:

 ```
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

# 4. vaje: Zanka *for*

##  1. naloga: Iskanje minimuma 

Napišite program `iskanje_minimuma.py`, ki poišče in izpiše najmanjši element v seznamu celih števil brez uporabe funkcije `min()` ali sortiranja!  
Seznam števil naj vpiše uporabnik. Za interpretacijo vhodnega niza kot seznam lahko uporabite funkcijo `eval()`, ki je običajno za branje seznamov ne uporabljamo, vendar jo bomo v tem primeru uporabili, da bo koda za pretvarjanje vnesenih podatkov krajša.  
  
Primer delovanja:
```
Vpišite seznam števil: [23, 42, 87, 34, 1, -3, 2]
-3
````
## 2. naloga: Niz v seznamu 

Napišite program `niz_v_seznamu.py`, ki ugotovi, ali je nek niz vsebovan v predhodno definiranem seznamu nizov. Seznam definirajte na vrhu programa kot seznam sledečih nizov:  `seznam = ["beseda", "spremenljivka", "niz", "zanka", "stavek", "slovar"]`. Vaš program naj uporabnika vpraša po nizu, ki ga išče. Nato naj program izpiše, ali je ta niz vsebovan v seznamu. Nalogo poskusite rešiti tudi brez uporabe zanke.

Primer delovanja programa:

```
Vpišite iskani niz: zanka
Seznam vsebuje niz "zanka".
```

Še en primer:

```
Vpišite iskani niz: vrednost
Seznam ne vsebuje niza "vrednost".
```

Seveda mora program delati za poljubne sezname nizov in ne samo za zgornji seznam.  
  
Pri tej nalogi testi ne bodo občutljivi na presledke.

##  3. naloga: Števila v seznamu 

Napišite program `stevilo_v_seznamu.py`, ki ugotovi, ali je število, ki ga vpiše uporabnik, v seznamu celih števil, ki je definirano v vašem programu. Seznam definirajte na vrhu programa kot seznam sledečih števil: `seznam = [3, 35, 7, 68, 9, 10, 12, 481, 17, 12, 31, 21, 98, 33]`. Nalogo poskusite rešiti tudi brez uporabe zanke.

Primer delovanja programa:

```
Vpišite število: 9
Seznam vsebuje število 9

Vpišite število: 4
Seznam ne vsebuje števila 4
````

Seveda mora program delati za poljubne sezname in ne samo za zgornji seznam.

##  4. naloga: Vsota in povprečje 

Napišite program `vsota_in_povprecje.py`, ki za podani seznam izračuna vsoto (brez uporabe funkcije `sum`) in povprečje elementov.  
Seznam števil naj vpiše uporabnik. Za pretvorbo vhodnega niza v seznam uporabite funkcijo `eval()`. Rezultat zaokrožite na 5 decimalk.  
  
Primer delovanja:

```
Vpišite seznam števil: [23, 42, 87, 34, 1, -3, 2]
186
26.57143
```

##  5. naloga: Iskanje večkratnikov 

Napišite program `iskanje_veckratnikov.py`, ki preveri, če seznam vsebuje vsaj en večkratnik števila, ki ga vnese uporabnik. Poskusite uporabiti tudi `break`.  
Seznam števil naj vpiše uporabnik. Za pretvorbo vhodnega niza v seznam uporabite funkcijo `eval()`.  
  
1. primer delovanja:

```
Vpišite seznam števil: [23, 42, 87, 34, 1, -3, 2]
Vnesite število: 3
Vsebuje.
```

2. primer delovanja:

```
Vpišite seznam števil: [23, 42, 87, 34, 1, -3, 2]
Vnesite število: 8
Ne vsebuje.
```

##  6. naloga: Samo večkratniki 

Napišite program `samo_veckratniki.py`, ki preveri, če seznam vsebuje le večkratnike števila, ki ga vnese uporabnik. Poskusite uporabiti tudi `break`.  
Seznam števil naj vpiše uporabnik. Za pretvorbo vhodnega niza v seznam uporabite funkcijo `eval()`.  
  
1. primer delovanja:

```
Vpišite seznam števil: [27, 21, 3, 33, 60, -3]
Vnesite število: 3
Vsebuje.
```

2. primer delovanja:

```
Vpišite seznam števil: [27, 21, 3, 33, 60, -3]
Vnesite število: 9
Ne vsebuje.
```

##  7. naloga: Izris trikotnika 

Po programerski tradiciji eden prvih programov, ki jih napišemo v določenem programskem jeziku, nariše trikotnik iz zvezdic. Napišite program `izris_trikotnika.py`, ki vpraša uporabnika po višini trikotnika, nato pa izpiše takšen trikotnik iz zvezdic:

```
Vpiši višino: 4
 *
 * *
 * * *
 * * * *
```

##  8. naloga: Izris smrekice 

Napišite program `izris_smrekice.py`, ki bo namesto trikotnikov izrisoval "smrekice".  
  
Primer delovanja:

```
Vpiši višino: 4
       *
     * * *
   * * * * *
 * * * * * * *
```

Pozor: testi bodo občutljivi na presledke; ne uporabljajte presledkov tam, kjer niso potrebni.

# 5. vaje:

Sledijo trije sklopi nalog. Funkcije v posameznem sklopu shranite v Pythonovo datoteko in jo poimenujte kot piše v navodilih. Testi so na voljo v mapi. Datoteke shranite v ustrezen imenik `vaje05/ime_sklopa`. Teste poženete, kot ponavadi, tako da poženete `test.py` za vsak sklop nalog posebej. Vhodne podatke (v testih enot) najdete v imeniku `public/unit_test`.

## Preproste funkcije

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
# 6. vaje: (Ne)spremenljivi podatkovni tipi in terke 

Sledita dva sklopa nalog, funkcije v posameznem sklopu shranite v Pythonovo datoteko in jo poimenujte kot piše v navodilu. Testi so na voljo v mapi. Datoteki s končnico `.py` shranite v imenik `Vaje06/ime_sklopa`. Teste poženete tako, da poženete `test.py` za vsak sklop posebej. Teste enot z vhodnimi podatki najdete v imeniku `public/unit_test`.

# Spremenljivost

Funkcije shranite v datoteko `spremenljivost.py`

## 1. naloga: Korenjenje v seznamu (1)

Napišite funkcijo `koreni_seznam(seznam)`, ki prejme seznam in **spremeni** vse vrednosti v seznamu v njihove korene. Če je vrednost pod korenom negativna, jo prepiše v seznamu z `None`.  
1. primer uporabe:
```
>>> s = [0, 1, 4, 9, 16, 25]
>>> koreni_seznam(s)
>>> s
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
```
2. primer uporabe:
```
>>> s = [400, -100, 256, -1089]
>>> koreni_seznam(s)
>>> s
[20.0, None, 16.0, None]
```
## 2. naloga: Korenjenje v seznamu (2)

Napišite funkcijo `koreni_seznam2(seznam)`, ki prejme seznam in **vrne** seznam korenov vrednosti podanega seznama. Če je vrednost po korenom negativna, naj doda v seznam vrednost `None`.  
1. primer uporabe:
```
>>> s = [0, 1, 4, 9, 16, 25]
>>> s2 = koreni_seznam2(s)
>>> s2
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
>>> s
[0, 1, 4, 9, 16, 25]
```
2. primer uporabe:
```
>>> s = [400, -100, 256, -1089]
>>> s2 = koreni_seznam2(s)
>>> s2
[20.0, None, 16.0, None]
```
## 3. naloga: Unikaten seznam

Napišite funkcijo `unikaten_seznam(seznam)`, ki prejme seznam elementov, **vrne** pa seznam, ki vsebuje elemente prvega seznama samo po enkrat (vrstni red elementov pa naj bo isti, kot je vrstni red prve pojavitve v podanem seznamu).  
1. primer uporabe:
```
>>> unikaten_seznam([1, 2, 3, 3, 3, 3, 4, 5])
[1, 2, 3, 4, 5]
```
2. primer uporabe:
```
>>> unikaten_seznam([1, 2, 3, 4, 5, 1, 3, 5])
[1, 2, 3, 4, 5]
```
3. primer uporabe:
```
>>> unikaten_seznam([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]
```
# Terke

Funkcije shranite v datoteko `IMDb.py`

## 4. naloga: IMDb

Podan je primer seznama serij, ki poleg imena serije vsebuje tudi njeno oceno na IMDb-ju ter leto začetka predvajanja.
```
serije = [
    ('Friends', 9.0, 1994),
    ('The Big Bang Theory', 8.4, 2007),
    ('Game of Thrones', 9.5, 2011),
    ('Mr. Robot', 8.7, 2015),
    ('Humans', 8.1, 2015),
]
```
Napišite funkcijo `ocene(serije)`, ki sprejme seznam `serije` in **vrne** seznam naslovov serij, ki imajo oceno večjo ali enako 9!  
Primer uporabe:
```
>>> ocene(serije)
['Friends', 'Game of Thrones']
```
Naslove nanizajte v istem vrstnem redu, kot so podatki v podanem seznamu.  
  

## 5. naloga: Najstarejša serija

Napišite funkcijo `najstarejsa(serije)`, ki **vrne** ime najstarejše serije! Tokrat lahko predpostavite, da so vsi testni podatki taki, je najstarejša serija samo ena.  
Primer uporabe:
```
>>> najstarejsa(serije)
'Friends'
```
## 6. naloga: Povprečna ocena

Napišite funkcijo `povprecna_ocena(serije)`, ki **vrne** povprečno oceno vseh serij v seznamu!  
Primer uporabe:
```
>>> povprecna_ocena(serije)
8.74
```
## 7. naloga: Dolga imena serij

Napišite funkcijo `dolga_imena(serije)`, ki **vrne** seznam imen serij, ki so daljša od dveh besed!  
Primer uporabe:
```
>>> dolga_imena(serije)
['The Big Bang Theory', 'Game of Thrones']
```
Namig: pomagajte si z metodo `split()`, ki glede na presledke razbije niz na seznam nizov in tega vrne. Primer klica:
```
>>> niz='The Big Bang Theory'
>>> niz.split()
['The', 'Big', 'Bang', 'Theory']
```
## 8. naloga: Krajšanje

Napišite funkcijo `krajsanje(serije)`, ki **vrne** seznam terk, kjer vsaka terka predstavlja le ime serije in njeno oceno!  
Primer uporabe:
```
>>> krajsanje(serije)
[('Friends', 9.0), ('The Big Bang Theory', 8.4), ('Game of Thrones', 9.5), ('Mr. Robot', 8.7), ('Humans', 8.1)]
```
## 9. naloga: Najnovejše serije

Napišite funkcijo `najnovejse(serije)`, ki **vrne** seznam imen najnovejših serij iz podanega seznama serij (imena v vrnjenem seznamu naj bodo v istem vrstnem redu, kot so v podanem seznamu serij)!  
Primer uporabe:
```
>>> najnovejse(serije)
['Mr. Robot', 'Humans']
```

# 7. vaje: Slovarji

Tokrat sledi en sklop nalog, funkcije shranite v Pythonovo datoteko in jo poimenujte kot piše v navodilu. Testi so na voljo v mapi. Datoteko s končnico `.py` shranite v imenik `Vaje08/ime_sklopa`. Teste poženete, kot ponavadi, tako, da poženete `test.py`. Vhodne podatke najdete v imenik `public/unit_test`.

# Trgovina

Funkcije shranite v datoteko modul `trgovina`.

## 1. naloga: V slovar

Podan je seznam izdelkov v trgovini, ki poleg imena izdelka vsebuje tudi njegovo ceno in zalogo.
```
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
Napišite funkcijo `v_slovar(izdelki)`, ki sprejme seznam `izdelki` in **vrne** **slovar** izdelkov z njihovimi cenami in zalogo.  
Primer uporabe:
```
>>> v_slovar(izdelki)
{'mleko': [0.86, 128], 'hrenovka': [1.99, 28], 'jogurt': [0.49, 56], 'sok': [1.79, 104], 'moka': [1.39, 99], 'paradižnik': [0.23, 35], 'gorgonzola': [2.69, 32], 'makaroni': [1.89, 67], 'kruh': [2.19, 43], 'piškoti': [2.99, 73], 'jajce': [0.1, 103]}
```
## 2. naloga: Število izdelkov

Napišite funkcijo `stevilo_izdelkov(zaloga)`, ki **vrne** število vseh izdelkov v trgovini.  
Primer uporabe:
```
>>> zaloga = v_slovar(izdelki)
>>> stevilo_izdelkov(zaloga)
768
```
## 3. naloga: Nakupovalna košara

Napišite funkcijo `nakupovalna_kosara(seznam)`, ki prejme seznam vsebine nakupovalne košare in **vrne** slovar nakupov.  
Primer uporabe:
```
>>> seznam = ['jogurt', 'mleko', 'jogurt', 'jogurt', 'piškoti']
>>> nakupovalna_kosara(seznam)
{'jogurt': 3, 'mleko': 1, 'piškoti': 1}
```
## 4. naloga: Cena

Napišite funkcijo `cena(zaloga, slovar_nakupov)`, ki sprejme slovar nakupov in **vrne** znesek, ki ga mora plačati kupec.  
Primer uporabe:
```
>>> zaloga = v_slovar(izdelki)
>>> seznam = ['jogurt', 'mleko', 'jogurt', 'jogurt', 'piškoti']
>>> slovar_nakupov = nakupovalna_kosara(seznam)
>>> cena(zaloga, slovar_nakupov)
5.32
```
## 5. naloga: Popravek zaloge

Napišite funkcijo `popravek_zaloge(zaloga, izdelek, popravek)`, ki **spremeni** slovar `zaloga` tako, da zalogo `izdelek`\-a spremeni glede na popravek in **vrne** novo vrednost zaloge. Popravek je lahko negativen ali pozitiven. Če bi popravek spremenil zalogo na negativno, naj funkcija **vrne** `None` in naj ne spremeni zaloge.  
1. primer uporabe:
```
>>> zaloga = v_slovar(izdelki)
>>> popravek_zaloge(zaloga, 'sok', 100)
204
>>> zaloga
{'mleko': [0.86, 128], 'hrenovka': [1.99, 28], 'moka': [1.39, 99], 'sok': [1.79, 204], 'makaroni': [1.89, 67], 'kruh': [2.19, 43], 'jogurt': [0.49, 56], 'paradižnik': [0.23, 35], 'piškoti': [2.99, 73], 'gorgonzola': [2.69, 32], 'jajce': [0.1, 103]}
```
2. primer uporabe:
```
>>> zaloga = v_slovar(izdelki)
>>> popravek_zaloge(zaloga, 'jogurt', -60)
None (oz. ne izpiše ničesar)
```
## 6. naloga: Blagajna

Napišite funkcijo `blagajna(zaloga, slovar_nakupov)`, ki sprejme seznam nakupov, **spremeni** slovar `zaloga` in **vrne** znesek, ki ga mora plačati kupec. Pomagajte si s funkcijami, ki ste jih napisali do sedaj. Predvidite lahko, da nihče ne kupi več, kolikor imajo zaloge v trgovini.  
Primer uporabe:
```
>>> zaloga = v_slovar(izdelki)
>>> seznam = ['jogurt', 'mleko', 'jogurt', 'jogurt', 'piškoti']
>>> slovar_nakupov = nakupovalna_kosara(seznam)
>>> blagajna(zaloga, slovar_nakupov)
5.32
>>> zaloga
{'paradižnik': [0.23, 35], 'kruh': [2.19, 43], 'mleko': [0.86, 127], 'jajce': [0.1, 103], 'piškoti': [2.99, 72], 'moka': [1.39, 99], 'jogurt': [0.49, 53], 'hrenovka': [1.99, 28], 'sok': [1.79, 104], 'makaroni': [1.89, 67], 'gorgonzola': [2.69, 32]}
```
## 7. naloga: Kuhanje

David ni preveč spreten v kuhanju in zna pripraviti le nekaj jedi. Za njih ima točno recepturo, za katero natanko ve, koliko surovin potrebuje za pripravo:
```
jedi = {
    "palačinke": {"jajce": 3, "mleko": 1, "moka": 1},
    "šmorn": {"jajce": 3, "mleko": 1, "moka": 1},
    "hrenovke": {"hrenovka": 2, "kruh": 1},
    "makaroni": {"makaroni": 1, "paradižnik": 3, "gorgonzola": 1},
    "piškoti": {"piškoti": 1}
}
```
Napišite funkcijo `kuhanje(zaloga, jedi, jed)`, ki **vrne** ceno izdelkov potrebnih za pripravo jedi.  
Primer uporabe:
```
>>> zaloga = v_slovar(izdelki)
>>> kuhanje(zaloga, jedi, 'palačinke')
2.55
```
## 8. naloga: Obrok

Napišite funkcijo `posamezna_jed(jedi, jed, obrokov)`, ki kot argument dobi jed, ki jo želimo pripraviti in koliko obrokov. Kot rezultat **vrne** slovar s potrebnimi količinami.  
Primer uporabe:
```
>>> posamezna_jed(jedi, "šmorn", 4)
{'moka': 4, 'mleko': 4, 'jajce': 12}
```
## 9. naloga: Nakup

Napišite funkcijo `nakup(jedi, obroki)`, ki kot vhodni podatek prejme seznam jedi in količino obrokov, ter **vrne** vse, kar je potrebno nakupiti.  
Primer uporabe:
```
>>> obroki = [("makaroni", 20), ("palačinke", 15), ("šmorn", 10), ("hrenovke", 5)]
>>> nakup(jedi, obroki)
{'paradižnik': 60, 'gorgonzola': 20, 'moka': 25, 'kruh': 5, 'hrenovka': 10, 'jajce': 75, 'makaroni': 20, 'mleko': 25}
```
## 10. naloga: Primanjkljaj

Napišite funkcijo `primanjkljaj(zaloga, jedi, obroki)`, ki kot vhodni podatek prejme zalogo trgovine, seznam jedi in količino obrokov, ter **vrne** slovar vsega, kar morajo v trgovini še dokupiti, da bodo lahko prodali Davidu.  
Primer uporabe:
```
>>> zaloga = v_slovar(izdelki)
>>> obroki = [("makaroni", 20), ("palačinke", 15), ("šmorn", 10), ("hrenovke", 25)]
>>> primanjkljaj(zaloga, jedi, obroki)
{'hrenovka': 22, 'paradižnik': 25}
```

# 8. vaje: Množice in metode

Funkcije shranite v Pythonovo datoteko in jo poimenujte kot piše v navodilu. Testi so na voljo v mapi. Datoteko s končnico `.py` shranite v imenik `Vaje07/ime_sklopa`. Teste poženete, kot ponavadi, tako, da poženete `test.py`. Vhodne podatke najdete v imenik `public/unit_test`.  
  

Funkcije shranite v datoteko `metode.py`

## 1. naloga: Besede z a-ji

Napišite funkcijo `aa_besede(s)`, ki **vrne** množico besed v nizu `s`, ki vsebujejo vsaj dve črki `a`. Funkcija naj **ne** bo občutljiva na velikost črk.  
Namig: pred iskanjem odstranite ločila; privzamete lahko, da bo edino ločilo v testnih nizih pika (`.`).  
  
Primer uporabe:
```
>>> aa_besede('Anja je v trgovini kupila ananas in jabolka.')
{'ananas', 'Anja', 'jabolka'}
```
## 2. naloga: Najdaljše besede

Napišite funkcijo `najdaljse_besede(s)`, ki **vrne** množico najdaljših besed v nizu `s`.  
Predpostavite lahko, da bosta edini dve ločili v testnih nizih pika (`.`) in vejica (`,`).  
  
Primer uporabe:
```
>>> najdaljse_besede('Univerza v Ljubljani')
{'Ljubljani'}
```
## 3. naloga: Inicialke

Napišite funkcijo `velike_zacetnice(s)`, ki v nizu `s` vsem besedam daljšim od dveh znakov spremeni prvo črko v veliko začetnico in **vrne** spremenjen niz.  
Primer uporabe:
```
>>> velike_zacetnice('V trgovini je kupila ananas in jabolka.')
'V Trgovini je Kupila Ananas in Jabolka.'
```
## 4. naloga: Unikaten seznam

Napišite funkcijo `razlicne_skladbe(seznam)`, ki sprejme seznam vseh poslušanih skladb in **vrne** število različnih skladb.  
Primer uporabe:
```
>>> razlicne_skladbe(['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me', 'Imagine', 'Stairway To Heaven', 'One', 'Imagine'])
6
```
## 5. naloga: Prijatelji

Napišite funkcijo `skupne(seznam1, seznam2)`, ki sprejme seznama predvajanj dveh prijateljev in **vrne** množico skladb, ki so na obeh seznamih.  
Primer uporabe:
```
>>> skupne(['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me'], ['Imagine', 'Stairway To Heaven', 'One', 'Imagine'])
{'Imagine', 'One'}
```
## 6. naloga: Repertuar

Napišite funkcijo `repertuar(seznam1, seznam2)`, ki sprejme seznama predvajanj dveh prijateljev in **vrne** množico skladb, ki so na enem ali drugem ali obeh seznamih.  
Primer uporabe:
```
>>> repertuar(['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me'], ['Imagine', 'Stairway To Heaven', 'One', 'Imagine'])
{'Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me', 'Stairway To Heaven'}
```
## 7. naloga: Unikati

Napišite funkcijo `unikatna_predvajanja(seznam1, seznam2)`, ki sprejme seznama predvajanj dveh prijateljev in **vrne** množico skladb, ki so na enem ali na drugem seznamu, ne pa na obeh!  
Primer uporabe:
```
>>> unikatna_predvajanja(['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me'], ['Imagine', 'Stairway To Heaven', 'One', 'Imagine'])
{'Let It Be', 'The River', 'Stand By Me', 'Stairway To Heaven'}
```
## 8. naloga: Ponavljajoči se znaki

Napišite funkcijo `ponavljajoci_znaki(niz)`, ki sprejme niz in najde vse znake, ki se pojavijo več kot enkrat. Funkcije naj **vrne** množico terk, kjer je posamezna terka sestavljena iz dveh elementov: znaka in števila pojavitev. Funkcija naj bo občutljiva na velikost črk.  
Primer uporabe:
```
>>> ponavljajoci_znaki('otorinolaringologija')  
{('l', 2), ('i', 3), ('r', 2), ('a', 2), ('g', 2), ('o', 5), ('n', 2)}  
```
## 9. naloga: Onesnaženost z delci PM10

Agencija Republike Slovenije za okolje (ARSO) nas je prosila, da naredimo analizo onesnaženosti z delci PM10 v treh največjih slovenskih mestih (Ljubljana, Maribor in Celje) ter primerjamo podatke z merilno postajo Iskrba (merilno mesto Iskrba se nahaja ob Kočevski Reki, kjer v bližini ni virov, ki bi povzročali emisije delcev).

Napišite funcijo `najveckrat_onesnazena_mesta`, ki prejme mesečne podatke o onesnaženosti, ki so predstavljeni kot seznam dnevnih meritev merilnih postaj, vrne pa množico vseh krajev, v katerih je bila največkrat dosežena oz. presežena mejna vrednost 50 µg/m 3. Takih krajev je lahko več ali pa tudi nič – v takem primeru naj funkcija vrne prazno množico. Seznam krajev funkcija prejme kot drugi argument.

Seznam dnevnih meritev za en mesec vsebuje 28, 30 ali 31 terk, vsaka izmed njih pa predstavlja podatke za en dan v mesecu. Vsaka terka ima dva elementa; najprej dan v mesecu, nato pa terko,  v kateri so podatki o povprečni dnevni koncentraciji delcev PM 10 merilnih postaj Ljubljana, Maribor, Celje ter Iskrba (v tem vrstnem redu). Podatki so podani v enotah µg/m3. Lahko se tudi zgodi, da kakšne meritve manjkajo; v tem primeru imamo v terki shranjen `None`. Primer podatkov za januar 2017:
```
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
Primer klica funkcije:
```
>>> najveckrat_onesnazena_mesta(januar, kraji)  
{'Maribor', 'Celje'}
```

# 9. vaje: Datoteke

Sledita dva sklopa nalog, funkcije v posameznem sklopu shranite v Pythonovi datoteki in ju poimenujte kot piše v navodilih. Testi so na voljo v mapi. Vsako izmed dveh datotek s končnico `.py` shranite v mapo `Vaje09/ime_sklopa`. Teste poženete, kot ponavadi tako, da poženete `test.py` za vsak sklop posebej. Vhodne podatke najdete v mapi `public/unit_test`.

# Filmi

Funkcije shranite v datoteko `filmi.py`. Datoteka `filmi.txt` se nahaja v podimeniku `podatki` imenika s testi.

## 1. naloga: Preberi

Napišite funkcijo `preberi(datoteka)`, ki prebere datoteko in **vrne** **niz** zapisan v datoteki.  
Primer uporabe:
```
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
## 2. naloga: V seznam

Napišite funkcijo `v_seznam(datoteka)`, ki prebere datoteko in **vrne** vsebino v obliki **seznama seznamov**.  
Primer uporabe:
```
>>> v_seznam('podatki/filmi.txt')
[['The Godfather', 9.2, 'Kriminalka', 1972], ["Schindler's List", 8.9, 'Drama', 1993], ['Casablanca', 8.6, 'Drama', 1942], ['Forrest Gump', 8.8, 'Komedija', 1994], ['The Sound of Music', 8.0, 'Glasbena biografija', 1965], ['Gladiator', 8.5, 'Akcija', 2000], ['Titanic', 7.7, 'Romantična drama', 1997], ['Saving Private Ryan', 8.6, 'Akcija', 1998]]
```
## 3. naloga: V slovar

Napišite funkcijo `v_slovar(datoteka)`, ki prebere datoteko in **vrne** vsebino v obliki **slovarja**, kjer ključi predstavljajo žanr filma.  
Primer uporabe:
```
>>> v_slovar('podatki/filmi.txt')
{'Romantična drama': ['Titanic'], 'Kriminalka': ['The Godfather'], 'Akcija': ['Gladiator', 'Saving Private Ryan'], 'Drama': ["Schindler's List", 'Casablanca'], 'Komedija': ['Forrest Gump'], 'Glasbena biografija': ['The Sound of Music']}
```
## 4. naloga: Najljubši film

Napišite funkcijo `najljubsi(datoteka_pisanja)`, ki vpraša uporabnika po najljubšem filmu in v novo datoteko `datoteka_pisanja` **zapiše** naslov tega filma.  
Primer uporabe:
```
>>> najljubsi('podatki/najljubsi_film.txt')
Najljubši film: Forrest Gump
```
V datoteki `najljubsi_film.txt` je sedaj viden zapis:

```Forrest Gump```

## 5. naloga: Zapis

Napišite funkcijo `zapis(datoteka_branja, datoteka_pisanja)`, ki **prebere** vsebino datoteke `datoteka_branja` in v novo datoteko `datoteka_pisanja` **zapiše** naslove filmov urejene po abecedi.  
Primer uporabe:
```
>>> zapis('podatki/filmi.txt', 'podatki/imena_filmov.txt')
```
V datoteki `imena_filmov.txt` je sedaj viden zapis:

```
Casablanca
Forrest Gump
Gladiator
Saving Private Ryan
Schindler's List
The Godfather
The Sound of Music
Titanic
```

## 6. naloga: CSV

Prijatelj vam je poslal datoteko `ratings.csv` shranjeno v formatu CSV, ki hrani podatke o ocenah večjega števila filmov iz strani večih ocenjevalcev (približno 13 tisoč ocenjevalcev). Začetek datoteke izgleda kot sledi:
```
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
kjer si podatki v vsaki vrstici sledijo, kot piše v prvi vrstici: _ID ocenjevalca, ID filma, ocena, časovna oznaka_.

Prijatelj vas prosi, če mu lahko napišete program `ocena_filma(id_filma, csv_datoteka)`, ki bo za podani id filma vrnil povprečno oceno. Ker vam je prijatelj poslal zares veliko podatkov, bo tudi vaš program potreboval nekoliko več, da bo vrnil rezultat.  
Primer uporabe:
```
>>> ocena_filma(2, 'podatki/ratings.csv')
3.2296978281397544
```

# Oliver Twist

Tokrat bomo malce bolj literarni. Brali bomo knjigo Oliver Twist avtorja Charlesa Dickensena (`OliverTwist.txt`; vir: [Project Gutenberg](http://www.gutenberg.org/ebooks/730)). Funkcije shranite v datoteko `knjiga.py`.

## 7. naloga: Število besed

Napišite funkcijo `stevilo_besed(datoteka)`, ki prebere datoteko in **vrne** število besed, ki se pojavijo v knjigi. Besedilo lahko le ločite po presledkih in se ne obremenjujete z odstranjevanjem ločil.  
Primer uporabe:
```
>>> stevilo_besed('OliverTwist.txt')
158041
```
## 8. naloga: Različni znaki

Napišite funkcijo `razlicni_znaki(datoteka)`, ki prebere datoteko in **vrne** število različnih znakov, ki se pojavijo v knjigi.  
Primer uporabe:
```
>>> razlicni_znaki('OliverTwist.txt')
70
```
## 9. naloga: Najpogostejši znak

Napišite funkcijo `najpogostejsi_znak(datoteka)`, ki prebere datoteko in **vrne** **znak**, ki se v knjigi Oliver Twist pojavi največkrat.  
Primer uporabe:
```
>>> najpogostejsi_znak('OliverTwist.txt')
 <izpisan je presledek>
```
## 10. naloga: Hapax legomenon

Napišite funkcijo `hapax(datoteka)`, ki prebere datoteko in **vrne** število besed, ki se v knjigi Oliver Twist pojavijo natanko enkrat (t.i. [hapax legomenon](https://en.wikipedia.org/wiki/Hapax_legomenon)). Besedilo lahko le ločite po presledkih in se ne obremenjujete z odstranjevanjem ločil.  
Primer uporabe:
```
>>> hapax('OliverTwist.txt')
11851
```