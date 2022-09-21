def main():
    Arwyn = PlayerStats(15,20,16,10,18,12,'Changling',['Druid', 'Rogue'], [3,3],30)
    
    Arwyn.getClass()

class PlayerStats:
    def __init__(self, strength, dexterity, constitution, intellegence, wisdom, charisma, race, _class, classLvl, speed):
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

    def STR_modifier(self):
        if self.str == 1:
            return "-5"
        elif self.str <= 3:
            return "-4"
        elif self.str <= 5:
            return "-3"
        elif self.str <= 7:
            return "-2"
        elif self.str <= 9:
            return "-1"
        elif self.str <= 11:
            return "0"
        elif self.str <= 13:
            return "+1"
        elif self.str <= 15:
            return "+2"
        elif self.str <= 17:
            return "+3"
        elif self.str <= 19:
            return "+4"
        elif self.str <= 21:
            return "+5"
        elif self.str <= 23:
            return "+6"
        elif self.str <= 25:
            return "+7"
        elif self.str <= 27:
            return "+8"
        elif self.str <= 29:
            return "+9"
        elif self.str == 30:
            return "+10"
        else:
            return "That number is not valid, must be within 1-30"
    def DEX_modifier(self):
        if self.dex == 1:
            return "-5"
        elif self.dex <= 3:
            return "-4"
        elif self.dex <= 5:
            return "-3"
        elif self.dex <= 7:
            return "-2"
        elif self.dex <= 9:
            return "-1"
        elif self.dex <= 11:
            return "0"
        elif self.dex <= 13:
            return "+1"
        elif self.dex <= 15:
            return "+2"
        elif self.dex <= 17:
            return "+3"
        elif self.dex <= 19:
            return "+4"
        elif self.dex <= 21:
            return "+5"
        elif self.dex <= 23:
            return "+6"
        elif self.dex <= 25:
            return "+7"
        elif self.dex <= 27:
            return "+8"
        elif self.dex <= 29:
            return "+9"
        elif self.dex == 30:
            return "+10"
        else:
            return "That number is not valid, must be within 1-30"
    def CON_modifier(self):
        if self.con == 1:
            return "-5"
        elif self.con <= 3:
            return "-4"
        elif self.con <= 5:
            return "-3"
        elif self.con <= 7:
            return "-2"
        elif self.con <= 9:
            return "-1"
        elif self.con <= 11:
            return "0"
        elif self.con <= 13:
            return "+1"
        elif self.con <= 15:
            return "+2"
        elif self.con <= 17:
            return "+3"
        elif self.con <= 19:
            return "+4"
        elif self.con <= 21:
            return "+5"
        elif self.con <= 23:
            return "+6"
        elif self.con <= 25:
            return "+7"
        elif self.con <= 27:
            return "+8"
        elif self.con <= 29:
            return "+9"
        elif self.con == 30:
            return "+10"
        else:
            return "That number is not valid, must be within 1-30"
    def INT_modifier(self):
        if self.int == 1:
            return "-5"
        elif self.int <= 3:
            return "-4"
        elif self.int <= 5:
            return "-3"
        elif self.int <= 7:
            return "-2"
        elif self.int <= 9:
            return "-1"
        elif self.int <= 11:
            return "0"
        elif self.int <= 13:
            return "+1"
        elif self.int <= 15:
            return "+2"
        elif self.int <= 17:
            return "+3"
        elif self.int <= 19:
            return "+4"
        elif self.int <= 21:
            return "+5"
        elif self.int <= 23:
            return "+6"
        elif self.int <= 25:
            return "+7"
        elif self.int <= 27:
            return "+8"
        elif self.int <= 29:
            return "+9"
        elif self.int == 30:
            return "+10"
        else:
            return "That number is not valid, must be within 1-30"
    def WIS_modifier(self):
        if self.wis == 1:
            return "-5"
        elif self.wis <= 3:
            return "-4"
        elif self.wis <= 5:
            return "-3"
        elif self.wis <= 7:
            return "-2"
        elif self.wis <= 9:
            return "-1"
        elif self.wis <= 11:
            return "0"
        elif self.wis <= 13:
            return "+1"
        elif self.wis <= 15:
            return "+2"
        elif self.wis <= 17:
            return "+3"
        elif self.wis <= 19:
            return "+4"
        elif self.wis <= 21:
            return "+5"
        elif self.wis <= 23:
            return "+6"
        elif self.wis <= 25:
            return "+7"
        elif self.wis <= 27:
            return "+8"
        elif self.wis <= 29:
            return "+9"
        elif self.wis == 30:
            return "+10"
        else:
            return "That number is not valid, must be within 1-30"
    def CHA_modifier(self):
        if self.cha == 1:
            return "-5"
        elif self.cha <= 3:
            return "-4"
        elif self.cha <= 5:
            return "-3"
        elif self.cha <= 7:
            return "-2"
        elif self.cha <= 9:
            return "-1"
        elif self.cha <= 11:
            return "0"
        elif self.cha <= 13:
            return "+1"
        elif self.cha <= 15:
            return "+2"
        elif self.cha <= 17:
            return "+3"
        elif self.cha <= 19:
            return "+4"
        elif self.cha <= 21:
            return "+5"
        elif self.cha <= 23:
            return "+6"
        elif self.cha <= 25:
            return "+7"
        elif self.cha <= 27:
            return "+8"
        elif self.cha <= 29:
            return "+9"
        elif self.cha == 30:
            return "+10"
        else:
            return "That number is not valid, must be within 1-30"
    def AC(self):
        return self.DEX_modifier
    def get_speed(self):
        return self.speed
    def getClass(self):
        for x in range(0, len(self._class)):
            print(f"lvl {self.level[x]} {self._class[x]}")




if __name__ == "__main__":
    main()
