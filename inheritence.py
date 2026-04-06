
class A:
    def __init__(self):
        print("create class A")

    def f1(self):
        print("call the fun in f1")

class B:
    def __init__(self):
        print("create class B")
    def f1(self):
        print("call the fun f2")


class C(B, A):
    def __init__(self):
        super().__init__()
    # def f1(self):
    #     print("call the fun f3")

a = C()
a.f1()

