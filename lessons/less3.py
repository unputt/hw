class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f'{self.name}'


class POint:
    def __init__(self, *args):
        self.a = args

    def __len__(self):
        return len(self.a)

    def __abs__(self):
        return list(map(abs, self.a))


cat = Cat('beka')
print(cat)

s = POint(1, 2, 3, 3)
print(len(s))
print((abs(s)))
