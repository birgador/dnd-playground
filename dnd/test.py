import random
class A:
    def __init__(self):
        print('Initializing: class A')
        self.val = random.randint(1,10)

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()
        self.ufff = "bb"

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(A):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()
        self.ufff ='cc'

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)



x,y,z = A(),B(),C()

print(x.val)
print(y.val,y.ufff)
print(z.val,z.ufff)