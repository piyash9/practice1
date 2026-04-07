class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        else:
            self.__name = value
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name


obj = Person("piyash")
print(obj.name)
obj.name = "Alice"
print(obj.name)
del obj.name