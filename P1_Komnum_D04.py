
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pip import main

##make bisection method.
data = []

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

def show(data,x1,x2):
    df = pd.DataFrame(data,columns=['x1','f(x1)','x2','f(x2)','x3','f(x3)'])
    print(df)
    ## make graph from df
    x = np.linspace(x1,x2)
    f = lambda x: x**3 - 2*x**2 + 4*x - 8
    y = f(x)
    plt.plot(x,y)
    plt.show()
##main
if __name__ == '__main__':
    root,x1,x2= bisection(lambda x: x**3 - 3 *x + 1 ,1.5,3)
    print(x1,x2)
    print("root is",root," and f(root) is",root**3 - 3 *root + 1)
    show(data,x1,x2)


    



