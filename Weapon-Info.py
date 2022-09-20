import random
import Character # Needed for some weapon properties


def main():
    club = Weapon("Club", "1sp", (1, 4), "Bludgeoning", "melee", "2 lb", ["light"], "Simple Melee")
    print(club.get_damage())

    counter = 0
    for i in range(10):
        counter += club.roll_damage()
    print(counter)


# Classes for various things


class Weapon:
    def __init__(self, name, cost, damage, dmgType, weight, properties):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.dmgType = dmgType
        self.weight = weight
        self.properties = properties
    def get_cost(self):
        return self.cost
    def get_damage(self):
        return f"{self.damage[0]}d{self.damage[1]} {self.dmgType}"
    def get_dmgType(self):
        return self.dmgType
    def get_Range(self):
        return self.range
    def get_weight(self):
        return self.weight
    def get_properties(self):
        return self.properties
    def roll_damage(self):
        counter = 0
        for i in range(self.damage[0]):
            counter += random.randint(1, self.damage[1])
        return counter
class RangeWeapon(Weapon):
    def __init__(self, name, cost, damage, dmgType, weight, properties, weaponType):
        # super().__init__(name, cost, damage, dmgType, weight, properties, weaponType)
        self.weaponType = weaponType

    def get_weaponType(self):
        return self.weaponType

class property():
    pass
class thrown(property):
    def __init__(self, Range):
        self.range = Range
class ammunition(property):
    def __init__(self, ammoType):
        self.ammoType = ammoType
class finnesse(property):
    def STRorDEX(choice, player):
        if choice == "str":
            return player.STR_modifier
        elif choice == "dex":
            return Character.player.DEX_modifier
class heavy(property):
    pass
class light(property):
    pass
class loading(property):
    pass
class reach(property):
    pass
class thrown(property):
    def __init__(self, Range):
        self.range = Range
class two_handed(property):
    pass
class versatile(property):
    pass

if __name__ == "__main__":
    main()