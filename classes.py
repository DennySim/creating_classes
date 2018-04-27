class DomesticAnimal:
    leg = None
    meat = None
    speed = 0

    def accelerate(self, value):
        self.speed += value

    def __init__(self, leg):
        self.leg = leg


class Livestock(DomesticAnimal):
    hoof = True
    horn = True
    milk = True
    wool = True


class Cow(Livestock):
    wool = False


class Goat(Livestock):
    pass


class Sheep(Livestock):
    color = 'brown'


class Pig(Livestock):
    milk = False
    wool = False


class Poultry(DomesticAnimal):
    webbed_paw = False
    can_fly = True
    fluff = True


class Duck(Poultry):
    webbed_paw = True


class Hen(Poultry):
    can_fly = False


class Goose(Poultry):
    webbed_paw = True
