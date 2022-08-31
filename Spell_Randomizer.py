from random import choice
def Cantrips(Num=1): # Num = number of spells to pick
    cantrip = [] # empty list to add selected spells
    list = ["Acid Splash","Blade Ward","Booming Blade","Chill Touch","Control Flames","Create Bonfire","Dancing Lights","Decompose","Druidcraft","Eldritch Blast","Encode Thoughts","Fire Bolt","Friends","Frostbite","Green-Flame Blade","Guidance","Gust","Hand of Radiance","Infestation","Light","Lightning Lure","Mage Hand","Magic Stone","Mending","Message","Mind Sliver","Minor Illusion","Mold Earth","Poison Spray","Prestidigitation","Primal Savagery","Produce Flame","Ray of Frost","Resistance","Sacred Flame","Sapping Sting","Shape Water","Shillelagh","Shocking Grasp","Spare the Dying","Sword Burst","Thaumaturgy","Thron Whip","Thunderclap","Toll the Dead","True Strike","Vicious Mockery","Word of Radiance"]
    for i in range(Num):
        cantrip.append(choice(list))
    print(cantrip)


if __name__ == "__main__":
    Cantrips(5)