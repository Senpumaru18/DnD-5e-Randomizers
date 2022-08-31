from random import choice
def Cantrips(Num=1): # Num = number of spells to pick
    cantrip = [] # empty list to add selected spells to
    list = ["Acid Splash","Blade Ward","Booming Blade","Chill Touch","Control Flames","Create Bonfire","Dancing Lights","Decompose","Druidcraft","Eldritch Blast","Encode Thoughts","Fire Bolt","Friends","Frostbite","Green-Flame Blade","Guidance","Gust","Hand of Radiance","Infestation","Light","Lightning Lure","Mage Hand","Magic Stone","Mending","Message","Mind Sliver","Minor Illusion","Mold Earth","Poison Spray","Prestidigitation","Primal Savagery","Produce Flame","Ray of Frost","Resistance","Sacred Flame","Sapping Sting","Shape Water","Shillelagh","Shocking Grasp","Spare the Dying","Sword Burst","Thaumaturgy","Thron Whip","Thunderclap","Toll the Dead","True Strike","Vicious Mockery","Word of Radiance"]
    for i in range(Num):
        cantrip.append(choice(list))
    print(cantrip)
def First_Level(Num=1): # Num = number of spells to pick
    first = [] # empty list to add selected spells to
    list = ["Absorb Elements","Acid Stream","Alarm","Animal Friendship","Armor of Agathys","Arms of Hadar","Bane","Beast Bond","Bless","Burning Hands","Catapult","Cause Fear","Ceremony","Chaos Bolt","Charm Person","Chromatic Orb","Color Spray","Command","Compelled Duel","Comprehend Languages","Create or Destroy Water","Cure Wounds","Detect Evil and Good","Detect Magic","Detect Poison and Disease","Disguise Self","Dissonant Whispers","Distort Value","Divine Favor","Earth Tremor","Ensnaring Strike","Entangle","Expeditious Retreat","Faerie Fire","False Life","Feather Fall","Find Familiar","Fog Cloud","Frost Fingers","Gift of Alacrity","Goodberry","Grease","Guiding Bolt","Hail of Thorns","Healing Word","Hellish Rebuke","Heroism","Hex","Hunter's Mark","Ice Knife","Identify","Illusory Script","Inflict Wounds","Jim's Magic Missile","Jump","Longstrider","Mage Armor","Magic Missile","Magnify Gravity","Protection from Evil and Good","Purify Food and Drink","Ray of Sickness","Sanctuary","Searing Smite","Shield","Shield of Faith","Silent Image","Silvery Barbs","Sleep","Snare","Speak with Animals","Tasha's Caustic Brew","Tasha's Hideous Laughter","Tenser's Floating Disk","Thunderous Smite","Thunderwave","Unseen Servant","Witch Bolt","Wrathful Smite","Zephyr Strike"]
    for i in range(Num):
        first.append(choice(list))
    print(first)
def Second_Level(Num=1): # Num = number of spells to pick
    second = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        second.append(choice(list))
    print(second)
def Third_Level(Num=1): # Num = number of spells to pick
    third = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        third.append(choice(list))
    print(third)
def Fourth_Level(Num=1): # Num = number of spells to pick
    fourth = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        fourth.append(choice(list))
    print(fourth)
def Fifth_Level(Num=1): # Num = number of spells to pick
    fifth = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        fifth.append(choice(list))
    print(fifth)
def Sixth_Level(Num=1): # Num = number of spells to pick
    sixth = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        sixth.append(choice(list))
    print(sixth)
def Seventh_Level(Num=1): # Num = number of spells to pick
    seventh = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        seventh.append(choice(list))
    print(seventh)
def Eighth_Level(Num=1): # Num = number of spells to pick
    eighth = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        eighth.append(choice(list))
    print(eighth)
def Ninth_Level(Num=1): # Num = number of spells to pick
    ninth = [] # empty list to add selected spells to
    list = [""]
    for i in range(Num):
        ninth.append(choice(list))
    print(ninth)
def All_Spells(Num=1): # Num = number of spells to pick
    all = [] # empty list to add selected spells to
    list = ["d","D"]
    for i in range(Num):
        all.append(choice(list))
    print(all)

if __name__ == "__main__":
    Cantrips()
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