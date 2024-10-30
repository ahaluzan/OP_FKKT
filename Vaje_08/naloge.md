Funkcije shranite v Pythonovo datoteko in jo poimenujte kot piše v navodilu. Testi so na voljo v mapi. Datoteko s končnico `.py` shranite v imenik `Vaje07/ime_sklopa`. Teste poženete, kot ponavadi, tako, da poženete `test.py`. Vhodne podatke najdete v imenik `public/unit_test`.  
  

# Množice in metode

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