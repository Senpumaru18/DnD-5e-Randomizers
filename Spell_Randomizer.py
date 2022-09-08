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
    list = ["Aganazzar's Scorcher","Aid","Alter Self","Animal Messenger","Arcane Lock","Augury","Barkskin","Beast Sense","Blindness/Deafness","Blur","Borrowed Knowledge","Branding Smite","Calm Emotions","Cloud of Daggers","Continual Flame","Cordon of Arrows","Darkness","Darkvision","Detect Thoughts","Dragon's Breath","Dust Devil","Earthbind","Enhance Ability","Enlarge/Reduce","Enthrall","Find Steed","Find Traps","Flame Blade","Flaming Sphere","Flock of Familiars","Fortune's Favor","Gentle Repose","Gift of Gab","Gust of Wind","Healing Spirit","Heat Metal","Hold Person","Immovable Object","Invisibility","Jim's Glowing Coin","Kinetic Jaunt","Knock","Lesser Restoration","Levitate","Locate Animals or Plants","Locate Object","Magic Mouth","Magic Weapon","Maximillian's Earthen Grasp","Melf's Acid Arrow","Mind Spike","Mirror Image","Misty Step","Moonbeam","Nathair's Mischief","Nystul's Magic Aura","Pass Without Trace","Phantasmal Force","Prayer of Healing","Protection from Poison","Pyrotechnics","Ray of Enfeeblement","Rime's Binding Ice","Rope Trick","Scorching Ray","See Invisibility","Shadow Blade","Shatter","Silence","Skywrite","Snilloc's Snowball Storm","Spder Climb","Spike Growth","Spiritual Weapon","Suggestion","Summon Beast","Tasha's Mind Whip","Vortext Warp","Warding Bond","Warding Wind","Web","Wither and Bloom","Wristpocket","Zone of Truth"]
    for i in range(Num):
        second.append(choice(list))
    print(second)
def Third_Level(Num=1): # Num = number of spells to pick
    third = [] # empty list to add selected spells to
    list = ["Animate Dead","Ashardalon's Stride","Aura of Vitality","Beacon of Hope","Bestow Curse","Binding Smite","Blink","Call Lightning","Catnap","Clairvoyance","Conjure Animals","Conjure Barrage","Conjure Lesser Demon","Counterspell","Create Food and Water","Crusader's Mantle","Daylight","Dispel Magic","Elemental Weapon","Enemies Abound","Erupting Earth","Fast Friends","Fear","Feign Death","Fireball","Flame Arrows","Fly","Galder's Tower","Gaseous Form","Glyph of Warding","Haste","Hunger of Hadar","Hypnotic Pattern","Incite Greed","Intellect Fortress","Leomund's Tiny Hut","Life Transference","Lightning Arrow","Lightning Bolt","Magic Circle","Major Image","Mass Healing Word","Meld into Stone","Melf's Minute Meteors","Motivational Speech","Nondetection","Phantom Steed","Plant Growth","Protection from Energy","Pulse Wave","Remove Curse","Revivify","Sending","Sleet Storm","Slow","Speak with Dead","Speak with Plants","Spirit Guardians","Spirit Shroud","Stinking Cloud","Summon Fey","Summon Lesser Deoms","Summon Shadowspawn","Summon Undead","Thunder Step","Tidal Wave","Tiny Servant","Tongues","Vampiric Touch","Wall of Sand","Wall of Water","Water Breathing","Water Walk","Wind Wall"]
    for i in range(Num):
        third.append(choice(list))
    print(third)
def Fourth_Level(Num=1): # Num = number of spells to pick
    fourth = [] # empty list to add selected spells to
    list = ["Arcane Eye","Aura of Life","Aura of Puritiy","Banishment","Blight","Charm Monster","Compulsion","Confusion","Conjure Minor Elementals","Conjure Woodland Beings","Control Water","Death Ward","Dimension Door","Divination","Dominate Beast","Elemental Bane","Evard's Black Tentacles","Fabricate","Find Greater Steed","Fire Shield","Freedom of Movement","Galder's Speedy Courier","Giant Insect","Grasping Vine","Gravity Sinkhole","Greater Invisibility","Guardian of Faith","Guardian of Nature","Hallucinatory Terrain","Ice Storm","Leomund's Secret Chest","Locate Creature","Mordenkainen's Faithful Hound","Mordenkainen's Private Sanctum","Otiluke's Resilient Sphere","Phanasmal Killer","Polymorph","Raulothim's Pyschic Lance","Shadow of Moil","Sickening Radiance","Staggering Smite","Stone Shape","Stoneskin","Storm Sphere","Summon Aberration","Summon Construct","Summon Elemental","Summon Greater Demon","Bitriolic Sphere","Wall fo Fire","Watery Sphere"]
    for i in range(Num):
        fourth.append(choice(list))
    print(fourth)
