def my_function(x = 5):
    return x * x

print(my_function(7))



def my_function(animal, name, age = 27):
  print("I have a", age, "year old", animal, "named", name)

my_function( animal = "Buddy", name = 5)



def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


x = lambda a, b : a + b;

print(x(10, 20))
