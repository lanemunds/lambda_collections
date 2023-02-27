import collections
from collections import Counter, namedtuple, deque

c = Counter('helloworld')
print(c['l'])
f = Counter(['a', 'd', 'f'])
print(c)
d = Counter(cats=4, dogs=7)
print(d)
print(list(d.elements()))
print(c.most_common(2))

e = Counter(a=4, b=2, c=4, d=-2)
a = ['a', 'b', 'c', 'd']
e.subtract(a)
print(e)
e.update(a)
print(e)


Point = namedtuple('Point','x y z')
newP = Point(3,4,5)
print(newP._asdict())

print(newP)

j = deque('hello', maxlen=10)
print(j)

j.extend('456')
print(j)

j.rotate(5)
print(j)
j.extend('789')
print(j)