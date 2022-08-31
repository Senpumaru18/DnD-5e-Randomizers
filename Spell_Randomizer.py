from random import choice
def Cantrips(Num=1): # Num = number of spells to pick
    cantrip = [] # empty list to add selected spells to
    list = ["Acid Splash","Blade Ward","Booming Blade","Chill Touch","Control Flames","Create Bonfire","Dancing Lights","Decompose","Druidcraft","Eldritch Blast","Encode Thoughts","Fire Bolt","Friends","Frostbite","Green-Flame Blade","Guidance","Gust","Hand of Radiance","Infestation","Light","Lightning Lure","Mage Hand","Magic Stone","Mending","Message","Mind Sliver","Minor Illusion","Mold Earth","Poison Spray","Prestidigitation","Primal Savagery","Produce Flame","Ray of Frost","Resistance","Sacred Flame","Sapping Sting","Shape Water","Shillelagh","Shocking Grasp","Spare the Dying","Sword Burst","Thaumaturgy","Thron Whip","Thunderclap","Toll the Dead","True Strike","Vicious Mockery","Word of Radiance"]
    for i in range(Num):
        cantrip.append(choice(list))
    print(cantrip)
def First_Level(Num=1): # Num = number of spells to pick
    first = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        first.append(choice(list))
    print(first)
def Second_Level(Num=1): # Num = number of spells to pick
    second = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        first.append(choice(list))
    print(first)
def Third_Level(Num=1): # Num = number of spells to pick
    third = [] # empty list to add selected spells to
    list = [""]
def Fourth_Level(Num=1): # Num = number of spells to pick
    fourth = [] # empty list to add selected spells to
    list = [""]
def Fifth_Level(Num=1): # Num = number of spells to pick
    fifth = [] # empty list to add selected spells to
    list = [""]
def Sixth_Level(Num=1): # Num = number of spells to pick
    sixth = [] # empty list to add selected spells to
    list = [""]
def Seventh_Level(Num=1): # Num = number of spells to pick
    seventh = [] # empty list to add selected spells to
    list = [""]
def Eighth_Level(Num=1): # Num = number of spells to pick
    eighth = [] # empty list to add selected spells to
    list = [""]
def Ninth_Level(Num=1): # Num = number of spells to pick
    ninth = [] # empty list to add selected spells to
    list = [""]
def All_Spells(Num=1): # Num = number of spells to pick
    all = [] # empty list to add selected spells to
    list = [""]

if __name__ == "__main__":
    Cantrips(5)
    First_Level()
    Second_Level()
    Third_Level()
    Fourth_Level()
    Fifth_Level()
    Sixth_Level()
    Seventh_Level()
    Eighth_Level()
    Ninth_Level()
    All_Spells()