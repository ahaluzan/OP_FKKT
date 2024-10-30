# Zanka *for*

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