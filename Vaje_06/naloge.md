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