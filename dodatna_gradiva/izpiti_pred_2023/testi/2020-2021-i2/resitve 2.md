# Naloga 1

```python
def preberi_temperaturo(ime):
    f = open(ime, encoding="utf8")
    s = []
    f.readline()    
    for l in f:
        y,c,t = l.strip().split(";")
        t,u = t.split("+-")
        t = round(float(t),2)
        u = round(float(u),2)
        s.append((int(y),c,t,u))
    return s
```

# Naloga 2

```python
def presezek(s, t_min, y_max=None):
    cs = set()
    for y, c, t, _ in s:
        if y_max and y > y_max:
            continue
        if t >= t_min:
            cs.add(c)              
    return cs
```    

# Naloga 3

```python
def slovarji(s):
    d = {}
    for y, c, t, _ in s:
        if c not in d:
            d[c] = {}
        d[c][y] = t
    return d
```
    
# Naloga 4

```python
def visanje_po_letih(d, drzava, start, stop):
    if drzava not in d:
        return None
    T = d[drzava]
    dT = []
    for y in range(start, stop):
        if (y+1 in T) and (y in T):
            dT.append(T[y+1]-T[y])
    if dT:
        return round(sum(dT)/len(dT),2)
    return None
```
    
# Naloga 5

```python
def najvecje_povisanje(s):
    naj_c = None
    naj_T = 0
    
    for c, T in s:
        if T > naj_T:
            naj_T = T
            naj_c = c
    return naj_c
```