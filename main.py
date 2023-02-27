a = [1, 2, 3, 4, 5, 6, 7]
def d(x): return x-2


print(d(10))
b = list(map(lambda x: x+5, a))
print(b)

c = list(filter(lambda x: x % 2 == 0, a))
print(c)
