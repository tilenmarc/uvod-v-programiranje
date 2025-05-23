def foo(x):
    a = 2
    for i in range(10):
        a = foo(4)

    return a


b = 4

c = foo(b)

print(c)
