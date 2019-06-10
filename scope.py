a = 250
c = [1,2,3]

def f1():
    b = a + 10
    c[0] = 5
    print(b)
    print(c)

def f2():
    a = 10
    print(a)

def f3():
    global a
    a = 100
    print(a)


f1()
f2()
print(a)
f3()
print(a)
print(c)
