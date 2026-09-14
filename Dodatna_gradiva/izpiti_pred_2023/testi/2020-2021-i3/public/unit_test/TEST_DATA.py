TEST_DATA = {
    'MP ŠENTILJ - POČIVALIŠČE ŠENTILJ': ('A1', 'MT Šentilj AC', 54, 18167, 143, 5316),
    'POČIVALIŠČE ŠENTILJ - ŠENTILJ': ('A1', 'Šentilj AC', 52, 17781, 142, 5265),
    'PRIKLJŠENTILJ - MP ŠENTILJ': ('A1', 'Priklj Šentilj-MP', 4, 376, 1, 74),
    'ŠENTILJ  -  PESNICA': ('A1', ' Pesnica AC', 70, 22594, 227, 6209),
    'PESNICA - DRAGUČOVA': ('A1', 'neznano', 90, 22550, 240, 6420),
    'DRAGUČOVA - MB (ZRKOVSKA)': ('A1', 'Malečnik AC', 45, 25538, 327, 11620),
    'MB (ZRKOVSKA)  - MB (PTUJSKA)': ('A1', 'neznano', 40, 25640, 310, 11810),
    'MB (PTUJSKA) - ROGOZA': ('A1', 'Ptujska AC', 38, 31656, 309, 12766),
    'ROGOZA - SLIVNICA': ('A1', 'neznano', 40, 29810, 310, 12340),
    'SLIVNICA': ('A1', 'neznano', 40, 34870, 315, 12145)}

DRUGA = [
    ({'MP ŠENTILJ - POČIVALIŠČE ŠENTILJ': ('A1', 'MT Šentilj AC', 54, 18167, 143, 5316),
      'POČIVALIŠČE ŠENTILJ - ŠENTILJ': ('A1', 'Šentilj AC', 52, 17781, 142, 5265),
      'PRIKLJŠENTILJ - MP ŠENTILJ': ('A1', 'Priklj Šentilj-MP', 4, 376, 1, 74),
      'ŠENTILJ  -  PESNICA': ('A1', ' Pesnica AC', 70, 22594, 227, 6209),
      'PESNICA - DRAGUČOVA': ('A1', 'neznano', 90, 22550, 240, 6420),
      'DRAGUČOVA - MB (ZRKOVSKA)': ('A1', 'Malečnik AC', 45, 25538, 327, 11620),
      'MB (ZRKOVSKA)  - MB (PTUJSKA)': ('A1', 'neznano', 40, 25640, 310, 11810),
      'MB (PTUJSKA) - ROGOZA': ('A1', 'Ptujska AC', 38, 31656, 309, 12766),
      'ROGOZA - SLIVNICA': ('A1', 'neznano', 40, 29810, 310, 12340),
      'SLIVNICA': ('A1', 'neznano', 40, 34870, 315, 12145)},
     [('MP ŠENTILJ - POČIVALIŠČE ŠENTILJ', 23680), ('POČIVALIŠČE ŠENTILJ - ŠENTILJ', 23240),
      ('PRIKLJŠENTILJ - MP ŠENTILJ', 455), ('ŠENTILJ  -  PESNICA', 29100), ('PESNICA - DRAGUČOVA', 29300),
      ('DRAGUČOVA - MB (ZRKOVSKA)', 37530), ('MB (ZRKOVSKA)  - MB (PTUJSKA)', 37800), ('MB (PTUJSKA) - ROGOZA', 44769),
      ('ROGOZA - SLIVNICA', 42500), ('SLIVNICA', 47370)]),
    ({}, [])
]

TRETJA = [
    ([('MP ŠENTILJ - POČIVALIŠČE ŠENTILJ', 23680),
      ('POČIVALIŠČE ŠENTILJ - ŠENTILJ', 23240),
      ('PRIKLJŠENTILJ - MP ŠENTILJ', 455),
      ('ŠENTILJ  -  PESNICA', 29100),
      ('PESNICA - DRAGUČOVA', 29300),
      ('DRAGUČOVA - MB (ZRKOVSKA)', 37530),
      ('MB (ZRKOVSKA)  - MB (PTUJSKA)', 37800),
      ('MB (PTUJSKA) - ROGOZA', 44769),
      ('ROGOZA - SLIVNICA', 42500),
      ('SLIVNICA', 47370)], 'SLIVNICA'),
    ([], ""),
    ([('ŠENTILJ  -  PESNICA', 47370)], 'ŠENTILJ  -  PESNICA'),
    ([('MP ŠENTILJ - POČIVALIŠČE ŠENTILJ', 23680),
      ('POČIVALIŠČE ŠENTILJ - ŠENTILJ', 23240),
      ('PRIKLJŠENTILJ - MP ŠENTILJ', 455),
      ('ŠENTILJ  -  PESNICA', 29100),
      ('PESNICA - DRAGUČOVA', 29300),
      ('DRAGUČOVA - MB (ZRKOVSKA)', 37530),
      ('MB (ZRKOVSKA)  - MB (PTUJSKA)', 37800),
      ('MB (PTUJSKA) - ROGOZA', 44769),
      ('ROGOZA - SLIVNICA', 42500)
      ], 'MB (PTUJSKA) - ROGOZA')
]

