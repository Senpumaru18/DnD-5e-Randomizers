def main():
    Arwyn = playerStats('Arwyn',15,20,16,10,18,12,'Changling',['Druid', 'Rogue'], [3,3],30)
    BOB = playerStats('BOB',16,18,20,8,12,20,'Human',['Fighter'],[20],45)
    
    print(Arwyn.allSkills())
    print(BOB.allSkills())
    
# DO NOT TOUCH ANYTHING PAST THIS
class playerStats:
    def __init__(self, name, strength, dexterity, constitution, intellegence, wisdom, charisma, race, _class, classLvl, speed):
        self.name = name
        self.str = strength
        self.dex = dexterity
        self.con = constitution
        self.int = intellegence
        self.wis = wisdom
        self.cha = charisma
        self.race = race
        self._class = _class
        self.level = classLvl
        self.speed = speed

    def strModifier(self):  # All xModifier converts the ability score into the corresponing modifier
        if self.str == 1:
            return -5
        elif self.str <= 3:
            return -4
        elif self.str <= 5:
            return -3
        elif self.str <= 7:
            return -2
        elif self.str <= 9:
            return -1
        elif self.str <= 11:
            return 0
        elif self.str <= 13:
            return 1
        elif self.str <= 15:
            return 2
        elif self.str <= 17:
            return 3
        elif self.str <= 19:
            return 4
        elif self.str <= 21:
            return 5
        elif self.str <= 23:
            return 6
        elif self.str <= 25:
            return 7
        elif self.str <= 27:
            return 8
        elif self.str <= 29:
            return 9
        elif self.str == 30:
            return 10
        else:
            return "That number is not valid, must be within 1-30"
    def dexModifier(self):
        if self.dex == 1:
            return -5
        elif self.dex <= 3:
            return -4
        elif self.dex <= 5:
            return -3
        elif self.dex <= 7:
            return -2
        elif self.dex <= 9:
            return -1
        elif self.dex <= 11:
            return 0
        elif self.dex <= 13:
            return 1
        elif self.dex <= 15:
            return 2
        elif self.dex <= 17:
            return 3
        elif self.dex <= 19:
            return 4
        elif self.dex <= 21:
            return 5
        elif self.dex <= 23:
            return 6
        elif self.dex <= 25:
            return 7
        elif self.dex <= 27:
            return 8
        elif self.dex <= 29:
            return 9
        elif self.dex == 30:
            return 10
        else:
            return "That number is not valid, must be within 1-30"
    def conModifier(self):
        if self.con == 1:
            return -5
        elif self.con <= 3:
            return -4
        elif self.con <= 5:
            return -3
        elif self.con <= 7:
            return -2
        elif self.con <= 9:
            return -1
        elif self.con <= 11:
            return 0
        elif self.con <= 13:
            return 1
        elif self.con <= 15:
            return 2
        elif self.con <= 17:
            return 3
        elif self.con <= 19:
            return 4
        elif self.con <= 21:
            return 5
        elif self.con <= 23:
            return 6
        elif self.con <= 25:
            return 7
        elif self.con <= 27:
            return 8
        elif self.con <= 29:
            return 9
        elif self.con == 30:
            return 10
        else:
            return "That number is not valid, must be within 1-30"
    def intModifier(self):
        if self.int == 1:
            return -5
        elif self.int <= 3:
            return -4
        elif self.int <= 5:
            return -3
        elif self.int <= 7:
            return -2
        elif self.int <= 9:
            return -1
        elif self.int <= 11:
            return 0
        elif self.int <= 13:
            return 1
        elif self.int <= 15:
            return 2
        elif self.int <= 17:
            return 3
        elif self.int <= 19:
            return 4
        elif self.int <= 21:
            return 5
        elif self.int <= 23:
            return 6
        elif self.int <= 25:
            return 7
        elif self.int <= 27:
            return 8
        elif self.int <= 29:
            return 9
        elif self.int == 30:
            return 10
        else:
            return "That number is not valid, must be within 1-30"
    def wisModifier(self):
        if self.wis == 1:
            return -5
        elif self.wis <= 3:
            return -4
        elif self.wis <= 5:
            return -3
        elif self.wis <= 7:
            return -2
        elif self.wis <= 9:
            return -1
        elif self.wis <= 11:
            return 0
        elif self.wis <= 13:
            return 1
        elif self.wis <= 15:
            return 2
        elif self.wis <= 17:
            return 3
        elif self.wis <= 19:
            return 4
        elif self.wis <= 21:
            return 5
        elif self.wis <= 23:
            return 6
        elif self.wis <= 25:
            return 7
        elif self.wis <= 27:
            return 8
        elif self.wis <= 29:
            return 9
        elif self.wis == 30:
            return 10
        else:
            return "That number is not valid, must be within 1-30"
    def chaModifier(self):
        if self.cha == 1:
            return -5
        elif self.cha <= 3:
            return -4
        elif self.cha <= 5:
            return -3
        elif self.cha <= 7:
            return -2
        elif self.cha <= 9:
            return -1
        elif self.cha <= 11:
            return 0
        elif self.cha <= 13:
            return 1
        elif self.cha <= 15:
            return 2
        elif self.cha <= 17:
            return 3
        elif self.cha <= 19:
            return 4
        elif self.cha <= 21:
            return 5
        elif self.cha <= 23:
            return 6
        elif self.cha <= 25:
            return 7
        elif self.cha <= 27:
            return 8
        elif self.cha <= 29:
            return 9
        elif self.cha == 30:
            return 10
        else:
            return "That number is not valid, must be within 1-30"
    def AC(self):           # Retrieves the info to make the character's Armor Class (AC)
        return self.DEX_modifier
    def getClass(self):     # Prints out all the classes and levels of the character
        for x in range(len(self._class)):
            print(f"lvl {self.level[x]} {self._class[x]}")
    def proficiencyBonus(self):
        totalLvl = 0
        for lvl in self.level:
            totalLvl += lvl
        if totalLvl <= 4:
            return f"{self.name} has a proficiency bonus of +2"
        elif totalLvl <= 8:
            return f"{self.name} has a proficiency bonus of +3"
        elif totalLvl <= 12:
            return f"{self.name} has a proficiency bonus of +4"
        elif totalLvl <= 16:
            return f"{self.name} has a proficiency bonus of +5"
        elif totalLvl <= 20:
            return f"{self.name} has a proficiency bonus of +6"
        else:
            return "exceeded current paramiters"
    def profBonus(self):
        totalLvl = 0
        for lvl in self.level:
            totalLvl += lvl
        if totalLvl <= 4:
            return 2
        elif totalLvl <= 8:
            return 3
        elif totalLvl <= 12:
            return 4
        elif totalLvl <= 16:
            return 5
        elif totalLvl <= 20:
            return 6
        else:
            return "exceeded current paramiters"
    def acrobatics(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.dexModifier()
        else:
            skill += self.dexModifier()
        return skill
    def animalHandling(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.wisModifier()
        else:
            skill += self.wisModifier()
        return skill
    def arcana(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.intModifier()
        else:
            skill += self.intModifier()
        return skill
    def athletics(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.strModifier()
        else:
            skill += self.strModifier()
        return skill
    def deception(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.chaModifier()
        else:
            skill += self.chaModifier()
        return skill
    def history(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.intModifier()
        else:
            skill += self.intModifier()
        return skill
    def insight(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.wisModifier()
        else:
            skill += self.wisModifier()
        return skill
    def intimidation(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.chaModifier()
        else:
            skill += self.chaModifier()
        return skill
    def investigation(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.intModifier()
        else:
            skill += self.intModifier()
        return skill
    def medicine(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.wisModifier()
        else:
            skill += self.wisModifier()
        return skill
    def nature(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.intModifier()
        else:
            skill += self.intModifier()
        return skill
    def perception(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.wisModifier()
        else:
            skill += self.wisModifier()
        return skill
    def performance(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.chaModifier()
        else:
            skill += self.chaModifier()
        return skill
    def persuasion(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.chaModifier()
        else:
            skill += self.chaModifier()
        return skill
    def religion(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.intModifier()
        else:
            skill += self.intModifier()
        return skill
    def sleightOfHand(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.dexModifier()
        else:
            skill += self.dexModifier()
        return skill
    def stealth(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.dexModifier()
        else:
            skill += self.dexModifier()
        return skill
    def survival(self, proficiency=0):
        skill = 0
        if proficiency != 0:
            skill += self.profBonus() + self.wisModifier()
        else:
            skill += self.wisModifier()
        return skill
    def allSkills(self):
        return self.acrobatics(),self.animalHandling(),self.arcana(),self.athletics(),self.deception(),self.history(),self.insight(),self.intimidation(),self.investigation(),self.medicine(),self.nature(),self.perception(),self.performance(),self.persuasion(),self.religion(),self.sleightOfHand(),self.stealth(),self.survival()
    


if __name__ == "__main__":
    main()
