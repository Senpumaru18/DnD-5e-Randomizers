from itertools import chain
from random import randint
# import Character # Needed for some weapon properties
def workspace():
# Space for all the weapons
    club = meleeWeapon('Club', 10, [1,4], 'bludgeoning', 2, [light()], 'Simple')
    dagger = meleeWeapon('Dagger', 200, [1,4], 'piercing', 1, [finesse(), light(), thrown([20,60])], 'Simple', [20,60])
    greatClub = meleeWeapon('Great Club', 20, [1,8], 'bludgeoning', 10, [two_handed()], 'Simple')
    handaxe = meleeWeapon('Handaxe', 500, [1,6], 'slashing', 2, [light(),thrown([20,60])], 'Simple', [20,60])
    javelin = meleeWeapon('Javelijn', 50, [1,6], 'piercing', 2, [thrown([30,120])], 'Simple', [30,120])
    lightHammer = meleeWeapon('Light Hammer', 200, [1,4], 'bludgeoning', 2, [light(), thrown([20,60])], 'Simple', [20,60])
    mace = meleeWeapon('Mace', 500, [1,6], 'bludgeoning', 4, [], 'Simple')
    quarterstaff = meleeWeapon('Quarterstaff', 20, [1,6], 'bludgeoning', 4, [versatile([1,8])], 'Simple')
    sickle = meleeWeapon('Sickle', 100, [1,4], 'slashing', 2, [light()], 'Simple')
    spear = meleeWeapon('Spear', 100, [1,6], 'piercing', 3, [thrown([20,60]), versatile([1,8])], 'Simple', [20,60])
    lightCrossbow = rangedWeapon('Crossbow, Light', 2500, [1,8], 'piercing', 5, [ammunition('bolt'), loading(), two_handed()], 'Simple', [80,320])
    # dart = rangedWeapon('Dart')
    # shortbow = rangedWeapon('Shortbow')
    # sling = rangedWeapon('Sling')
    # battleaxe = meleeWeapon('Battleaxe')
    # flail = meleeWeapon('Flail')
    # glaive = meleeWeapon('Glaive')
    # greateaxe = meleeWeapon('Greataxe')
    # greatsword = meleeWeapon('Greatsword')
    # halberd = meleeWeapon('Halberd')
    # lance = meleeWeapon('Lance')
    # longsword = meleeWeapon('Longsword')
    # maul = meleeWeapon('Maul')
    # morningstar = meleeWeapon('Morningstar')
    # pike = meleeWeapon('Pike')
    # rapier = meleeWeapon('Rapier')
    # scimitar = meleeWeapon('Scimitar')
    # shortsword = meleeWeapon('Shortsword')
    # trident = meleeWeapon('Trident')
    # warPick = meleeWeapon('War Pick')
    # warhammer = meleeWeapon('Warhammer')
    # whip = meleeWeapon('Whip')
    # blowgun = rangedWeapon('Blowgun')
    # handCrossbow = rangedWeapon('Crossbow, Hand')
    # heavyCrossbow = rangedWeapon('Crossbow, Heavy')
    # longbow = rangedWeapon('Longbow')
    # net = rangedWeapon('Net')
    

# Area to call functions
    print(dagger.getRange())
    # print(club.getWeight())


# Classes for various things
class Player:
    def __init__(self,STR,DEX,CON,INT,WIS,CHA):
        self.str = STR
        self.dex = DEX
        self.con = CON
        self.int = INT
        self.wis = WIS
        self.cha = CHA       
        
class property_:
    pass 
class ammunition(property_):
    def __init__(self, ammoType):
        self.ammoType = ammoType
class finesse(property_):
    def STRorDEX(choice, player):
        if choice == "str":
            return player.str
        elif choice == "dex":
            return player.dex
class heavy(property_):
    pass
class light(property_):
    pass
class loading(property_):
    pass
class reach(property_):
    pass
class thrown(property_):
    def __init__(self, _range):
        self.range = _range
class two_handed(property_):
    pass
class versatile(property_):
    def __init__(self, damage) -> None:
        self.damage = damage

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
class rangedWeapon(weapon):
    def __init__(self, name, cost, damage, dmgType, weight, properties, weaponGrade, _range):
        super().__init__(name, cost, damage, dmgType, weight, properties, weaponGrade)
        self.range = _range
    def getRange(self):
        return f"{self.range} ft"
class meleeWeapon(weapon):
    def __init__(self, name, cost, damage, dmgType, weight, properties, weaponGrade, _range=0):
        super().__init__(name, cost, damage, dmgType, weight, properties, weaponGrade)
        if _range != 0:
            self.range = _range
        else:
            pass
        for prop in self.properties:
            prop
    # def 


if __name__ == "__main__":
    workspace()