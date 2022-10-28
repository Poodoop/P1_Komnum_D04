# Praktikum Komputasi Numerik 1
Program Algoritma Pemrosesan Akar Persamaan Metode Bolzano

- Muhammad Zufarrifqi Prakoso	5025201276
- Kadek Ari Dharmika	5025201239
- Elbert Dicky Aristyo	5025201231

Penjelasan Program:

1. Import Library
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pip import main
```

2. Bisection Method
```python
def bisection(f, a, b, tol=1e-5):
    if f(a)*f(b) > 0:
        print("No root in this interval")
        return None
    c = (a+b)/2.0
    while abs(f(c)) > tol:
        c = (a+b)/2.0
        data.append([a,f(a),b,f(b),c,f(c)])
        if f(c) == 0:
            return c
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return (a+b)/2.0,a,b
```
3. Show Results

```python
def show(data,x1,x2):
    df = pd.DataFrame(data,columns=['x1','f(x1)','x2','f(x2)','x3','f(x3)'])
    print(df)
```
4. Make Graph
```python
   x = np.linspace(x1,x2)
    f = lambda x: x**3 - 2*x**2 + 4*x - 8
    y = f(x)
    plt.plot(x,y)
    plt.show()
```


