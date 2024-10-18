# Zanka *`while`*  

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
Sprememba: \-30
Stanje: 8
Sprememba: 10
Stanje: 18
Sprememba: 100
Stanje: 118
Sprememba: \-200
Stanje: -82
Sprememba: \-50
Stanje: \-132
Bankrot!
```