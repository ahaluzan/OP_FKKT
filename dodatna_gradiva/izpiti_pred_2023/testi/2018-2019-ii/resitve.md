## 1. naloga

```
import numpy as np
def preberi_podatke(datoteka):
    with open(datoteka, "r", encoding="utf-8") as f:
        s={}
        vrstice=f.read().strip().split('\n')
        for v in vrstice:
            p=v.split(',')
            if p[0] not in s:
                s[p[0]]=[]
            s[p[0]].append(list(np.array(p[1:], dtype=int)))
            
    return s
```

## 2. naloga

```
def statistika_vplacil(vplacila):
    s={}
    for v in vplacila:
        s[v]=len(vplacila[v])
    return s
```

## 3. naloga  

```
def prestej_ujemanja(vplacane_kombinacije, dobitek):
    s=[]
    for k in vplacane_kombinacije:
        s.append(len(set(dobitek) & set(k)))

    return s
```

## 4. naloga

```
def prestej_sedmice(vplacila, dobitek):
    st = 0
    for v in vplacila:
        if dobitek in vplacila[v]:
            st+=1
    return st
```

## 5. naloga

```
def najmanj_pogosta_stevila(vplacila):
    st = {}
    for k,v in vplacila.items():
        for vp in v:
            for i in vp:
                if i not in st:
                    st[i]=0
                st[i]+=1
    m=min(st.values())
    for i in st:
        if m == st[i]:
            return i
```