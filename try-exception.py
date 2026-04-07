
a = 5
b = 0

try:
    print(a / b)
except ZeroDivisionError as D1:
    print("kjbewkjbcew")
except ValueError as v1:
    print(v1)
except Exception as e:
    print(e)
finally:
    print("there are two number")
