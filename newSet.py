from collections import deque

class newset:
    def __init__(self):
        self.a = deque()

    def add(self, val):
        self.a.append(val)

    def pop(self):
        return self.a.popleft()

    def print_items(self):
        print(self.a)


val1 = newset()

new_val = val1
new_val.add(10)
new_val.add(20)
new_val.add(30)
new_val.add(50)
#
# for x in new_val:
#     print(x)
#
new_val.pop()
new_val.print_items()
#
# for x in new_val:
#     print(x)