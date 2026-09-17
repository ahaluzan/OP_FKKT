import unittest
import kolokvij


datoteka = 'public/data/movies_double.txt'
slovar = {'Italy': {('La vita è bella', 1997), ('Per qualche dollaro in più', 1965), ("C'era una volta il West", 1968), ('Il buono, il brutto, il cattivo', 1966), ('Nuovo Cinema Paradiso', 1988), ('La grande bellezza', 2013), ('Ladri di biciclette', 1948)}, 'Argentina': {('El secreto de sus ojos', 2009)}, 'Bosnia & Herzegovina': {('Ničija zemlja', 2001)}, 'USA': {('Casablanca', 1942), ("Schindler's List", 1993), ('Forrest Gump', 1994), ('Gladiator', 2000), ('The Godfather', 1972), ('Saving Private Ryan', 1998), ('Titanic', 1997), ('The Sound of Music', 1965)}, 'UK': {('Slumdog Millionaire', 2008), ('Hotel Rwanda', 2004)}, 'Mexico': {('Amores perros', 2000)}, 'Netherlands': {('Karakter', 1997)}, 'Canada': {('Les Invasions barbares', 2003)}, 'South Korea': {('Oldeuboi', 2003)}, 'Denmark': {('Hævnen', 2010)}, 'Austria': {('Amour', 2012), ('Die Fälscher', 2007)}, 'Poland': {('Ida', 2013)}, 'West Germany': {('Das Boot', 1981)}, 'France': {("Le fabuleux destin d'Amélie Poulain", 2001), ('Le scaphandre et le papillon', 2007)}, 'Hungary': {('Son of Saul', 2015)}, 'South Africa': {('Tsotsi', 2005)}, 'Germany': {('Der Untergang', 2004), ('Das Leben der Anderen', 2006), ('Nirgendwo in Afrika', 2001)}, 'Sweden': {('Det sjunde inseglet', 1957), ('Smultronstället', 1957)}, 'Spain': {('Mar adentro', 2004), ('Todo sobre mi madre', 1999), ('El laberinto del fauno', 2006)}, 'Japan': {('Sen to Chihiro no kamikakushi', 2001), ('Rashômon', 1950), ('Hotaru no haka', 1988), ('Okuribito', 2008), ('Yôjinbô', 1961), ('Mononoke-hime', 1997), ('Shichinin no samurai', 1954), ('Wòhǔ Cánglóng', 2000)}, 'Brazil': {('Cidade de Deus', 2002)}, 'Iran': {('Jodaeiye Nader az Simin', 2011)}}


test_case = unittest.TestCase()
test_case.assertEqual(kolokvij.preberi(datoteka), slovar)

