def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)



def func():
  n = 1
  while n <= 10:
    yield n
    n += 1

for i in func():
  print(i)



def fun1():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

x = fun1()

for i in x:
  print(i)
  x.close()