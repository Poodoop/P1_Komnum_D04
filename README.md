# Praktikum Komputasi Numerik 1
Program Algoritma Pemrosesan Akar Persamaan Metode Bolzano

- Muhammad Zufarrifqi Prakoso	5025201276
- Kadek Ari Dharmika	5025201239
- Elbert Dicky Aristyo	5025201231

Link Demo : https://youtu.be/ssti-ew4eSg<br>
Penjelasan Program:

Misalkan fungsi yang diketahui: x^3 - 3x + 1

## 1. Import Libraries
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pip import main
```
Library yang perlu diimport agar dapat menjalankan program python adalah numpy untuk pembuatan array dan matplotlib untuk pembuatan grafik.

## 2. Bisection Method
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
Fungsi bisection ini menerapkan metode pencarian akar persamaan Bolzano, dimana nilai tengah dari selang x dicari agar semakin mendekati akar yang tepat. Fungsi akan memasukkan data-data x dan f(x) ke dalam array data yang dibuat.

## 3. Show Results
```python
def show(data,x1,x2):
    df = pd.DataFrame(data,columns=['x1','f(x1)','x2','f(x2)','x3','f(x3)'])
    print(df)
    x = np.linspace(x1,x2)
    f = lambda x: x**3 - 3*x + 1
    y = f(x)
    plt.plot(x,y)
    plt.show()
```
Fungsi show akan menunjukkan iterasi-iterasi dan grafik dari data yang dihasilkan fungsi bisection.

Hasil Print Iterasi:

![image](https://user-images.githubusercontent.com/55837575/198862907-b60e4ec7-b037-49d5-8440-c2b5dcdc98ab.png)

Hasil Print Grafik:

![image](https://user-images.githubusercontent.com/55837575/198862924-7a45adeb-2b29-4528-87b8-481ab03f3183.png)




