def main():
    Arwyn = playerStats('Arwyn',15,20,16,10,18,12,'Changling',['Druid','Rogue'], [3,3],30, ['acrobatics', 'arcana', 'deception', 'history', 'medicine'])
    BOB = playerStats('BOB',16,18,20,8,12,20,'Human',['Fighter'],[20],45,['athletics','animal handling'])
    
    print(Arwyn.functions())
    print(BOB.allSkills())
    
# DO NOT TOUCH ANYTHING PAST THIS
class playerStats:
    def __init__(self, name, strength, dexterity, constitution, intellegence, wisdom, charisma, race, _class, classLvl, speed, proficiency):
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
        self.prof = proficiency
    def savingProf(self):
        saves = []
        if self._class[0] == 'Barbarian':
            saves += 'strength', 'constitution'
        elif self._class[0] == 'Bard':
            saves += 'dexterity','charisma'
        elif self._class[0] == 'Cleric':
            saves += 'wisdom','charisma'
        elif self._class[0] == 'Druid':
            saves += 'intelegence','wisdom'
        elif self._class[0] == 'Fighter':
            saves += 'strength','constitution'
        elif self._class[0] == 'Monk':
            saves += 'strength','dexterity'
        elif self._class[0] == 'Paladin':
            saves += 'wisdom','charisma'
        elif self._class[0] == 'Ranger':
            saves += 'strength','dexterity'
        elif self._class[0] == 'Rogue':
            saves += 'dexterity','intelegence'
        elif self._class[0] == 'Sorcerer':
            saves += 'constitution','charisma'
        elif self._class[0] == 'Warlcok':
            saves += 'wisdom','charisma'
        elif self._class[0] == 'Wizard':
            saves += 'intelegence','wisdom'
        return saves
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
    def acrobatics(self):
        skill = 0
        for prof in self.prof:
            if prof == 'acrobatics':
                skill += self.profBonus() + self.dexModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.dexModifier()
        else:
            pass
        return skill
    def animalHandling(self):
        skill = 0
        for prof in self.prof:
            if prof == 'animal handling':
                skill += self.profBonus() + self.wisModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.wisModifier()
        else:
            pass
        return skill
    def arcana(self):
        skill = 0
        for prof in self.prof:
            if prof == 'arcana':
                skill += self.profBonus() + self.intModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.intModifier()
        else:
            pass
        return skill
    def athletics(self):
        skill = 0
        for prof in self.prof:
            if prof == 'athletics':
                skill += self.profBonus() + self.strModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.strModifier()
        else:
            pass
        return skill
    def deception(self):
        skill = 0
        for prof in self.prof:
            if prof == 'deception':
                skill += self.profBonus() + self.chaModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.chaModifier()
        else:
            pass
        return skill
    def history(self):
        skill = 0
        for prof in self.prof:
            if prof == 'history':
                skill += self.profBonus() + self.intModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.intModifier()
        else:
            pass
        return skill
    def insight(self):
        skill = 0
        for prof in self.prof:
            if prof == 'insight':
                skill += self.profBonus() + self.wisModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.wisModifier()
        else:
            pass
        return skill
    def intimidation(self):
        skill = 0
        for prof in self.prof:
            if prof == 'intimidation':
                skill += self.profBonus() + self.chaModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.chaModifier()
        else:
            pass
        return skill
    def investigation(self):
        skill = 0
        for prof in self.prof:
            if prof == 'investigation':
                skill += self.profBonus() + self.intModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.intModifier()
        else:
            pass
        return skill
    def medicine(self):
        skill = 0
        for prof in self.prof:
            if prof == 'medicine':
                skill += self.profBonus() + self.wisModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.wisModifier()
        else:
            pass
        return skill
    def nature(self):
        skill = 0
        for prof in self.prof:
            if prof == 'nature':
                skill += self.profBonus() + self.intModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.intModifier()
        else:
            pass
        return skill
    def perception(self):
        skill = 0
        for prof in self.prof:
            if prof == 'perception':
                skill += self.profBonus() + self.wisModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.wisModifier()
        else:
            pass
        return skill
    def performance(self):
        skill = 0
        for prof in self.prof:
            if prof == 'performance':
                skill += self.profBonus() + self.chaModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.chaModifier()
        else:
            pass
        return skill
    def persuasion(self):
        skill = 0
        for prof in self.prof:
            if prof == 'persuasion':
                skill += self.profBonus() + self.chaModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.chaModifier()
        else:
            pass
        return skill
    def religion(self):
        skill = 0
        for prof in self.prof:
            if prof == 'religion':
                skill += self.profBonus() + self.intModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.intModifier()
        else:
            pass
        return skill
    def sleightOfHand(self):
        skill = 0
        for prof in self.prof:
            if prof == 'sleight of hand':
                skill += self.profBonus() + self.dexModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.dexModifier()
        else:
            pass
        return skill
    def stealth(self):
        skill = 0
        for prof in self.prof:
            if prof == 'stealth':
                skill += self.profBonus() + self.dexModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.dexModifier()
        else:
            pass
        return skill
    def survival(self):
        skill = 0
        for prof in self.prof:
            if prof == 'survival':
                skill += self.profBonus() + self.wisModifier()
                break
            else:
                pass
        if skill == 0:
            skill += self.wisModifier()
        else:
            pass
        return skill
    def allSkills(self):
        return f"{self.name}'s ability checks:\n--------------------\nacrobatics: {self.acrobatics()}\nanimal handling: {self.animalHandling()}\narcana: {self.arcana()}\nathletics: {self.athletics()}\ndeception: {self.deception()}\nhistory: {self.history()}\ninsight: {self.insight()}\nintimidation: {self.intimidation()}\ninvestigation: {self.investigation()}\nmedicin: {self.medicine()}\nnature: {self.nature()}\nperception: {self.perception()}\nperformance: {self.performance()}\npersuasion: {self.persuasion()}\nreligion: {self.religion()}\nsleight of hand: {self.sleightOfHand()}\nstealth: {self.stealth()}\nsurvival: {self.survival()}\n"
    def strSave(self):
        saves = self.savingProf()
        saveMod = 0
        for save in saves:
            if save == 'strength':
                saveMod += self.profBonus() + self.strModifier()
                break
            else:
                pass
        if saveMod == 0:
            saveMod += self.strModifier()
        else:
            pass
        return saveMod
    def dexSave(self):
        saves = self.savingProf()
        saveMod = 0
        for save in saves:
            if save == 'dexterity':
                saveMod += self.profBonus() + self.dexModifier()
                break
            else:
                pass
        if saveMod == 0:
            saveMod += self.dexModifier()
        else:
            pass
        return saveMod
    def conSave(self):
        saves = self.savingProf()
        saveMod = 0
        for save in saves:
            if save == 'constitution':
                saveMod += self.profBonus() + self.conModifier()
                break
            else:
                pass
        if saveMod == 0:
            saveMod += self.conModifier()
        else:
            pass
        return saveMod
    def intSave(self):
        saves = self.savingProf()
        saveMod = 0
        for save in saves:
            if save == 'intelegence':
                saveMod += self.profBonus() + self.intModifier()
                break
            else:
                pass
        if saveMod == 0:
            saveMod += self.intModifier()
        else:
            pass
        return saveMod
    def wisSave(self):
        saves = self.savingProf()
        saveMod = 0
        for save in saves:
            if save == 'wisdom':
                saveMod += self.profBonus() + self.wisModifier()
                break
            else:
                pass
        if saveMod == 0:
            saveMod += self.wisModifier()
        else:
            pass
        return saveMod
    def chaSave(self):
        saves = self.savingProf()
        saveMod = 0
        for save in saves:
            if save == 'charisma':
                saveMod += self.profBonus() + self.chaModifier()
                break
            else:
                pass
        if saveMod == 0:
            saveMod += self.chaModifier()
        else:
            pass
        return saveMod
    def allSaves(self):
        return f"{self.name}'s ability checks:\n--------------------\nstrenght: {self.strSave()}\ndexterity: {self.dexSave()}\nconstitution: {self.conSave()}\nintelegence: {self.intSave()}\nwisdom: {self.wisSave()}\ncharisma: {self.chaSave()}\n"


    def functions(self):
        return f"Here's a list of all the functions (they are case sensitive) you can call and what they will return\n---------------------------\nsavingProf() = saving throws you have proficiency in\nstrModifier() = your strength modifier\ndexModifier() = your dexterity modifier\nconModifier() = your constitution modifier\nintModifier() = your intelegence modifier\nwisModifier() = your wisdom modifier\nchaModifier() = your charisma modifier\nAC() = your armor class\ngetClass() = your classes and how many levels you have in each\nproficiencyBonus() = your current proficiency bonus\nacrobatics() = your modifier for acrobatics\nanimalHandling() = your modifier for animal handling\narcana() = your modifier for arcana\nathletics() = your modifier for athletics\ndeception() = your modifier for deception\nhistory() = your modifier for history\ninsight() = your modifier for insight\nintimidation() = your modifier for intimidation\ninvestigation() = your modifier for investigation\nmedicine() = your modifier for medicine\nnature() = your modifier for nature\nperception() = your modifier for perception\nperformance() = your modifier for performance\npersuasion() = your modifier for persuasion\nreligion() = your modifier for religion\nsleightOfHand() = your modifier for sleight of hand\nstealth() = your modifier for stealth\nsurvival() = your modifier for survival\nallSkills() = your modifier for all skill checks\nstrSave() = your modifier for strength saving throws\ndexSave() = your modifier for dexterity saving throws\nconSave() = your modifier for constitution saving throws\nintSave() = your modifier for intelegence saving throws\nwisSave() = your modifier for wisdom saving throws\nchaSave() = your modifier for charisma saving throws\nallSaves() = your modifier for all your saving throws"

if __name__ == "__main__":
    main()
