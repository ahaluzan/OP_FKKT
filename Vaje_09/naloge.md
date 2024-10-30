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