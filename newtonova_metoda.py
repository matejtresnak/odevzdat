def newtonova_metoda(fn, dfn, x, tol=0.001, lim=100):
    for i in range(lim):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew - x) < tol: break
        x = xnew
    return xnew

y = lambda x: x**2 - 1
dy = lambda x: 2*x

n = newtonova_metoda(y, dy, 5)
print(n)
