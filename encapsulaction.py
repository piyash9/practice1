
class A:
    def __init__(self, b, c):
        self.__b = b
        self.__c = c

    def get_b(self):
        return self.__b

    def set_b(self, b):
        self.__b = b

my_a = A("cnekvc", "nerln")

print(my_a.get_b())
my_a.set_b("nnekce")
print(my_a.get_b())