_cetrta = [
    ('MP ŠENTILJ - POČIVALIŠČE ŠENTILJ', 23680),
    ('POČIVALIŠČE ŠENTILJ - ŠENTILJ', 23240),
    ('PRIKLJŠENTILJ - MP ŠENTILJ', 455),
    ('ŠENTILJ  -  PESNICA', 29100),
    ('PESNICA - DRAGUČOVA', 29300),
    ('DRAGUČOVA - MB (ZRKOVSKA)', 37530),
    ('MB (ZRKOVSKA)  - MB (PTUJSKA)', 37800),
    ('MB (PTUJSKA) - ROGOZA', 44769),
    ('ROGOZA - SLIVNICA', 42500),
    ('SLIVNICA', 47370)]

CETRTA = [
    ([_cetrta, "MB"], 40033.0),
    ([_cetrta, "Vrhnika"], 0),
    ([_cetrta, "SLIVNICA"], 44935.0),
    ([_cetrta, "LJ"], 19118.75)
]

_ceste = {
    'MP ŠENTILJ - POČIVALIŠČE ŠENTILJ': ('A1', 'MT Šentilj AC', 520, 157240, 1150, 45900),
    'POČIVALIŠČE ŠENTILJ - ŠENTILJ': ('A1', 'Šentilj AC', 520, 155600, 1140, 45490),
    'PRIKLJŠENTILJ - MP ŠENTILJ': ('A1', 'Priklj Šentilj MP', 10, 3460, 0, 540),
    'ŠENTILJ  -  PESNICA': ('A1', 'Pesnica AC', 620, 197400, 2050, 50480),
    'LJ (BROD - ŠENTVID)': ('A2', 'neznano', 1800, 458200, 2700, 67300),
    'LJ (ŠENTVID - PODUTIK)': ('A2', 'Kamna Gorica AC', 1900, 426400, 2150, 72550),
    'LJ (PODUTIK - KOSEZE)': ('H3', 'neznano', 1750, 463750, 1250, 87250),
    'LJ (KOSEZE  -  BRDO)': ('A2', 'neznano', 2700, 662300, 3050, 119950),
    'LJ (BRDO  -  KOZARJE)': ('A2', 'Bokalce AC', 2640, 616120, 3040, 122580),
    'GRUŠKOVJE - R HRVAŠKA': ('A4', 'neznano', 420, 81340, 1450, 24880),
    'DRAGUČOVA - PERNICA': ('A5', 'Dragučova AC', 520, 178010, 1860, 75230),
    'PERNICA - LENART': ('A5', 'Močna AC', 510, 172890, 1840, 74320),
    'LJ (IND CONA ŠIŠKA - CELOVŠKA)': ('H3', 'neznano', 1800, 616350, 1750, 90100),
    'LJ (CELOVŠKA  -  VODNIKOVA)': ('H3', 'neznano', 1800, 528700, 1400, 88100),
    'LJ (VODNIKOVA  -  PODUTIK)': ('H3', 'Dravlje HC', 1740, 483800, 1280, 87880),
    'BREZNO - RUTA': ('1', 'Ožbalt', 430, 35450, 440, 7480),
    'RUTA - SELNICA': ('1', 'Zgornji Boč', 640, 39140, 370, 7690),
    'SOLKAN-NOVA GORICA (KROMBERK)': ('103', 'Solkan 3', 1440, 68760, 210, 9940),
    'KROMBERK  -  ROŽNA DOLINA': ('103', 'Panovec', 1980, 220360, 1350, 18010)}

PETA_A = [
    (_ceste, {'A1': 4, 'A2': 4, 'H3': 4, 'A4': 1, 'A5': 2, '1': 2, '103': 2}),
    ({}, {})
]

PETA_B = [
    ([_ceste, 5], {'1', '103', 'A1', 'A2', 'A4', 'A5', 'H3'}),
    ([_ceste, 3], {'1', '103', 'A4', 'A5'}),
    ([_ceste, 2], {'A4'}),
]
