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


class Cow(Livestock, DomesticAnimal):
    wool = False


class Goat(Livestock, DomesticAnimal):
    pass


class Sheep(Livestock, DomesticAnimal):
    color = 'brown'


class Pig(Livestock, DomesticAnimal):
    milk = False
    wool = False


class Poultry(DomesticAnimal):
    webbed_paw = False
    can_fly = True
    fluff = True


class Duck(Poultry, DomesticAnimal):
    webbed_paw = True


class Hen(Poultry, DomesticAnimal):
    can_fly = False


class Goose(Poultry, DomesticAnimal):
    webbed_paw = True
