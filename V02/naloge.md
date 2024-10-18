Pri primerih delovanja programov so z **modro** označeni izpisi vašega programa, z **rdečo** pa vnos uporabnika. Pri reševanju pazite, da se vaši izpisi ujemajo z izpisi v navodilih (vključno s presledki). Testirate s testnimi skriptami, ki jih dobite [**⇉ tukaj ⇇**](https://ucilnica.fri.uni-lj.si/draftfile.php/201846/user/draft/352115717/vaje02.zip?time=1633365588558).

ZIP-datoteko s testi razpakirajte v enega od imenikov, kjer imate pravice za pisanje. Vsaka naloga ima svoj podimenik, v katerem so testi. Svoj program ustrezno poimenujte in shranite v imenik poleg testne skripte `test.py`. Teste poženete tako, da požnete program test.py (lahko preko IDLE ali konzole).

## 1. naloga: Črka v nizu

Napišite program `crka_v_nizu.py`, ki ugotovi, ali nek niz vsebuje podano črko (ali nek drug znak). Vaš program naj uporabnika najprej vpraša po nizu, nato še po črki. Program naj izpiše, ali je ta črka vsebovana v nizu. Da bo naloga lažja, naj program velike in male črke smatra kot različne znake.

Primer delovanja programa: 

```
Vpišite niz: fakulteta  
Vpišite črko: a
Niz vsebuje črko a.

Še en primer:

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
Vpiši temperaturo \[°C\]: 32
Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)?K
32.0 °C je enako 305.15 K

Vpiši temperaturo \[°C\]: 23
Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)? F
23.0 °C je enako 73.4 °F

Vpiši temperaturo \[°C\]: 13
Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)? C
Vnesli ste napačno enoto!
```

## 4. naloga: Indeks telesne mase

Napišite program `ITM.py`, ki uporabnika vpraša po telesni višini in masi ter izračuna [indeks telesne mase](https://sl.wikipedia.org/wiki/Indeks_telesne_mase). Če je indeks manjši od 18.5, uporabniku sporočite, da je presuh in mu priporočite, da naj poje kakšen kos torte. Če je indeks telesne teže večji od 25, spodbudite uporabnika, da se začne več gibati in jesti bolj zdravo. Drugače pa uporabniku sporočite, da naj kar nadaljuje s svojim življenjskim stilom.  
Primer delovanja programa:

```
Telesna višina \[cm\]: 189
Teža \[kg\]: 70
Vaš indeks telesne mase je: 19.6
Super, nadaljujte s svojim življenjskim stilom!

Telesna višina \[cm\]: 170
Teža \[kg\]: 53
Vaš indeks telesne mase je: 18.34
Pojejte kakšen kos torte več! ;)

Telesna višina \[cm\]: 165
Teža \[kg\]: 70
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