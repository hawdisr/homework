def f1():
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    print(d)
    del d['B']
    print(d)

def f2():
    a = [10, 20, 30, 40, 50]
    print(a)
    del a[1]
    print(a)

def f3():
    t = ('A', 'B', 'C', 'D')
    print(t)
    a = list(t)
    del a[1]
    t = tuple(a)
    print(t)


f1()
print()
f2()
print()
f3()
