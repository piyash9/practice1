from collections import namedtuple

person = namedtuple('person', ["name", "age"])
p = person("piyash", 26)
print(p.name)
print(p.age)

num = namedtuple("num", ["x", "y"])
n = num(10, 20)
print(n.x)
print(n.y)














