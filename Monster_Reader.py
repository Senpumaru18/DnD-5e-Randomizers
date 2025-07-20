from random import randint

Monsters = {"Goblin" : {"HP" : 7, "AC" : 15, "Initiative" : 2, "Strength" : 8, "Dexterity" : 14, "Constitution" : 10, "Inteligence" : 10, "Wisdom" : 8, "Charisma" : 8, "AttackRoll" : 4, "Attacks" : 1, "Dice" : 1, "Sides" : 6, "Add" : 2},
            "Boar" : {"HP" : 11, "AC" : 11, "Initiative" : 0, "Strength" : 13, "Dexterity" : 11, "Constitution" : 12, "Inteligence" : 2, "Wisdom" : 9, "Charisma" : 5, "AttackRoll" : 3, "Attacks" : 1, "Dice" : 1, "Sides" : 6, "Add" : 1},
            "Tarrasque" : {"HP" : 676, "AC" : 20, "Initiative" : 0, "Strength" : 30, "Dexterity" : 11, "Constitution" : 30, "Inteligence" : 3, "Wisdom" : 11, "Charisma" : 11, "AttackRoll" : 5, "Attacks" : 5, "Dice" : 4, "Sides" : 10, "Add" : 10},
            "False Hydra (10 Heads)" : {"HP" : 990, "AC" : 14, "Initiative" : 0, "Strength" : 16, "Dexterity" : 10, "Constitution" : 18, "Inteligence" : 12, "Wisdom" : 20, "Charisma" : 8, "AttackRoll" : 7, "Attacks" : 10, "Dice" : 3, "Sides" : 8, "Add" : 3}}

def XdX(sides,number=1):
    sum = 0
    for n in range(number):
        sum += randint(1,sides)
    return sum

class Monster:
    def __init__(self, name, creature):
        self.name = name
        self.creature = creature
        self.HP = 0
        self.AC = 0
        self.Initiative = 0
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.attackRoll = 0
        self.attacks = 0
        self.dice = 0
        self.sides = 0
        self.add = 0

        for id in Monsters[self.creature]:
            match id:
                case "HP": self.HP = Monsters[self.creature][id]
                case "AC": self.AC = Monsters[self.creature][id]
                case "Initiative": self.Initiative = Monsters[self.creature][id]
                case "Strength": self.strength = Monsters[self.creature][id]
                case "Dexterity": self.dexterity = Monsters[self.creature][id]
                case "Constitution": self.constitution = Monsters[self.creature][id]
                case "Inteligence": self.intelligence = Monsters[self.creature][id]
                case "Wisdom": self.wisdom = Monsters[self.creature][id]
                case "Charisma": self.charisma = Monsters[self.creature][id]
                case "AttackRoll": self.attackRoll = Monsters[self.creature][id]
                case "Attacks": self.attacks = Monsters[self.creature][id]
                case "Dice": self.dice = Monsters[self.creature][id]
                case "Sides": self.sides = Monsters[self.creature][id]
                case "Add": self.add = Monsters[self.creature][id]
    def attack_roll(self):
        roll = self.attackRoll + XdX(20)
        return roll
    def attack(self):
        damage = 0
        for x in range(self.attacks):
            damage += XdX(self.sides,self.dice) + self.add
        return damage
    def getName(self):
        return self.name
    def getHP(self):
        return self.HP
    def getAC(self):
        return self.AC
    def getInitiative(self):
        return self.Initiative
    def getStrength(self):
        self.strength
    def getDexterity(self):
        self.dexterity
    def getConstitution(self):
        self.constitution
    def getIntelligence(self):
        self.intelligence
    def getWisdom(self):
        self.wisdom
    def getCharisma(self):
        self.charisma
        
    def print_self(self):
        for attr_name in vars(self):
            print(f"{attr_name} : {getattr(self, attr_name)}")

