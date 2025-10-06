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
