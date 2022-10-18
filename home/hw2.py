from homewr1 import Hero


class Air(Hero):
    esey = 3

    def init(self, name, nickname, hp, damage, fly=False):
        super().init(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')

    def Gen_x(self):
        pass



class Earthly(Hero):
    legs = 2

    def __init(self, name, nickname, hp, damage, fly=False):
        super().init(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')

    def Gen_x(self):
        pass



class Space(Hero):
    arms = 8

    def __init(self, name, nickname, hp, damage, fly=False):
        super().init(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')

    def __Gen_x(self):
        pass

hero1 = Air(name='Alexsey', nickname='Alex', hp=100, damage=50)
hero2 = Earthly(name='Jonnar', nickname='Joni', hp=100, damage=30)
hero3 = Space(name='Lukas', nickname='Luk', hp=100, damage=40)
hero1.brand_phrase()
