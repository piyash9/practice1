
x = [1,2,3,4,5,6,7,8,9,1,10,11,12]

it = iter(x)
print(next(it))
print(next(it))
print(next(it))

# for i in x:
#     print(i)

class myclass:
    def __iter__(self):
        self.a = 1;
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


cls = myclass()

myiter = iter(myclass)

print(next(myiter))

