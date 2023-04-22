def myfun(a):
    yield a * 2
    yield a * 3


x = myfun(10)
print(x)
print(next(x))
