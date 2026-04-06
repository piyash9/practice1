from functools import reduce
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def even_num(n):
    return n % 2 == 0

x1 = list(filter(even_num, x))
print(x1)

def add(n):
    return n + 2;

x2 = list(map(add, x))
print(x2)

def sum(a, b):
    return a+b;


x3 = float(reduce(sum, x))
print(x3 / len(x))

