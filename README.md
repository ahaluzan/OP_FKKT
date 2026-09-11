# Osnove programiranja (OP) – gradiva za študente

Ta repozitorij vsebuje vsa gradiva za predmet **Osnove programiranja**, ki se izvaja na Fakulteti za kemijo in kemijsko tehnologijo Univerze v Ljubljani. 

Povezava do spletne učilnice predmeta: [https://ucilnica.fri.uni-lj.si/course/view.php?id=239](https://ucilnica.fri.uni-lj.si/course/view.php?id=239)

Spletna učilnica se uporablja predvsem za obvestila in oddajo nalog, medtem ko so vaje in dodatna gradiva ažurneje vzdrževana tukaj. V primeru razlik med gradivi na spletni učilnici in tu se držite gradiv iz tega repozitorija.

## Struktura repozitorija

```
.
├── vaje_komplet.md      # Zbirka nalog za vse vaje
├── naloge_testi/         # Avtomatski testi za posamezne sklope vaj
├── dodatna_gradiva/       # Gradiva za dodatne vaje in tematike
├── testi_kol_izp/          # Avtomatski testi starih kolokvijev in izpitov
└── gradiva/               # PDF-ji gradiv, predpisanih za študij
```

- **`vaje_komplet.md`** – vsebuje navodila za vse naloge na enem mestu;
- **`naloge_testi/`** – mapa vsebuje podmape s testi za vsak sklop vaj. S testi preverjate pravilnost svojih rešitev;
- **`testi_kol_izp/`** - mapa vsebuje podmape s testi starih izpitov in kolokvijev
- **`dodatna_gradiva/`** – vsebine, ki presegajo redni obseg vaj (npr. dodatne naloge in teme za tiste, ki želite znanje poglobiti);
- **`gradiva/`** – PDF-ji skript, uporabljenih pri predmetu.

## Kako uporabljati repozitorij

Repozitorij lahko prenesete na enega od naslednjih načinov:

- **kloniranje** (priporočeno, saj lahko z `git pull` enostavno pridobite posodobitve):
  ```
  git clone <povezava-do-repozitorija>
  ```
- **prenos ZIP datoteke**: na GitHubu kliknite `Code → Download ZIP`.

Če ste repozitorij klonirali, gradiva redno posodabljate z ukazom:
```
git pull
```

## Uporaba avtomatskih testov

V mapi `naloge_testi` je za vsak sklop vaj svoja podmapa s testi. Avtomatsko testiranje izvedete tako, da:

1. v mapo, ki ustreza sklopu vaj in nalogi, ki jo rešujete, shranite svojo datoteko z rešitvami. Vaša datoteka mora biti poimenovano tako, kot je navedeno v navodilih vaj, sicer je test ne bo prepoznal;
2. v mapi odprete in zaženite datoteko `test.py`.

Iz terminala to storite z ukazom (v mapi, kjer je `test.py`):
```
python test.py
```
(na nekaterih sistemih, kot je Linux, je ukaz `python3 test.py`)

Test označi, katere naloge so rešene pravilno in kje so morebitne napake.
