def foo(list):
    return [i for i in list if i > 0]

def foo2(list):
    return [i if not isinstance(i, str) else 0 for i in list ]

def foo3(list):
    return sum([float(i) for i in list])

print(foo([-5, 3, -1, 101]))
print(foo2([-5, 3, -1, 101, 'no']))
print(foo3(['1.2', '2.6', '3.3']))