def Fifth_Level(Num=1): # Num = number of spells to pick
    fifth = [] # empty list to add selected spells to
    list = ["Animate Objects","Antilife Shell","Awaken","Banishing Smite","Bigby's Hand","Circle of Power","Cloudkill","Commune","Commune with Nature","Cone of Cold","Conjure Elemental","Conjure Volley","Contact Other Plane","Contagion","Control Winds","Creation","Danse Macabre","Dawn","Destructive Wave","Dispel Evil and Good","Dominate Person","Dream","Enervation","Far Step","Flame Strike","Geas","Greater Restoration","Hallow","Hold Monster","Holy Weapon","Immolation","Infernal Calling","Insect Plague","Legend Lore","Maelstrom","Mass Cure Wounds","Mislead","Modify Memory","Negative Energy Flood","Passwall","Planar Binding","Raise Dead","Rary's Telepathic Bond","Reincarnate","Scrying","Seeming","Skill Empowerment","Steel Wind Strike","Summon Celestial","Summon Draconic Spirit","Swift Quiver","Synaptic Static","Telekinesis","Teleportation Circle","Temporal Shunt","Transmute Rock","Tree Stride","Wall of Force","Wall of Light","Wall of Stone","Wrath of Nature"]
    for i in range(Num):
        fifth.append(choice(list))
    print(fifth)
def Sixth_Level(Num=1): # Num = number of spells to pick
    sixth = [] # empty list to add selected spells to
    list = ["Arcane Gate","Blade Barrier","Bones of the Earth","Chain Lightning","Circle of Death","Conjure Fey","Contingency","Create Homunculus","Create Undead","Disintegrate","Drawmij's Instant Summons","Druid Grove","Eyebite","Find the Path","Fizban's Platinum Shield","Flesh to Stone","Forbiddance","Globe of Invulnerability","Gravity Fissure","Guards and Wards","Harm","Heal","Heroes' Feast","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Magic Jar","Mass Suggestion","Mental Prision","Move Earth","Otiluke's Freezing Sphere","Otto's Irresistible Dance","Planar Ally","Primordial Ward","Programmed Illusion","Scatter","Soul Cage","Summon Fiend","Sunbeam","Tasha's Otherworldly Guise","Tenser's Transformation","Transport via Plants","True Seeing","Wall of Ice","Wall of Thorns","Wind Walk","Word of Recall"]
    for i in range(Num):
        sixth.append(choice(list))
    print(sixth)
def Seventh_Level(Num=1): # Num = number of spells to pick
    seventh = [] # empty list to add selected spells to
    list = ["Conjure Celestial","Create Magen","Crown of Stars","Delayed Blast Fireball","Divine Word","Draconic Transformation","Dream of the Blue Veil","Etherealness","Finger of Death","Fire Storm","Forcecage","Mirage Arcane","Mordenkainen's Magnificent Mansion","Mordenkainen's Sword","Plane Shift","Power Word: Pain","Prismatic Spray","Project Image","Regenerate","Resurrection","Reverse Gravity","Sequester","Simulacrum","Symbol","Teleport","Temple of the Gods","Tether Essence","Whirlwind"]
    for i in range(Num):
        seventh.append(choice(list))
    print(seventh)
def Eighth_Level(Num=1): # Num = number of spells to pick
    eighth = [] # empty list to add selected spells to
    list = []
    for i in range(Num):
        eighth.append(choice(list))
    print(eighth)
def Ninth_Level(Num=1): # Num = number of spells to pick
    ninth = [] # empty list to add selected spells to
    list = []
    for i in range(Num):
        ninth.append(choice(list))
    print(ninth)
def All_Spells(Num=1): # Num = number of spells to pick
    all = [] # empty list to add selected spells to
    list = []
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