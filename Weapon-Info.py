from random import randint
import Character # Needed for some weapon properties
def workspace():
# Space for all the weapons
    club = meleeWeapon('Club', 10, [1,4], 'bludgeoning', 2, ['light'], 'Simple')
    dagger = meleeWeapon('Dagger', 200, [1,4], 'piercing', 1, ['finesse', 'light', 'thrown', '20/60'], 'Simple')

# Area to call functions
    print(dagger.getRange)
    # print(club.getWeight())


# Classes for various things
class weapon:
    def __init__(self, name, cost, damage, dmgType, weight, properties, weaponGrade):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.dmgType = dmgType
        self.weight = weight
        self.properties = properties
        self.weaponGrade = weaponGrade
    def getCost(self):
        # return self.cost
        copper = 0
        silver = 0
        gold = 0
        platinum = 0
        cost = self.cost
        while cost > 0:
            if cost >= 1000:
                cost -= 1000
                platinum += 1
            elif cost >= 100:
                cost -= 100
                gold += 1
            elif cost >= 10:
                cost -= 10
                silver += 1
            else:
                copper += cost
                cost -= cost
        if platinum > 0 and gold > 0 and silver > 0 and copper > 0:
            return f"{platinum} pp, {gold} gp, {silver} sp, {copper} cp"
        elif platinum > 0 and gold > 0 and silver > 0:
            return f"{platinum} pp, {gold} gp, {silver} sp"
        elif platinum > 0 and gold > 0 and copper > 0:
            return f"{platinum} pp, {gold} gp, {copper} cp"
        elif platinum > 0 and silver > 0 and copper > 0:
            return f"{platinum} pp, {silver} sp, {copper} cp"
        elif platinum > 0 and gold > 0:
            return f"{platinum} pp, {gold} gp"
        elif platinum > 0 and silver > 0:
            return f"{platinum} pp, {silver} sp"
        elif platinum > 0 and copper > 0:
            return f"{platinum} pp, {copper} cp"
        elif platinum > 0:
            return f"{platinum} pp"
        elif gold > 0 and silver > 0 and copper > 0:
            return f"{gold} gp, {silver} sp, {copper} cp"
        elif gold > 0 and silver > 0:
            return f"{gold} gp, {silver} sp"
        elif gold > 0 and copper > 0:
            return f"{gold} gp, {copper} cp"
        elif gold > 0:
            return f"{gold} gp"
        elif silver > 0 and copper > 0:
            return f"{silver} sp, {copper} cp"
        elif silver > 0:
            return f"{silver} sp"
        else:
            return f"{copper} cp"
    def getDamage(self):
        return f"{self.damage[0]}d{self.damage[1]} {self.dmgType}"
    def getDmgType(self):
        return self.dmgType
    def getWeaponGrade(self):
        return self.weaponGrade
    def getWeight(self):
        return f"{self.weight} lb."
    def getProperties(self):
        return self.properties
    def rollDamage(self, crit=0): # crit will auto be 0 in place of no and if anything else is taken for crit it will mean that it is rolling for a critical hit
        damage = 0
        if crit == 0:
            for i in range(self.damage[0]):
                damage += randint(1, self.damage[1])
        else:
            for i in range(self.damage[0]*2):
                damage += randint(1, self.damage[1])
        return f"{damage} {self.dmgType}"

class property():
    pass
class thrown(property):
    def __init__(self, _range):
        self.range = _range
    
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
    def rollVersDmg(self, crit=0):
        damage = 0
        if crit == 0:
            for i in range(self.damage[0]):
                damage += randint(1, self.damage[1])
        else:
            for i in range(self.damage[0]*2):
                damage += randint(1, self.damage[1])
        return damage

class rangedWeapon(weapon):
    def __init__(self, name, cost, damage, dmgType, weight, properties, weaponGrade, _range):
        super().__init__(name, cost, damage, dmgType, weight, properties, weaponGrade)
        self.range = _range
    def getRange(self):
        return self.range
class meleeWeapon(weapon):
    def __init__(self, name, cost, damage, dmgType, weight, properties, weaponGrade):
        super().__init__(name, cost, damage, dmgType, weight, properties, weaponGrade)
        for property in self.properties:
            if property == 'thrown':
                thrown(properties[property+1])
            else:
                pass
    def getRange(self):
        return self.range


if __name__ == "__main__":
    workspace()