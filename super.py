
class A:
    def __init__(self):
        print("create class A")

    def f1(self):
        print("call the fun in f1")

class B(A):
    def __init__(self):
        print("create class B")
    def f2(self):
        print("call the fun f2")


class C(B):
    def __init__(self):
        super().__init__()
        print("create class C")
    def f3(self):
        print("call the fun f3")

a = C()
a.f1()
a.f2()
