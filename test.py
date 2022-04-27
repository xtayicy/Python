print("test")

print(100 + 200)

#name = input("Please input your name: ")
#print(name)

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
print(ord('A'))
print(chr(66))

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

n = 1
while n <= 100:
    if n > 3:
        break
    print(n)
    n = n + 1
print('END')

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

s = set([1, 2, 3])
print(s)
s.add(4)
print(s)

print(abs(-20))
print(int('123'))
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
import math
print(math.sqrt(2))

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
import os
print([d for d in os.listdir('.')])
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

def f(x):
    return x * x
m = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(m)
def add(x, y):
    return x + y
r = reduce(add, [1, 3, 5, 7, 9])
print(r)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())

print(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()

import module
module.test()