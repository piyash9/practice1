class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

obj = Cat()
obj.speak()


class Bird:
    def sound(self):
        print("Bird makes sound")

class Dog:
    def sound(self):
        print("Dog barks")

for animal in [Bird(), Dog()]:
    animal.sound()