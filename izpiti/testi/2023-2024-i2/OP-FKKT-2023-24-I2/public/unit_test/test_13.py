'''priporocila'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez =[('Pablo Escobar: The Drug Lord', 2012, 44, 10, 'crime', 'CO', 8.4, 'TV-14'),
 ('El Reemplazante', 2012, 45, 20, 'drama', 'CL', 8.5, 'TV-MA'),
 ('Leah Remini: Scientology and the Aftermath',2016,46,30,'documentary','US',9.0,'TV-14'),
 ('Anne with an E', 2017, 46, 30, 'drama', 'CA', 8.7, 'TV-G'),
 ('Wentworth', 2013, 46, 90, 'drama', 'AU', 8.6, 'TV-MA'),
 ('Queer Eye', 2018, 47, 60, 'reality', 'US', 8.5, 'TV-14'),
 ('Breaking Bad', 2008, 48, 50, 'drama', 'US', 9.5, 'TV-MA'),
 ('Lenox Hill', 2020, 48, 10, 'documentary', 'US', 8.6, 'TV-MA'),
 ('Better Call Saul', 2015, 49, 60, 'drama', 'US', 8.8, 'TV-MA'),
 ('Shtisel', 2013, 49, 30, 'drama', 'IL', 8.6, 'TV-14'),
 ('Our Planet', 2019, 50, 10, 'documentary', 'GB', 9.3, 'TV-G'),
 ('The Last Dance', 2020, 50, 10, 'documentary', 'US', 9.1, 'TV-MA'),
 ('Sacred Games', 2018, 50, 20, 'action', 'IN', 8.5, 'TV-MA'),
 ("Chef's Table", 2015, 50, 70, 'documentary', 'US', 8.5, 'TV-MA'),
 ('Middleditch & Schwartz', 2020, 51, 10, 'comedy', 'US', 8.6, 'TV-MA'),
 ('Narcos', 2015, 52, 30, 'drama', 'US', 8.8, 'TV-MA'),
 ('House of Cards', 2013, 52, 60, 'drama', 'US', 8.7, 'TV-MA'),
 ('Move to Heaven', 2021, 52, 10, 'drama', 'KR', 8.6, 'TV-MA'),
 ('James Acaster: Repertoire', 2018, 52, 10, 'comedy', 'GB', 8.4, 'TV-14'),
 ('Mindhunter', 2017, 53, 20, 'drama', 'US', 8.6, 'TV-MA'),
 ('Shameless', 2011, 54, 110, 'drama', 'US', 8.6, 'TV-MA'),
 ('The Last Kingdom', 2015, 55, 50, 'action', 'GB', 8.5, 'TV-MA'),
 ('Call the Midwife', 2012, 55, 110, 'family', 'GB', 8.5, 'TV-PG'),
 ('Dark', 2017, 56, 30, 'scifi', 'DE', 8.7, 'TV-MA'),
 ('The Crown', 2016, 56, 50, 'drama', 'GB,US', 8.7, 'TV-MA'),
 ("The Queen's Gambit", 2020, 56, 10, 'drama', 'US', 8.6, 'TV-MA'),
 ('The Great British Baking Show',2010,57,120,'reality','GB',8.6,'TV-PG'),
 ('Peaky Blinders', 2013, 58, 60, 'crime', 'GB', 8.8, 'TV-MA'),
 ('Top Gear', 2002, 58, 320, 'comedy', 'GB', 8.7, 'TV-PG'),
 ('The Haunting of Hill House', 2018, 58, 10, 'thriller', 'US', 8.6, 'TV-MA'),
 ('Borgen', 2010, 58, 40, 'drama', 'DK', 8.5, 'TV-MA'),
 ('Black Mirror', 2011, 59, 50, 'drama', 'GB', 8.8, 'TV-MA')]

act = naloge.priporocila('Peaky Blinders', sez)
exp = ['Pablo Escobar: The Drug Lord']

test_case.assertEqual(type(act), type(exp), 'Neustrezen podatkovni tip.')

