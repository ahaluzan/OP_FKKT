kava5 = [(25, 'F', 'Cappuccino', 'M', 3.5, 4.7),
 (34, 'M', 'Latte', 'L', 4.0, 4.2),
 (19, 'F', 'Espresso', 'S', 2.5, 4.9),
 (45, 'M', 'Cappuccino', 'L', 3.8, 3.9)]

slovar_izdelek5 = {'Cappuccino': [(25, 'F', 'M', 3.5, 4.7), (45, 'M', 'L', 3.8, 3.9)],
 'Espresso': [(19, 'F', 'S', 2.5, 4.9)],
 'Latte': [(34, 'M', 'L', 4.0, 4.2)]}

slovar_spol5 = {'F': [(25, 'Cappuccino', 'M', 3.5, 4.7), (19, 'Espresso', 'S', 2.5, 4.9)],
 'M': [(34, 'Latte', 'L', 4.0, 4.2), (45, 'Cappuccino', 'L', 3.8, 3.9)]}

statistika5 = {'Cappuccino': 3.65, 'Espresso': 2.5, 'Latte': 4.0}

po_spolu5 = {'samo_f': {'Espresso'}, 'samo_m': {'Latte'}, 'skupno': {'Cappuccino'}}

kava10 = [(22, 'F', 'Latte', 'S', 3.57, 4.3),
 (31, 'M', 'Espresso', 'M', 2.75, 4.0),
 (27, 'F', 'Cappuccino', 'L', 3.9, 4.8),
 (19, 'F', 'Cold Brew', 'M', 3.6, 4.6),
 (54, 'M', 'Latte', 'S', 3.1, 3.9),
 (36, 'F', 'Americano', 'M', 2.95, 4.4),
 (23, 'F', 'Flat White', 'S', 3.75, 4.5),
 (29, 'M', 'Espresso', 'M', 2.6, 3.8)]

slovar_izdelek10 = {'Americano': [(36, 'F', 'M', 2.95, 4.4)],
 'Cappuccino': [(27, 'F', 'L', 3.9, 4.8)],
 'Cold Brew': [(19, 'F', 'M', 3.6, 4.6)],
 'Espresso': [(31, 'M', 'M', 2.75, 4.0), (29, 'M', 'M', 2.6, 3.8)],
 'Flat White': [(23, 'F', 'S', 3.75, 4.5)],
 'Latte': [(22, 'F', 'S', 3.57, 4.3), (54, 'M', 'S', 3.1, 3.9)]}

slovar_spol10 = {'F': [(22, 'Latte', 'S', 3.57, 4.3),
       (27, 'Cappuccino', 'L', 3.9, 4.8),
       (19, 'Cold Brew', 'M', 3.6, 4.6),
       (36, 'Americano', 'M', 2.95, 4.4),
       (23, 'Flat White', 'S', 3.75, 4.5)],
 'M': [(31, 'Espresso', 'M', 2.75, 4.0),
       (54, 'Latte', 'S', 3.1, 3.9),
       (29, 'Espresso', 'M', 2.6, 3.8)]}

statistika10 = {'Americano': 2.95,
 'Cappuccino': 3.9,
 'Cold Brew': 3.6,
 'Espresso': 2.67,
 'Flat White': 3.75,
 'Latte': 3.33}

po_spolu10 = {'samo_f': {'Americano', 'Cold Brew', 'Cappuccino', 'Flat White'},
 'samo_m': {'Espresso'},
 'skupno': {'Latte'}}

kava20 = [(25, 'F', 'Cappuccino', 'M', 3.55, 4.6),
 (33, 'M', 'Latte', 'L', 4.05, 4.0),
 (41, 'F', 'Espresso', 'S', 2.45, 4.9),
 (52, 'F', 'Cold Brew', 'L', 4.35, 4.4),
 (20, 'M', 'Cappuccino', 'S', 3.15, 4.2),
 (37, 'F', 'Latte', 'M', 3.65, 4.7),
 (24, 'F', 'Flat White', 'L', 4.25, 4.5),
 (58, 'M', 'Espresso', 'M', 2.55, 3.9),
 (31, 'F', 'Mocha', 'L', 4.45, 4.8),
 (44, 'F', 'Cappuccino', 'S', 3.35, 4.3),
 (35, 'M', 'Latte', 'S', 3.25, 3.7),
 (22, 'F', 'Espresso', 'M', 2.65, 4.6),
 (49, 'M', 'Flat White', 'M', 4.05, 4.0),
 (26, 'F', 'Americano', 'L', 3.05, 4.4),
 (30, 'F', 'Cold Brew', 'S', 3.85, 4.9),
 (42, 'M', 'Cappuccino', 'L', 3.75, 4.2)]

slovar_izdelek20 = {'Americano': [(26, 'F', 'L', 3.05, 4.4)],
 'Cappuccino': [(25, 'F', 'M', 3.55, 4.6),
                (20, 'M', 'S', 3.15, 4.2),
                (44, 'F', 'S', 3.35, 4.3),
                (42, 'M', 'L', 3.75, 4.2)],
 'Cold Brew': [(52, 'F', 'L', 4.35, 4.4), (30, 'F', 'S', 3.85, 4.9)],
 'Espresso': [(41, 'F', 'S', 2.45, 4.9), (58, 'M', 'M', 2.55, 3.9), (22, 'F', 'M', 2.65, 4.6)],
 'Flat White': [(24, 'F', 'L', 4.25, 4.5), (49, 'M', 'M', 4.05, 4.0)],
 'Latte': [(33, 'M', 'L', 4.05, 4.0), (37, 'F', 'M', 3.65, 4.7), (35, 'M', 'S', 3.25, 3.7)],
 'Mocha': [(31, 'F', 'L', 4.45, 4.8)]}

slovar_spol20 = {'F': [(25, 'Cappuccino', 'M', 3.55, 4.6),
       (41, 'Espresso', 'S', 2.45, 4.9),
       (52, 'Cold Brew', 'L', 4.35, 4.4),
       (37, 'Latte', 'M', 3.65, 4.7),
       (24, 'Flat White', 'L', 4.25, 4.5),
       (31, 'Mocha', 'L', 4.45, 4.8),
       (44, 'Cappuccino', 'S', 3.35, 4.3),
       (22, 'Espresso', 'M', 2.65, 4.6),
       (26, 'Americano', 'L', 3.05, 4.4),
       (30, 'Cold Brew', 'S', 3.85, 4.9)],
 'M': [(33, 'Latte', 'L', 4.05, 4.0),
       (20, 'Cappuccino', 'S', 3.15, 4.2),
       (58, 'Espresso', 'M', 2.55, 3.9),
       (35, 'Latte', 'S', 3.25, 3.7),
       (49, 'Flat White', 'M', 4.05, 4.0),
       (42, 'Cappuccino', 'L', 3.75, 4.2)]}

statistika20 = {'Americano': 3.05,
 'Cappuccino': 3.45,
 'Cold Brew': 4.1,
 'Espresso': 2.55,
 'Flat White': 4.15,
 'Latte': 3.65,
 'Mocha': 4.45}

po_spolu20 = {'samo_f': {'Americano', 'Cold Brew', 'Mocha'},
 'samo_m': set(),
 'skupno': {'Latte', 'Cappuccino', 'Flat White', 'Espresso'}}

slovar_spol_samo_m = {'M': [(30, 'Latte', 'L', 4.57, 4.0), (50, 'Mocha', 'S', 3.0, 3.5)]}

po_spolu_samo_m = {'skupno': set(), 'samo_m': {'Latte', 'Mocha'}, 'samo_f': set()}