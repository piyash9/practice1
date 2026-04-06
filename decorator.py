



def decorator(func):
    def inner(a, b):
        if a < b:
            a,b = b,a
        return func(a, b)
    return inner

# devision = decorator(devision)

@decorator
def devision(a, b):
    return a / b

x = devision(3, 9)
print(x)