def Combat(Participant1, Participant2):
    HP_1 = Participant1.getHP()
    AC_1 = Participant1.getAC()
    HP_2 = Participant2.getHP()
    AC_2 = Participant2.getAC()
    Initiative_1 = Participant1.getInitiative() + XdX(20)
    Initiative_2 = Participant2.getInitiative() + XdX(20)

    print(f"Intitative rolls are:\n{Participant1.getName()} : {Initiative_1}\n{Participant2.getName()} : {Initiative_2}\n")

    while(HP_1 >= 0 or HP_2 >= 0):
        # input("Press enter to continue\n")
        if Initiative_1 > Initiative_2:
            attackRoll1 = Participant1.attack_roll()
            print(f"{Participant1.getName()} rolled {attackRoll1} to attack")
            if attackRoll1 >= AC_2:
                dmg = Participant1.attack()
                HP_2 -= dmg
                print(f"\n{Participant1.getName()} hit and dealt {dmg} damage\n")
                print(f"{Participant2.getName()} has {HP_2} Health left\n")
            else:
                print("They missed thier Attack\n")
            if HP_2 > 0:
                attackRoll2 = Participant2.attack_roll()
                print(f"{Participant2.getName()} rolled {attackRoll2} to attack")
                if attackRoll2 >= AC_1:
                    dmg = Participant2.attack()
                    HP_1 -= dmg
                    print(f"\n{Participant2.getName()} hit and dealt {dmg} damage\n")
                    print(f"{Participant1.getName()} has {HP_1} Health left\n")
                else:
                    print("They missed thier Attack\n")
        elif Initiative_2 > Initiative_1:
            attackRoll2 = Participant2.attack_roll()
            print(f"{Participant2.getName()} rolled {attackRoll2} to attack")
            if attackRoll2 >= AC_1:
                dmg = Participant2.attack()
                HP_1 -= dmg
                print(f"\n{Participant2.getName()} hit and dealt {dmg} damage\n")
                print(f"{Participant1.getName()} has {HP_1} Health left\n")
            else:
                print("They missed thier Attack\n")
            if HP_1 > 0:
                attackRoll1 = Participant1.attack_roll()
                print(f"{Participant1.getName()} rolled {attackRoll1} to attack")
                if attackRoll1 >= AC_2:
                    dmg = Participant1.attack()
                    HP_2 -= dmg
                    print(f"\n{Participant1.getName()} hit and dealt {dmg} damage\n")
                    print(f"{Participant2.getName()} has {HP_2} Health left\n")
                else:
                    print("They missed thier Attack\n")
        else:
            if Participant1.getInitiative() > Participant2.getInitiative():
                attackRoll1 = Participant1.attack_roll()
                print(f"{Participant1.getName()} rolled {attackRoll1} to attack")
                if attackRoll1 >= AC_2:
                    dmg = Participant1.attack()
                    HP_2 -= dmg
                    print(f"\n{Participant1.getName()} hit and dealt {dmg} damage\n")
                    print(f"{Participant2.getName()} has {HP_2} Health left\n")
                else:
                    print("They missed thier Attack\n")
                if HP_2 > 0:
                    attackRoll2 = Participant2.attack_roll()
                    print(f"{Participant2.getName()} rolled {attackRoll2} to attack")
                    if attackRoll2 >= AC_1:
                        dmg = Participant2.attack()
                        HP_1 -= dmg
                        print(f"\n{Participant2.getName()} hit and dealt {dmg} damage\n")
                        print(f"{Participant1.getName()} has {HP_1} Health left\n")
                    else:
                        print("They missed thier Attack\n")
            else:
                attackRoll2 = Participant2.attack_roll()
                print(f"{Participant2.getName()} rolled {attackRoll2} to attack")
                if attackRoll2 >= AC_1:
                    dmg = Participant2.attack()
                    HP_1 -= dmg
                    print(f"\n{Participant2.getName()} hit and dealt {dmg} damage\n")
                    print(f"{Participant1.getName()} has {HP_1} Health left\n")
                else:
                    print("They missed thier Attack\n")
                if HP_1 > 0:
                    attackRoll1 = Participant1.attack_roll()
                    print(f"{Participant1.getName()} rolled {attackRoll1} to attack")
                    if attackRoll1 >= AC_2:
                        dmg = Participant1.attack()
                        HP_2 -= dmg
                        print(f"\n{Participant1.getName()} hit and dealt {dmg} damage\n")
                        print(f"{Participant2.getName()} has {HP_2} Health left\n")
                    else:
                        print("They missed thier Attack\n")
                
        if HP_1 <= 0:
            print(f"{Participant1.getName()} has Died\n\n{Participant2.getName()} is the Winner")
            return Participant1.getName()
        if HP_2 <= 0:
            print(f"{Participant2.getName()} has Died\n\n{Participant1.getName()} is the Winner")
            return Participant2.getName()
            

def QuickRunCombat(Fighter1, Fighter2, Combats):
    Wins_1 = 0
    Wins_2 = 0
    for x in range(Combats):
        winner = Combat(Fighter1, Fighter2)
        if winner == Fighter1.getName():
            Wins_1 += 1
        if winner == Fighter2.getName():
            Wins_2 += 1
    print(f"{Fighter1.getName()} wins : {Wins_1} times out of {Combats}\n{Fighter2.getName()} wins : {Wins_2} times out of {Combats}")

def Main():
    Boblin = Monster("Boblin", "Goblin")
    Tom = Monster("Tom", "Boar")
    Terry = Monster("Terry", "Tarrasque")
    Hydra = Monster("Hydra", "False Hydra (10 Heads)")
    

    # Combat(Terry,Hydra)
    QuickRunCombat(Terry,Hydra,1000000)
    # print(Boblin.attack_roll())
    # print()
    # print(Tom.attack())



if __name__ == "__main__":
    Main()