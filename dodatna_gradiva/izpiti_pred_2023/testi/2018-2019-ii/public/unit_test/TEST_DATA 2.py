DATA_FILES = ["data.csv", "data2.csv", "data3.csv"]

READS = [None, None, None]
READS[0] = {'Christina Coleman': [[3, 11, 23, 26, 31, 33, 38]],
            'Margaret Rentas': [[1, 2, 5, 7, 10, 15, 39],
                                [3, 5, 10, 11, 21, 22, 30],
                                [4, 5, 10, 11, 21, 22, 30]],
            'Romana Hammond': [[3, 9, 10, 12, 18, 19, 26]],
            'Teresa Hoffman': [[6, 10, 19, 25, 26, 29, 35]],
            'Cheryl Sheehan': [[3, 5, 15, 28, 29, 30, 31]],
            'Violet Bishop': [[3, 4, 18, 20, 24, 37, 38]],
            'Ronald Vue': [[1, 3, 16, 17, 23, 27, 28]],
            'Eric Atkins': [[1, 2, 5, 7, 10, 15, 39]],
            'Jerome Figures': [[4, 6, 20, 22, 29, 34, 37]],
            'Edgardo Burke': [[4, 5, 12, 16, 21, 22, 25]]}

READS[1] = {'Todd Warner': [[6, 8, 11, 20, 23, 27, 37], [3, 10, 16, 20, 26, 29, 39]],
            'Lon Heinrich': [[9, 20, 24, 27, 30, 32, 35], [5, 10, 21, 23, 24, 32, 34]],
            'Donita Tedford': [[7, 9, 17, 25, 28, 31, 33]],
            'Sheri Hanna': [[5, 12, 14, 31, 33, 34, 37]],
            'Truman Randolph': [[2, 16, 22, 23, 24, 30, 37]],
            'Anthony Thomas': [[1, 16, 19, 28, 29, 31, 32]]}

READS[2] = {'Glenda Perry': [[3, 4, 14, 26, 35, 37, 39],
                             [3, 10, 11, 25, 29, 30, 31],
                             [1, 4, 5, 6, 26, 29, 30],
                             [1, 3, 6, 7, 8, 27, 38],
                             [10, 12, 13, 18, 21, 24, 36],
                             [4, 6, 20, 24, 28, 34, 39]],
            'Julie Piekarski': [[4, 9, 11, 25, 31, 34, 35],
                                [4, 20, 27, 30, 31, 37, 39],
                                [3, 4, 6, 9, 11, 26, 30],
                                [2, 16, 21, 25, 26, 34, 38],
                                [1, 6, 12, 21, 30, 31, 36],
                                [4, 6, 20, 24, 28, 34, 39]],
            'Kate Sibley': [[8, 12, 14, 17, 18, 24, 31],
                            [15, 16, 17, 23, 25, 27, 29],
                            [1, 19, 22, 25, 33, 34, 39],
                            [7, 14, 19, 28, 31, 36, 38],
                            [3, 17, 24, 28, 36, 37, 38],
                            [4, 6, 20, 24, 28, 34, 39]],
            'Deborah Aguiar': [[9, 22, 25, 27, 28, 32, 34],
                               [6, 9, 30, 31, 37, 38, 39],
                               [1, 7, 19, 21, 27, 28, 29],
                               [13, 16, 17, 22, 27, 35, 38],
                               [1, 5, 17, 18, 23, 26, 31],
                               [4, 6, 20, 24, 28, 34, 39]],
            'Susan Doyle': [[3, 12, 13, 15, 24, 29, 39],
                            [6, 11, 15, 20, 22, 26, 39],
                            [8, 19, 25, 27, 29, 31, 37],
                            [1, 8, 11, 21, 23, 24, 34],
                            [1, 3, 15, 25, 32, 34, 38],
                            [4, 6, 20, 24, 28, 34, 39]]}

JACKPOTS = [
    [1, 2, 5, 7, 10, 15, 39],
    [1, 2, 3, 4, 5, 6, 7],
    [4, 6, 20, 24, 28, 34, 39]
]

STATS = [
    {'Christina Coleman': 1,
     'Margaret Rentas': 3,
     'Romana Hammond': 1,
     'Teresa Hoffman': 1,
     'Cheryl Sheehan': 1,
     'Violet Bishop': 1,
     'Ronald Vue': 1,
     'Eric Atkins': 1,
     'Jerome Figures': 1,
     'Edgardo Burke': 1},
    {'Todd Warner': 2,
     'Lon Heinrich': 2,
     'Donita Tedford': 1,
     'Sheri Hanna': 1,
     'Truman Randolph': 1,
     'Anthony Thomas': 1},
    {'Glenda Perry': 6,
     'Julie Piekarski': 6,
     'Kate Sibley': 6,
     'Deborah Aguiar': 6,
     'Susan Doyle': 6}
]

MATCHES = [
    {'Christina Coleman': [0],
     'Margaret Rentas': [7, 2, 2],
     'Romana Hammond': [1],
     'Teresa Hoffman': [1],
     'Cheryl Sheehan': [2],
     'Violet Bishop': [0],
     'Ronald Vue': [1],
     'Eric Atkins': [7],
     'Jerome Figures': [0],
     'Edgardo Burke': [1]},
    {'Todd Warner': [1, 1],
     'Lon Heinrich': [0, 1],
     'Donita Tedford': [1],
     'Sheri Hanna': [1],
     'Truman Randolph': [1],
     'Anthony Thomas': [1]},
    {'Glenda Perry': [2, 0, 2, 1, 1, 7],
     'Julie Piekarski': [2, 3, 2, 1, 1, 7],
     'Kate Sibley': [1, 0, 2, 1, 2, 7],
     'Deborah Aguiar': [2, 2, 1, 0, 0, 7],
     'Susan Doyle': [2, 3, 0, 2, 1, 7]}
]

HITS = [
    2,
    0,
    5,
]

RAREST = [
    [33, 9, 35, 24, 17, 27, 34],
    [6, 8, 11, 3, 10, 26, 39, 35, 7, 17, 25, 5, 12, 14, 34, 2, 22, 1, 19],
    [2, 33]
]
