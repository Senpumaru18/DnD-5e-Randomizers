from string import ascii_letters
from random import randint, choice, choices

# DICE ROLLS USED FOR THE GENERATORS (yes i understand i could have just used the 'XdX' dice roller for the whole thing.)
def Xd4(NumberOfRolls=1):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, 4)
    return result       #
def Xd6(NumberOfRolls=1):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, 6)
    return result
def Xd8(NumberOfRolls=1):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, 8)
    return result
def Xd10(NumberOfRolls=1):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, 10)
    return result
def Xd12(NumberOfRolls=1):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, 12)
    return result
def Xd20(NumberOfRolls=1):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, 20)
    return result
def Xd100(NumberOfRolls=1):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, 100)
    return result
def XdX(NumberOfRolls=1, NumberOfSides=2):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, NumberOfSides)
    return result

# GEMSTONES SORTED BY VALUE (from the tables in the Dungeon Master's Guide on pg. 134)
def Random_Gemstones_10GP(number_of_gems=1):            # Given a number select that many gems randomly
    result = []
    for i in range(number_of_gems):
        d12_roll = Xd12()
        if 1 <= d12_roll <= 1:
            result.append("Azurite, worth 10 GP")
        elif 2 <= d12_roll <= 2:
            result.append("Banded agate, worth 10 GP")
        elif 3 <= d12_roll <= 3:
            result.append("Blue quartz, worth 10 GP")
        elif 4 <= d12_roll <= 4:
            result.append("Eye agate, worth 10 GP")
        elif 5 <= d12_roll <= 5:
            result.append("Hematite, worth 10 GP")
        elif 6 <= d12_roll <= 6:
            result.append("Lapis lazuli, worth 10 GP")
        elif 7 <= d12_roll <= 7:
            result.append("Malachite, worth 10 GP")
        elif 8 <= d12_roll <= 8:
            result.append("Moss agate, worth 10 GP")
        elif 9 <= d12_roll <= 9:
            result.append("Obsidian, worth 10 GP")
        elif 10 <= d12_roll <= 10:
            result.append("Rhodochrosite, worth 10 GP")
        elif 11 <= d12_roll <= 11:
            result.append("Tiger eye, worth 10 GP")
        elif 12 <= d12_roll <= 12:
            result.append("Turquoise, worth 10 GP")
        else:
            result.append("Dice roll Exceeded 12")
    return result
def Random_Gemstones_50GP(number_of_gems=1):
    result = []
    for i in range(number_of_gems):
        d12_roll = Xd12()
        if 1 <= d12_roll <= 1:
            result.append("Bloodstone, worth 50 GP")
        elif 2 <= d12_roll <= 2:
            result.append("Carnelian, worth 50 GP")
        elif 3 <= d12_roll <= 3:
            result.append("Chalcedony, worth 50 GP")
        elif 4 <= d12_roll <= 4:
            result.append("Chrysoprase, worth 50 GP")
        elif 5 <= d12_roll <= 5:
            result.append("Citrine, worth 50 GP")
        elif 6 <= d12_roll <= 6:
            result.append("Jasper, worth 50 GP")
        elif 7 <= d12_roll <= 7:
            result.append("Moonstone, worth 50 GP")
        elif 8 <= d12_roll <= 8:
            result.append("Onyx, worth 50 GP")
        elif 9 <= d12_roll <= 9:
            result.append("Quartz, worth 50 GP")
        elif 10 <= d12_roll <= 10:
            result.append("Sardonyx, worth 50 GP")
        elif 11 <= d12_roll <= 11:
            result.append("Star rose quartz, worth 50 GP")
        elif 12 <= d12_roll <= 12:
            result.append("Zircon, worth 50 GP")
        else:
            result.append("Dice roll Exceeded 12")
    return result
def Random_Gemstones_100GP(number_of_gems=1):
    result = []
    for i in range(number_of_gems):
        d10_roll = Xd10()
        if 1 <= d10_roll <= 1:
            result.append("Amber, worth 100 GP")
        elif 2 <= d10_roll <= 2:
            result.append("Amethyst, worth 100 GP")
        elif 3 <= d10_roll <= 3:
            result.append("Chrysoberyl, worth 100 GP")
        elif 4 <= d10_roll <= 4:
            result.append("Coral, worth 100 GP")
        elif 5 <= d10_roll <= 5:
            result.append("Garnet, worth 100 GP")
        elif 6 <= d10_roll <= 6:
            result.append("Jade, worth 100 GP")
        elif 7 <= d10_roll <= 7:
            result.append("Jet, worth 100 GP")
        elif 8 <= d10_roll <= 8:
            result.append("Pearl, worth 100 GP")
        elif 9 <= d10_roll <= 9:
            result.append("Spinel, worth 100 GP")
        elif 10 <= d10_roll <= 10:
            result.append("Tourmaline, worth 100 GP")
        else:
            result.append("Dice roll Exceeded 10")
    return result
def Random_Gemstones_500GP(number_of_gems=1):
    result = []
    for i in range(number_of_gems):
        d6_roll = Xd6()
        if 1 <= d6_roll <= 1:
            result.append("Alexandrite, worth 500 GP")
        elif 2 <= d6_roll <= 2:
            result.append("Aquamarine, worth 500 GP")
        elif 3 <= d6_roll <= 3:
            result.append("Black pearl, worth 500 GP")
        elif 4 <= d6_roll <= 4:
            result.append("Blue spinel, worth 500 GP")
        elif 5 <= d6_roll <= 5:
            result.append("Peridot, worth 500 GP")
        elif 6 <= d6_roll <= 6:
            result.append("Topaz, worth 500 GP")
        else:
            result.append("Dice roll Exceeded 6")
    return result
def Random_Gemstones_1000GP(number_of_gems=1):
    result = []
    for i in range(number_of_gems):
        d8_roll = Xd8()
        if 1 <= d8_roll <= 1:
            result.append("Black opal, worth 1,000 GP")
        elif 2 <= d8_roll <= 2:
            result.append("Blue sapphire, worth 1,000 GP")
        elif 3 <= d8_roll <= 3:
            result.append("Emerald, worth 1,000 GP")
        elif 4 <= d8_roll <= 4:
            result.append("Fire opal, worth 1,000 GP")
        elif 5 <= d8_roll <= 5:
            result.append("Opal, worth 1,000 GP")
        elif 6 <= d8_roll <= 6:
            result.append("Star ruby, worth 1,000 GP")
        elif 7 <= d8_roll <= 7:
            result.append("Star sapphire, worth 1,000 GP")
        elif 8 <= d8_roll <= 8:
            result.append("Yellow sapphire, worth 1,000 GP")
        else:
            result.append("Dice roll Exceeded 8")
    return result
def Random_Gemstones_5000GP(number_of_gems=1):
    result = []
    for i in range(number_of_gems):
        d4_roll = Xd4()
        if 1 <= d4_roll <= 1:
            result.append("Black sapphire, worth 5,000 GP")
        elif 2 <= d4_roll <= 2:
            result.append("Diamond, worth 5,000 GP")
        elif 3 <= d4_roll <= 3:
            result.append("Jacinth, worth 5,000 GP")
        elif 4 <= d4_roll <= 4:
            result.append("Ruby, worth 5,000 GP")
        else:
            result.append("Dice roll Exceeded 4")
    return result

# ART OBJECTS SORTED BY VALUE (from the tables in the Dungeon Master's Guide on pg. 134-135)
def Random_Art_Objects_25GP(number_of_art_objects=1):
    result = []
    for i in range(number_of_art_objects):
        d10_roll = Xd10()
        if 1 <= d10_roll <= 1:
            result.append("Silver ewer, worth 25 GP")
        elif 2 <= d10_roll <= 2:
            result.append("Carved bone statuette, worth 25 GP")
        elif 3 <= d10_roll <= 3:
            result.append("Small gold bracelet, worth 25 GP")
        elif 4 <= d10_roll <= 4:
            result.append("Cloth-of-gold vestments, worth 25 GP")
        elif 5 <= d10_roll <= 5:
            result.append("Black velvet mask stitched with silver thread, worth 25 GP")
        elif 6 <= d10_roll <= 6:
            result.append("Copper chalice with silver filgree, worth 25 GP")
        elif 7 <= d10_roll <= 7:
            result.append("Pair of engraved bone dice, worth 25 GP")
        elif 8 <= d10_roll <= 8:
            result.append("Small mirror set in a painted wooden frame, worth 25 GP")
        elif 9 <= d10_roll <= 9:
            result.append("Emroidered silk handkerchief, worth 25 GP")
        elif 10 <= d10_roll <= 10:
            result.append("Gold locket with a painted portrait inside, worth 25 GP")
        else:
            result.append("Dice roll Exceeded 10")
    return result
def Random_Art_Objects_250GP(number_of_art_objects=1):
    result = []
    for i in range(number_of_art_objects):
        d10_roll = Xd10()
        if 1 <= d10_roll <= 1:
            result.append("Gold ring set with bloodstones, worth 250 GP")
        elif 2 <= d10_roll <= 2:
            result.append("Carved ivory statuette, worth 250 GP")
        elif 3 <= d10_roll <= 3:
            result.append("Large gold bracelet, worth 250 GP")
        elif 4 <= d10_roll <= 4:
            result.append("Silver necklace with a gemstone pendant, worth 250 GP")
        elif 5 <= d10_roll <= 5:
            result.append("Bronze crown, worth 250 GP")
        elif 6 <= d10_roll <= 6:
            result.append("Silk robe with gold embroidery, worth 250 GP")
        elif 7 <= d10_roll <= 7:
            result.append("Large will-made tapestry, worth 250 GP")
        elif 8 <= d10_roll <= 8:
            result.append("Brass mug with jade inlay, worth 250 GP")
        elif 9 <= d10_roll <= 9:
            result.append("Box of turquoise animal figurines, worth 250 GP")
        elif 10 <= d10_roll <= 10:
            result.append("Gold bird cage with electrum filigree, worth 250 GP")
        else:
            result.append("Dice roll Exceeded 10")
    return result
def Random_Art_Objects_750GP(number_of_art_objects=1):
    result = []
    for i in range(number_of_art_objects):
        d10_roll = Xd10()
        if 1 <= d10_roll <= 1:
            result.append("Silver chalice set moonstones, worth 750 GP")
        elif 2 <= d10_roll <= 2:
            result.append("Silver-plated steel longsword with jet set in hilt, worth 750 GP")
        elif 3 <= d10_roll <= 3:
            result.append("Small gold idol, worth 750 GP")
        elif 4 <= d10_roll <= 4:
            result.append("Carved harp of exotic wood with ivory inlay and zircon gems, worth 750 GP")
        elif 5 <= d10_roll <= 5:
            result.append("Gold dragon comb set with garnets as eyes, worth 750 GP")
        elif 6 <= d10_roll <= 6:
            result.append("Bottle stopper cork embosssed with gold leaf and set with amethysts, worth 750 GP")
        elif 7 <= d10_roll <= 7:
            result.append("Ceremonial electrum dagger with a black pearl in the pommel, worth 750 GP")
        elif 8 <= d10_roll <= 8:
            result.append("Silver and gold brooch, worth 750 GP")
        elif 9 <= d10_roll <= 9:
            result.append("Obsidian statuette with gold fittings and inlay, worth 750 GP")
        elif 10 <= d10_roll <= 10:
            result.append("Painted gold war mask, worth 750 GP")
        else:
            result.append("Dice roll Exceeded 10")
    return result
def Random_Art_Objects_2500GP(number_of_art_objects=1):
    result = []
    for i in range(number_of_art_objects):
        d10_roll = Xd10()
        if 1 <= d10_roll <= 1:
            result.append("Fine gold chain set with a fire opal, worth 2,500 GP")
        elif 2 <= d10_roll <= 2:
            result.append("Old masterpiece painting, worth 2,500 GP")
        elif 3 <= d10_roll <= 3:
            result.append("Embroidered silk and velvet mantle set with numerous moonstones, worth 2,500 GP")
        elif 4 <= d10_roll <= 4:
            result.append("Jeweled anklet, worth 2,500 GP")
        elif 5 <= d10_roll <= 5:
            result.append("Platinum bracelet set with a sapphire, worth 2,500 GP")
        elif 6 <= d10_roll <= 6:
            result.append("Embroidered glove set with jewel chips, worth 2,500 GP")
        elif 7 <= d10_roll <= 7:
            result.append("Gold music box, worth 2,500 GP")
        elif 8 <= d10_roll <= 8:
            result.append("Gold circlet set with four aquamarines, worth 2,500 GP")
        elif 9 <= d10_roll <= 9:
            result.append("Eye patch with a mock eye set in blue sapphire and moonstone, worth 2,500 GP")
        elif 10 <= d10_roll <= 10:
            result.append("A necklace string of small pink pearls, worth 2,500 GP""Tourmaline, worth 100 GP")
        else:
            result.append("Dice roll Exceeded 10")
    return result
def Random_Art_Objects_7500GP(number_of_art_objects=1):
    result = []
    for i in range(number_of_art_objects):
        d8_roll = Xd8()
        if 1 <= d8_roll <= 1:
            result.append("Jeweled gold crown, worth 7,500 GP")
        elif 2 <= d8_roll <= 2:
            result.append("Jeweled platinum ring, worth 7,500 GP")
        elif 3 <= d8_roll <= 3:
            result.append("Small gold statuette set with rubies, worth 7,500 GP")
        elif 4 <= d8_roll <= 4:
            result.append("Gold cup set with emeralds, worth 7,500 GP")
        elif 5 <= d8_roll <= 5:
            result.append("Gold jewelry box with platinum filigree, worth 7,500 GP")
        elif 6 <= d8_roll <= 6:
            result.append("Painted gold child's sarcophagus, worth 7,500 GP")
        elif 7 <= d8_roll <= 7:
            result.append("Jade game board with solid gold playing pieces, worth 7,500 GP")
        elif 8 <= d8_roll <= 8:
            result.append("Bejeweled ivory drinking horn with gold filigree, worth 7,500 GP")
        else:
            result.append("Dice roll Exceeded 8")
    return result

# EXTRAS GENERATORS 
def Random_Weapon(number_of_weapons=1):   # These are from the table in the Player's Handbook on pg. 149
    result = []
    weapons = ["Club","Dagger","Greatlub","Handaxe","Javelin","Light Hammer","Mace","Quarterstaff","Sickle","Spear","Dart","Shortbow","Sling","Battleaxe","Flail","Glaive","Greataxe","Greatsword","Halberd","Lance","Longsword","Maul","Morningstar","Pike","Rapier","Scimitar","Shortsword","Trident","War pick","Warhammer","Whip","Whip","Blowgun","Hand crossbow","Heavy crossbow","Longbow","Net"]
    modifier = ["","+1","+2","+3"]
    for i in range(number_of_weapons):
        result.append(choice(weapons)+" "+choice(modifier))
    return result
def Random_Magic_Armor(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d12_roll = Xd12()
        if d12_roll <= 2:
            result.append("+2 half plate")
        elif 3 <= d12_roll <= 4:
            result.append("+2 plate")
        elif 5 <= d12_roll <= 6:
            result.append("+3 studded leather")
        elif 7 <= d12_roll <= 8:
            result.append("+3 breastplate")
        elif 9 <= d12_roll <= 10:
            result.append("+3 splint")
        elif 11 <= d12_roll <= 11:
            result.append("+3 half plate")
        elif 12 <= d12_roll <= 12:
            result.append("+3 plate")
        else:
            result.append("Dice roll exceeded 12")
    return result
def Figurine_of_Wondrous_power(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d8_roll = Xd8()
        if 1 <= d8_roll <= 1:
            result.append("Bronze griffon")
        elif 2 <= d8_roll <= 2:
            result.append("Ebony fly")
        elif 3 <= d8_roll <= 3:
            result.append("Golden lions")
        elif 4 <= d8_roll <= 4:
            result.append("Ivory goats")
        elif 5 <= d8_roll <= 5:
            result.append("Marble elephant")
        elif 6 <= d8_roll <= 7:
            result.append("Onyx dog")
        elif 8 <= d8_roll <= 8:
            result.append("Serpentine owl")
        else:
            result.append("Dice roll exceeded 8")
    return result

# SPELL SCROLLS
def Cantrip_Spell_Scroll(Number_of_Items=1):
    result = []
    Spell_List = ["Acid Splash","Blade Ward","Booming Blade","Chill Touch","Control Flames","Create Bonfire","Dancing Lights","Decompose","Druidcraft","Eldritch Blast","Encode Thoughts","Fire Bolt","Friends","Frostbite","Green-Flame Blade","Guidance","Gust","Hand of Radiance","Infestation","Light","Lightning Lure","Mage Hand","Magic Stone","Mending","Message","Mind Sliver","Minor Illusion","Mold Earth","Poison Spray","Prestidigitation","Primal Savagery","Produce Flame","Ray of Frost","Resistance","Sacred Flame","Sapping Sting","Shape Water","Shillelagh","Shocking Grasp","Spare the Dying","Sword Burst","Thaumaturgy","Thron Whip","Thunderclap","Toll the Dead","True Strike","Vicious Mockery","Word of Radiance"]
    for i in range(Number_of_Items):
        result.append(choice(Spell_List))
    return result
def Level_1_Spell_Scroll(Number_of_Itmes=1):
    result = []
    Spell_List = ["Absorb Elements","Acid Stream","Alarm","Animal Friendship","Armor of Agathys","Arms of Hadar","Bane","Beast Bond","Bless","Burning Hands","Catapult","Cause Fear","Ceremony","Chaos Bolt","Charm Person","Chromatic Orb","Color Spray","Command","Compelled Duel","Comprehend Languages","Create or Destroy Water","Cure Wounds","Detect Evil and Good","Detect Magic","Detect Poison and Disease","Disguise Self","Dissonant Whispers","Distort Value","Divine Favor","Earth Tremor","Ensnaring Strike","Entangle","Expeditious Retreat","Faerie Fire","False Life","Feather Fall","Find Familiar","Fog Cloud","Frost Fingers","Gift of Alacrity","Goodberry","Grease","Guiding Bolt","Hail of Thorns","Healing Word","Hellish Rebuke","Heroism","Hex","Hunter's Mark","Ice Knife","Identify","Illusory Script","Inflict Wounds","Jim's Magic Missile","Jump","Longstrider","Mage Armor","Magic Missile","Magnify Gravity","Protection from Evil and Good","Purify Food and Drink","Ray of Sickness","Sanctuary","Searing Smite","Shield","Shield of Faith","Silent Image","Silvery Barbs","Sleep","Snare","Speak with Animals","Tasha's Caustic Brew","Tasha's Hideous Laughter","Tenser's Floating Disk","Thunderous Smite","Thunderwave","Unseen Servant","Witch Bolt","Wrathful Smite","Zephyr Strike"]
    for i in range(Number_of_Itmes):
        result.append(choice(Spell_List))
    return result
def Level_2_Spell_Scroll(Number_of_Items=1):
    result = []
    Spell_List = ["Aganazzar's Scorcher","Aid","Alter Self","Animal Messenger","Arcane Lock","Augury","Barkskin","Beast Sense","Blindness/Deafness","Blur","Borrowed Knowledge","Branding Smite","Calm Emotions","Cloud of Daggers","Continual Flame","Cordon of Arrows","Darkness","Darkvision","Detect Thoughts","Dragon's Breath","Dust Devil","Earthbind","Enhance Ability","Enlarge/Reduce","Enthrall","Find Steed","Find Traps","Flame Blade","Flaming Sphere","Flock of Familiars","Fortune's Favor","Gentle Repose","Gift of Gab","Gust of Wind","Healing Spirit","Heat Metal","Hold Person","Immovable Object","Invisibility","Jim's Glowing Coin","Kinetic Jaunt","Knock","Lesser Restoration","Levitate","Locate Animals or Plants","Locate Object","Magic Mouth","Magic Weapon","Maximillian's Earthen Grasp","Melf's Acid Arrow","Mind Spike","Mirror Image","Misty Step","Moonbeam","Nathair's Mischief","Nystul's Magic Aura","Pass Without Trace","Phantasmal Force","Prayer of Healing","Protection from Poison","Pyrotechnics","Ray of Enfeeblement","Rime's Binding Ice","Rope Trick","Scorching Ray","See Invisibility","Shadow Blade","Shatter","Silence","Skywrite","Snilloc's Snowball Storm","Spder Climb","Spike Growth","Spiritual Weapon","Suggestion","Summon Beast","Tasha's Mind Whip","Vortext Warp","Warding Bond","Warding Wind","Web","Wither and Bloom","Wristpocket","Zone of Truth"]
    for i in range(Number_of_Items):
        result.append(choice(Spell_List))
    return result
def Level_3_Spell_Scroll(Number_of_Items=1):
    result = []
    Spell_List = ["Animate Dead","Ashardalon's Stride","Aura of Vitality","Beacon of Hope","Bestow Curse","Binding Smite","Blink","Call Lightning","Catnap","Clairvoyance","Conjure Animals","Conjure Barrage","Conjure Lesser Demon","Counterspell","Create Food and Water","Crusader's Mantle","Daylight","Dispel Magic","Elemental Weapon","Enemies Abound","Erupting Earth","Fast Friends","Fear","Feign Death","Fireball","Flame Arrows","Fly","Galder's Tower","Gaseous Form","Glyph of Warding","Haste","Hunger of Hadar","Hypnotic Pattern","Incite Greed","Intellect Fortress","Leomund's Tiny Hut","Life Transference","Lightning Arrow","Lightning Bolt","Magic Circle","Major Image","Mass Healing Word","Meld into Stone","Melf's Minute Meteors","Motivational Speech","Nondetection","Phantom Steed","Plant Growth","Protection from Energy","Pulse Wave","Remove Curse","Revivify","Sending","Sleet Storm","Slow","Speak with Dead","Speak with Plants","Spirit Guardians","Spirit Shroud","Stinking Cloud","Summon Fey","Summon Lesser Deoms","Summon Shadowspawn","Summon Undead","Thunder Step","Tidal Wave","Tiny Servant","Tongues","Vampiric Touch","Wall of Sand","Wall of Water","Water Breathing","Water Walk","Wind Wall"]
    for i in range(Number_of_Items):
        result.append(choice(Spell_List))
    return result
def Level_4_Spell_Scroll(Number_of_Items=1):
    result = []
    Spell_List = ["Arcane Eye","Aura of Life","Aura of Puritiy","Banishment","Blight","Charm Monster","Compulsion","Confusion","Conjure Minor Elementals","Conjure Woodland Beings","Control Water","Death Ward","Dimension Door","Divination","Dominate Beast","Elemental Bane","Evard's Black Tentacles","Fabricate","Find Greater Steed","Fire Shield","Freedom of Movement","Galder's Speedy Courier","Giant Insect","Grasping Vine","Gravity Sinkhole","Greater Invisibility","Guardian of Faith","Guardian of Nature","Hallucinatory Terrain","Ice Storm","Leomund's Secret Chest","Locate Creature","Mordenkainen's Faithful Hound","Mordenkainen's Private Sanctum","Otiluke's Resilient Sphere","Phanasmal Killer","Polymorph","Raulothim's Pyschic Lance","Shadow of Moil","Sickening Radiance","Staggering Smite","Stone Shape","Stoneskin","Storm Sphere","Summon Aberration","Summon Construct","Summon Elemental","Summon Greater Demon","Bitriolic Sphere","Wall fo Fire","Watery Sphere"]
    for i in range(Number_of_Items):
        result.append(choice(Spell_List))
    return result
def Level_5_Spell_Scroll(Number_of_Items=1):
    result = []
    Spell_List = ["Animate Objects","Antilife Shell","Awaken","Banishing Smite","Bigby's Hand","Circle of Power","Cloudkill","Commune","Commune with Nature","Cone of Cold","Conjure Elemental","Conjure Volley","Contact Other Plane","Contagion","Control Winds","Creation","Danse Macabre","Dawn","Destructive Wave","Dispel Evil and Good","Dominate Person","Dream","Enervation","Far Step","Flame Strike","Geas","Greater Restoration","Hallow","Hold Monster","Holy Weapon","Immolation","Infernal Calling","Insect Plague","Legend Lore","Maelstrom","Mass Cure Wounds","Mislead","Modify Memory","Negative Energy Flood","Passwall","Planar Binding","Raise Dead","Rary's Telepathic Bond","Reincarnate","Scrying","Seeming","Skill Empowerment","Steel Wind Strike","Summon Celestial","Summon Draconic Spirit","Swift Quiver","Synaptic Static","Telekinesis","Teleportation Circle","Temporal Shunt","Transmute Rock","Tree Stride","Wall of Force","Wall of Light","Wall of Stone","Wrath of Nature"]
    for i in range(Number_of_Items):
        result.append(choice(Spell_List))
    return result
def Level_6_Spell_Scroll(Number_of_Items=1):
    result = []
    Spell_List = ["Arcane Gate","Blade Barrier","Bones of the Earth","Chain Lightning","Circle of Death","Conjure Fey","Contingency","Create Homunculus","Create Undead","Disintegrate","Drawmij's Instant Summons","Druid Grove","Eyebite","Find the Path","Fizban's Platinum Shield","Flesh to Stone","Forbiddance","Globe of Invulnerability","Gravity Fissure","Guards and Wards","Harm","Heal","Heroes' Feast","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Magic Jar","Mass Suggestion","Mental Prision","Move Earth","Otiluke's Freezing Sphere","Otto's Irresistible Dance","Planar Ally","Primordial Ward","Programmed Illusion","Scatter","Soul Cage","Summon Fiend","Sunbeam","Tasha's Otherworldly Guise","Tenser's Transformation","Transport via Plants","True Seeing","Wall of Ice","Wall of Thorns","Wind Walk","Word of Recall"]
    for i in range(Number_of_Items):
        result.append(choice(Spell_List))
    return result
def Level_7_Spell_Scroll(Number_of_Items=1):
    result = []
    Spell_List = ["Conjure Celestial","Create Magen","Crown of Stars","Delayed Blast Fireball","Divine Word","Draconic Transformation","Dream of the Blue Veil","Etherealness","Finger of Death","Fire Storm","Forcecage","Mirage Arcane","Mordenkainen's Magnificent Mansion","Mordenkainen's Sword","Plane Shift","Power Word: Pain","Prismatic Spray","Project Image","Regenerate","Resurrection","Reverse Gravity","Sequester","Simulacrum","Symbol","Teleport","Temple of the Gods","Tether Essence","Whirlwind"]
    for i in range(Number_of_Items):
        result.append(choice(Spell_List))
    return result
def Level_8_Spell_Scroll(Number_of_Items=1):
    result = []
    Spell_List = ["Abi-Daizim's Horrid Wilting","Animal Shapes","Antimagic Field","Antipathy/Sympathy","Clone","Control Weather","Dark Star","Demiplane","Dominate Monster","Earthquake","Feeblemind","Glibness","Holy aura","illusory Dragon","Incendiary Cloud","Maddening Darkness","Maze","Mighty Fortress","Mind Blank","Power Word: Stun","Reality Break","Sunburst","Telepathy","Tsunami"]
    for i in range(Number_of_Items):
        result.append(choice(Spell_List))
    return result
def Level_9_Spell_Scroll(Number_of_Items=1):
    result = []
    Spell_List = ["Astral Projection", "Foresight", "Gate", "Imprisonment", "Mass Heal", "Meteor Swarm", "Power Word Heal","Power Word Kill", "Prismatic Wall", "Shapechange", "Storm of Vengance", "Time Stop", "True Polymorph","True Resurrection", "Weird", "Wish"]
    for i in range(Number_of_Items):
        result.append(choice(Spell_List))
    return result

# Idividual TREASURE Tables from the Dungeon Master's Guide on pg. 136
def Indv_Treasure_CR_0_to_4(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 30:
            result.append(str(Xd6(5)) + " CP")
        elif 31 <= d100_roll <= 60:
            result.append(str(Xd6(4)) + " SP")
        elif 61 <= d100_roll <= 70:
            result.append(str(Xd6(3)) + " EP")
        elif 71 <= d100_roll <= 95:
            result.append(str(Xd6(3)) + " GP")
        elif 96 <= d100_roll <= 100:
            result.append(str(Xd6(1)) + " PP")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Indv_Treasure_CR_5_to_10(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 30:
            result.append(str((Xd6(4)) * 100) + " CP")
            result.append(str(Xd6(1) * 10) + " EP")
        elif 31 <= d100_roll <= 60:
            result.append(str((Xd6(6)) * 10) + " SP")
            result.append(str((Xd6(2)) * 10) + " GP")
        elif 61 <= d100_roll <= 70:
            result.append(str((Xd6(3)) * 10) + " EP")
            result.append(str((Xd6(2)) * 10) + " GP")
        elif 71 <= d100_roll <= 95:
            result.append(str((Xd6(4)) * 10) + " GP")
        elif 96 <= d100_roll <= 100:
            result.append(str((Xd6(2)) * 10) + " GP")
            result.append(str(Xd6(3)) + " PP")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Indv_Treasure_CR_11_to_16(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 20:
            result.append(str((Xd6(4)) * 100) + " SP")
            result.append(str(Xd6(1) * 100))
        elif 21 <= d100_roll <= 35:
            result.append(str(Xd6(1) * 100) + " EP")
            result.append(str(Xd6(1) * 100) + " GP")
        elif 36 <= d100_roll <= 75:
            result.append(str(Xd6(2) * 100) + " GP")
            result.append(str(Xd6(1) * 10) + " PP")
        elif 76 <= d100_roll <= 100:
            result.append(str(Xd6(2) * 100) + " GP")
            result.append(str(Xd6(2) * 10) + " PP")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Indv_Treasure_CR_17_Up(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 15:
            result.append(str(Xd6(2) * 1000) + " EP")
            result.append(str(Xd6(8) * 100) + " GP")
        elif 16 <= d100_roll <= 55:
            result.append(str(Xd6(1) * 1000) + " GP")
            result.append(str(Xd6(1) * 100) + " PP")
        elif 56 <= d100_roll <= 100:
            result.append(str(Xd6(1) * 1000) + " GP")
            result.append(str(Xd6(2) * 100) + " PP")
        else:
            result.append("Dice roll exceeded 100")
    return result

# MAGIC ITEM TABLES from the Dungeon Master's Guide on pg. 144-149
def Magic_Item_Table_A(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 50:
            result.append("Potion of healing")
        elif 51 <= d100_roll <= 60:
            result.append("Cantrip Spell Scroll " + str(Cantrip_Spell_Scroll()))
        elif 61 <= d100_roll <= 70:
            result.append("Potion of climbing")
        elif 71 <= d100_roll <= 90:
            result.append("1st level Spell scroll " + str(Level_1_Spell_Scroll()))
        elif 91 <= d100_roll <= 94:
            result.append("2nd level Spell scroll " + str(Level_2_Spell_Scroll()))
        elif 95 <= d100_roll <= 98:
            result.append("Potion of greater healing")
        elif 99 <= d100_roll <= 99:
            result.append("Bag of holding")
        elif 100 <= d100_roll <= 100:
            result.append("Driftglobe")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Magic_Item_Table_B(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 15:
            result.append("Potion of greater healing")
        elif 16 <= d100_roll <= 22:
            result.append("Potion of fire breath")
        elif 23 <= d100_roll <= 29:
            result.append("Potion of resistance")
        elif 30 <= d100_roll <= 34:
            result.append("Ammunition, +1")
        elif 35 <= d100_roll <= 39:
            result.append("Potion of animal friendship")
        elif 40 <= d100_roll <= 44:
            result.append("Potion of hill giant strength")
        elif 45 <= d100_roll <= 49:
            result.append("Potion of growth")
        elif 50 <= d100_roll <= 54:
            result.append("Potion of water breathing")
        elif 55 <= d100_roll <= 59:
            result.append("2nd level Spell scroll " + str(Level_2_Spell_Scroll()))
        elif 60 <= d100_roll <= 64:
            result.append("3rd level Spell scroll " + str(Level_3_Spell_Scroll()))
        elif 65 <= d100_roll <= 67:
            result.append("Bag of holding")
        elif 68 <= d100_roll <= 70:
            result.append("Keoghtom's ointment")
        elif 71 <= d100_roll <= 73:
            result.append("Oil of slipperiness")
        elif 74 <= d100_roll <= 75:
            result.append("Dust of disappearance")
        elif 76 <= d100_roll <= 77:
            result.append("Dust of dryness")
        elif 78 <= d100_roll <= 79:
            result.append("Dust of sneezing and choking")
        elif 80 <= d100_roll <= 81:
            result.append("Elemental gem")
        elif 82 <= d100_roll <= 83:
            result.append("Philter of love")
        elif 84 <= d100_roll <= 84:
            result.append("Alchemy jug")
        elif 85 <= d100_roll <= 85:
            result.append("Cap of water breathing")
        elif 86 <= d100_roll <= 86:
            result.append("Cloak of the manta ray")
        elif 87 <= d100_roll <= 87:
            result.append("Driftglobe")
        elif 88 <= d100_roll <= 88:
            result.append("Goggles of night")
        elif 89 <= d100_roll <= 89:
            result.append("Helm of comprehending languages")
        elif 90 <= d100_roll <= 90:
            result.append("Immovable rod")
        elif 91 <= d100_roll <= 91:
            result.append("Lantern of revealing")
        elif 92 <= d100_roll <= 92:
            result.append("Mariner's armor")
        elif 93 <= d100_roll <= 93:
            result.append("Mithral armor")
        elif 94 <= d100_roll <= 94:
            result.append("Potion of poison")
        elif 95 <= d100_roll <= 95:
            result.append("Ring of swimming")
        elif 96 <= d100_roll <= 96:
            result.append("Robe of useful items")
        elif 97 <= d100_roll <= 97:
            result.append("Rope of climbing")
        elif 98 <= d100_roll <= 98:
            result.append("Saddle of the cavalier")
        elif 99 <= d100_roll <= 99:
            result.append("Wand of magic detection")
        elif 100 <= d100_roll <= 100:
            result.append("Wand of secrets")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Magic_Item_Table_C(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 15:
            result.append("Potion of superior healing")
        elif 16 <= d100_roll <= 22:
            result.append("4th level Spell scroll " + str(Level_4_Spell_Scroll()))
        elif 23 <= d100_roll <= 27:
            result.append("Ammunition, +2")
        elif 28 <= d100_roll <= 32:
            result.append("Potion of clairvoyance")
        elif 33 <= d100_roll <= 37:
            result.append("Potion of diminution")
        elif 38 <= d100_roll <= 42:
            result.append("Potion of gaseous form")
        elif 43 <= d100_roll <= 47:
            result.append("Potion of frost giant strength")
        elif 48 <= d100_roll <= 52:
            result.append("Potion of stone giant strength")
        elif 53 <= d100_roll <= 57:
            result.append("Potion of heroism")
        elif 58 <= d100_roll <= 62:
            result.append("Potion of invulnerability")
        elif 63 <= d100_roll <= 67:
            result.append("Potion of mind reading")
        elif 68 <= d100_roll <= 72:
            result.append("5th level Spell scroll " + str(Level_5_Spell_Scroll()))
        elif 73 <= d100_roll <= 75:
            result.append("Elixir of health")
        elif 76 <= d100_roll <= 78:
            result.append("Oil of etherealness")
        elif 79 <= d100_roll <= 81:
            result.append("Potion of fire giant strength")
        elif 82 <= d100_roll <= 84:
            result.append("Quaal's feather token")
        elif 85 <= d100_roll <= 87:
            result.append("Scroll of protection")
        elif 88 <= d100_roll <= 89:
            result.append("Bag of beans")
        elif 90 <= d100_roll <= 91:
            result.append("Bead of force")
        elif 92 <= d100_roll <= 92:
            result.append("Chime of opening")
        elif 93 <= d100_roll <= 93:
            result.append("Decanter of endless water")
        elif 94 <= d100_roll <= 94:
            result.append("Eyes of minute seeing")
        elif 95 <= d100_roll <= 95:
            result.append("Folding boat")
        elif 96 <= d100_roll <= 96:
            result.append("Heward's handy haversack")
        elif 97 <= d100_roll <= 97:
            result.append("Horseshoes of speed")
        elif 98 <= d100_roll <= 98:
            result.append("Necklace of firebalss")
        elif 99 <= d100_roll <= 99:
            result.append("Periapt of health")
        elif 100 <= d100_roll <= 100:
            result.append("Sending stones")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Magic_Item_Table_D(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 20:
            result.append("Potion of supreme healing")
        elif 21 <= d100_roll <= 30:
            result.append("Potion of invisibility")
        elif 31 <= d100_roll <= 40:
            result.append("Potion of speed")
        elif 41 <= d100_roll <= 50:
            result.append("6th level Spell scroll " + str(Level_6_Spell_Scroll()))
        elif 51 <= d100_roll <= 57:
            result.append("7th level Spell scroll " + str(Level_7_Spell_Scroll()))
        elif 58 <= d100_roll <= 62:
            result.append("Ammunition, +3")
        elif 63 <= d100_roll <= 67:
            result.append("Oil of sharpness")
        elif 68 <= d100_roll <= 72:
            result.append("Potion of flying")
        elif 73 <= d100_roll <= 77:
            result.append("Potion of cloud giant strength")
        elif 78 <= d100_roll <= 82:
            result.append("Potion of longevity")
        elif 83 <= d100_roll <= 87:
            result.append("Potion of vitality")
        elif 88 <= d100_roll <= 92:
            result.append("8th level Spell scroll " + str(Level_8_Spell_Scroll()))
        elif 93 <= d100_roll <= 95:
            result.append("Horseshoes of a zephyr")
        elif 96 <= d100_roll <= 98:
            result.append("Nolzur's marvelous pigments")
        elif 99 <= d100_roll <= 99:
            result.append("Bag of devouring")
        elif 100 <= d100_roll <= 100:
            result.append("Portable hole")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Magic_Item_Table_E(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 30:
            result.append("8th level Spell scroll " + str(Level_8_Spell_Scroll()))
        elif 31 <= d100_roll <= 55:
            result.append("Potion of storm giant strength")
        elif 56 <= d100_roll <= 70:
            result.append("Potion of supreme healing")
        elif 71 <= d100_roll <= 85:
            result.append("9th level Spell scroll " + str(Level_9_Spell_Scroll()))
        elif 86 <= d100_roll <= 93:
            result.append("Universal solvent")
        elif 94 <= d100_roll <= 98:
            result.append("Arrow of slaying")
        elif 99 <= d100_roll <= 100:
            result.append("Sovereign glue")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Magic_Item_Table_F(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 15:
            result.append(str(Random_Weapon()) + ", +1")
        elif 16 <= d100_roll <= 18:
            result.append("Sheild, +1")
        elif 19 <= d100_roll <= 21:
            result.append("Sentinel shield")
        elif 22 <= d100_roll <= 23:
            result.append("Amulet of proof against detection and location")
        elif 24 <= d100_roll <= 25:
            result.append("Boots of elvenkind")
        elif 26 <= d100_roll <= 27:
            result.append("Boots of striding and springing")
        elif 28 <= d100_roll <= 29:
            result.append("Bracers of archery")
        elif 30 <= d100_roll <= 31:
            result.append("Brooch of shielding")
        elif 32 <= d100_roll <= 33:
            result.append("Broom of flying")
        elif 34 <= d100_roll <= 35:
            result.append("Cloak of elvenkind")
        elif 36 <= d100_roll <= 37:
            result.append("Cloak of protection")
        elif 38 <= d100_roll <= 39:
            result.append("Gauntlets of ogre power")
        elif 40 <= d100_roll <= 41:
            result.append("Hat of disguise")
        elif 42 <= d100_roll <= 43:
            result.append("Javelin of lightning")
        elif 44 <= d100_roll <= 45:
            result.append("Pearl of power")
        elif 46 <= d100_roll <= 47:
            result.append("Rod of the pact keeper, +1")
        elif 48 <= d100_roll <= 49:
            result.append("Slippers of spider climbing")
        elif 50 <= d100_roll <= 51:
            result.append("Staff of the adder")
        elif 52 <= d100_roll <= 53:
            result.append("Staff of the pyton")
        elif 54 <= d100_roll <= 55:
            result.append("Sword of vengeance")
        elif 56 <= d100_roll <= 57:
            result.append("Trident of fish command")
        elif 58 <= d100_roll <= 59:
            result.append("Wand of magic missiles")
        elif 60 <= d100_roll <= 61:
            result.append("Wand of the war mage, +1")
        elif 62 <= d100_roll <= 63:
            result.append("Wand of web")
        elif 64 <= d100_roll <= 65:
            result.append("Weapon of warning")
        elif 66 <= d100_roll <= 66:
            result.append("Adamantine armor (chain mail)")
        elif 67 <= d100_roll <= 67:
            result.append("Adamantine armor (chain shirt)")
        elif 68 <= d100_roll <= 68:
            result.append("Adamantine armor (scale mail)")
        elif 69 <= d100_roll <= 69:
            result.append("Bag of tricks (grey)")
        elif 70 <= d100_roll <= 70:
            result.append("Bag of tricks (rust)")
        elif 71 <= d100_roll <= 71:
            result.append("Bag of tricks (tan)")
        elif 72 <= d100_roll <= 72:
            result.append("Boots of the winterlands")
        elif 73 <= d100_roll <= 73:
            result.append("Circlet of blasting")
        elif 74 <= d100_roll <= 74:
            result.append("Deck of illusions")
        elif 75 <= d100_roll <= 75:
            result.append("Eversmoking bottle")
        elif 76 <= d100_roll <= 76:
            result.append("Eyes of charming")
        elif 77 <= d100_roll <= 77:
            result.append("Eyes of the eagle")
        elif 78 <= d100_roll <= 78:
            result.append("Figurine of wondrous power (silver raven)")
        elif 79 <= d100_roll <= 79:
            result.append("Gem of brightness")
        elif 80 <= d100_roll <= 80:
            result.append("Gloves of missile snaring")
        elif 81 <= d100_roll <= 81:
            result.append("Gloves of swimming and climbing")
        elif 82 <= d100_roll <= 82:
            result.append("Gloves of thievery")
        elif 83 <= d100_roll <= 83:
            result.append("Headband of intellect")
        elif 84 <= d100_roll <= 84:
            result.append("Helm of telepathy")
        elif 85 <= d100_roll <= 85:
            result.append("Instrument of the bards (Doss lute)")
        elif 86 <= d100_roll <= 86:
            result.append("Instrument of the bards (Fochlucan bandore)")
        elif 87 <= d100_roll <= 87:
            result.append("Instrument of the bards (Mac-Fuimidh cittern)")
        elif 88 <= d100_roll <= 88:
            result.append("Medallion of thoughts")
        elif 89 <= d100_roll <= 89:
            result.append("Necklace of adaptation")
        elif 90 <= d100_roll <= 90:
            result.append("Periapt of wound closure")
        elif 91 <= d100_roll <= 91:
            result.append("Pipes of haunting")
        elif 92 <= d100_roll <= 92:
            result.append("Pipes of the sewers")
        elif 93 <= d100_roll <= 93:
            result.append("Ring of jumping")
        elif 94 <= d100_roll <= 94:
            result.append("Ring of mind shielding")
        elif 95 <= d100_roll <= 95:
            result.append("Ring of warmth")
        elif 96 <= d100_roll <= 96:
            result.append("Ring of water walking")
        elif 97 <= d100_roll <= 97:
            result.append("Quiver Ehlonna")
        elif 98 <= d100_roll <= 98:
            result.append("Stone of good luck")
        elif 99 <= d100_roll <= 99:
            result.append("Wind fan")
        elif 100 <= d100_roll <= 100:
            result.append("Winged boots")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Magic_Item_Table_G(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 11:
            result.append(str(Random_Weapon()) + ", +2")
        elif 12 <= d100_roll <= 14:
            result.append(Figurine_of_Wondrous_power(Xd8()))
        elif 15 <= d100_roll <= 15:
            result.append("Adamantine armor (breastplate)")
        elif 16 <= d100_roll <= 16:
            result.append("Adamantine armor (splint)")
        elif 17 <= d100_roll <= 17:
            result.append("Amulet of health")
        elif 18 <= d100_roll <= 18:
            result.append("Armor of vulnerability")
        elif 19 <= d100_roll <= 19:
            result.append("Arrow-catching shield")
        elif 20 <= d100_roll <= 20:
            result.append("Belt of dwarvenkind")
        elif 21 <= d100_roll <= 21:
            result.append("Belt of hill giant strength")
        elif 22 <= d100_roll <= 22:
            result.append("Berserker axe")
        elif 23 <= d100_roll <= 23:
            result.append("Boots of levitation")
        elif 24 <= d100_roll <= 24:
            result.append("Boots of speed")
        elif 25 <= d100_roll <= 25:
            result.append("Bowl of commanding water elementals")
        elif 26 <= d100_roll <= 26:
            result.append("Bracers of defense")
        elif 27 <= d100_roll <= 27:
            result.append("Brazier of commanding fire elementals")
        elif 28 <= d100_roll <= 28:
            result.append("Cape of the mountebank")
        elif 29 <= d100_roll <= 29:
            result.append("Censer of controlling air elementals")
        elif 30 <= d100_roll <= 30:
            result.append("Armor, +1 chain mail")
        elif 31 <= d100_roll <= 31:
            result.append("Armor of resistance (chain mail)")
        elif 32 <= d100_roll <= 32:
            result.append("Armor, +1 chain shirt")
        elif 33 <= d100_roll <= 33:
            result.append("Armor of resistance (chain shirt)")
        elif 34 <= d100_roll <= 34:
            result.append("Cloak of displacement")
        elif 35 <= d100_roll <= 35:
            result.append("Cloak of the bat")
        elif 36 <= d100_roll <= 36:
            result.append("Cube of force")
        elif 37 <= d100_roll <= 37:
            result.append("Daern's instant fortress")
        elif 38 <= d100_roll <= 38:
            result.append("Dagger of venom")
        elif 39 <= d100_roll <= 39:
            result.append("Dimensional shackles")
        elif 40 <= d100_roll <= 40:
            result.append("Dragon slayer")
        elif 41 <= d100_roll <= 41:
            result.append("Elven chain")
        elif 42 <= d100_roll <= 42:
            result.append("Flame tongue")
        elif 43 <= d100_roll <= 43:
            result.append("Gem of seeing")
        elif 44 <= d100_roll <= 44:
            result.append("Giant slayer")
        elif 45 <= d100_roll <= 45:
            result.append("Glamoured studded leather")
        elif 46 <= d100_roll <= 46:
            result.append("Helm of teleportation")
        elif 47 <= d100_roll <= 47:
            result.append("Horn of blasting")
        elif 48 <= d100_roll <= 48:
            result.append("Horn of Valhalla (silver or brass)")
        elif 49 <= d100_roll <= 49:
            result.append("Instrument of the bards (Canaith mandolin)")
        elif 50 <= d100_roll <= 50:
            result.append("Instrument of the bards (Cli lyre)")
        elif 51 <= d100_roll <= 51:
            result.append("Ioun stone (awareness)")
        elif 52 <= d100_roll <= 52:
            result.append("Ioun stone (protection)")
        elif 53 <= d100_roll <= 53:
            result.append("Ioun stone (reserve)")
        elif 54 <= d100_roll <= 54:
            result.append("Ioun stone (sustenance)")
        elif 55 <= d100_roll <= 55:
            result.append("Iron bands of Bilarro")
        elif 56 <= d100_roll <= 56:
            result.append("Armor, +1 leather")
        elif 57 <= d100_roll <= 57:
            result.append("Armor of resistance (leather)")
        elif 58 <= d100_roll <= 58:
            result.append("Mace of distruption")
        elif 59 <= d100_roll <= 59:
            result.append("Mace of smiting")
        elif 60 <= d100_roll <= 60:
            result.append("Mace of terror")
        elif 61 <= d100_roll <= 61:
            result.append("Mantle of spell resistance")
        elif 62 <= d100_roll <= 62:
            result.append("Necklace of prayer beads")
        elif 63 <= d100_roll <= 63:
            result.append("Periapt of proof against poison")
        elif 64 <= d100_roll <= 64:
            result.append("Ring of animal influence")
        elif 65 <= d100_roll <= 65:
            result.append("Ring of evasion")
        elif 66 <= d100_roll <= 66:
            result.append("Ring of feather falling")
        elif 67 <= d100_roll <= 67:
            result.append("Ring of free action")
        elif 68 <= d100_roll <= 68:
            result.append("Ring of protection")
        elif 69 <= d100_roll <= 69:
            result.append("Ring of resistance")
        elif 70 <= d100_roll <= 70:
            result.append("Ring of spell storing")
        elif 71 <= d100_roll <= 71:
            result.append("Ring of the ram")
        elif 72 <= d100_roll <= 72:
            result.append("Ring of X-ray vision")
        elif 73 <= d100_roll <= 73:
            result.append("Robe of eyes")
        elif 74 <= d100_roll <= 74:
            result.append("Rod of rulership")
        elif 75 <= d100_roll <= 75:
            result.append("Rod of the pact keeper, +2")
        elif 76 <= d100_roll <= 76:
            result.append("Rope of entanglement")
        elif 77 <= d100_roll <= 77:
            result.append("Armor, +1 scale mail")
        elif 78 <= d100_roll <= 78:
            result.append("Armor of resistance (scale mail)")
        elif 79 <= d100_roll <= 79:
            result.append("Shield, +2")
        elif 80 <= d100_roll <= 80:
            result.append("Shield of missile attraction")
        elif 81 <= d100_roll <= 81:
            result.append("Staff of charming")
        elif 82 <= d100_roll <= 82:
            result.append("Staff of healing")
        elif 83 <= d100_roll <= 83:
            result.append("Staff of swarming insects")
        elif 84 <= d100_roll <= 84:
            result.append("Staff of woodlands")
        elif 85 <= d100_roll <= 85:
            result.append("Staff of withering")
        elif 86 <= d100_roll <= 86:
            result.append("Stone of controlling earth elementals")
        elif 87 <= d100_roll <= 87:
            result.append("Sun blade")
        elif 88 <= d100_roll <= 88:
            result.append("Sword of life stealing")
        elif 89 <= d100_roll <= 89:
            result.append("Sword of wounding")
        elif 90 <= d100_roll <= 90:
            result.append("Tentacle rod")
        elif 91 <= d100_roll <= 91:
            result.append("Vicious " + str(Random_Weapon()))
        elif 92 <= d100_roll <= 92:
            result.append("Wand of binding")
        elif 93 <= d100_roll <= 93:
            result.append("Wand of enemy detection")
        elif 94 <= d100_roll <= 94:
            result.append("Wand of fear")
        elif 95 <= d100_roll <= 95:
            result.append("Wand of fireballs")
        elif 96 <= d100_roll <= 96:
            result.append("Wand of lighting bolts")
        elif 97 <= d100_roll <= 97:
            result.append("Wand of Paralysis")
        elif 98 <= d100_roll <= 98:
            result.append("Wand of the war mage, +2")
        elif 99 <= d100_roll <= 99:
            result.append("Wand of wonder")
        elif 100 <= d100_roll <= 100:
            result.append("Wings of flying")
        else:
            result.append("Dice roll exceeded 100")
    return result
def Magic_Item_Table_H(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 10:
            result.append(str(Random_Weapon()) + ", +3")
        elif 11 <= d100_roll <= 12:
            result.append("Amulet of the planes")
        elif 13 <= d100_roll <= 14:
            result.append("Carpet of flying")
        elif 15 <= d100_roll <= 16:
            result.append("Crystal ball (very rare version)")
        elif 17 <= d100_roll <= 18:
            result.append("Ring of regeneration")
        elif 19 <= d100_roll <= 20:
            result.append("Ring of shooting stars")
        elif 21 <= d100_roll <= 22:
            result.append("Ring of telekinesis")
        elif 23 <= d100_roll <= 24:
            result.append("Robe of scintillating colors")
        elif 25 <= d100_roll <= 26:
            result.append("Robe of scintillating colors")
        elif 27 <= d100_roll <= 28:
            result.append("Rod of absorption")
        elif 29 <= d100_roll <= 30:
            result.append("Rod of alertness")
        elif 31 <= d100_roll <= 32:
            result.append("Rod of security")
        elif 33 <= d100_roll <= 34:
            result.append("Rod of the pact keeper, +3")
        elif 35 <= d100_roll <= 36:
            result.append("Scimitar of speed")
        elif 37 <= d100_roll <= 38:
            result.append("Shield, +3")
        elif 39 <= d100_roll <= 40:
            result.append("Staff of fire")
        elif 41 <= d100_roll <= 42:
            result.append("Staff of frost")
        elif 43 <= d100_roll <= 44:
            result.append("Staff of power")
        elif 45 <= d100_roll <= 46:
            result.append("Staff of striking")
        elif 47 <= d100_roll <= 48:
            result.append("Staff of thunder and lighting")
        elif 49 <= d100_roll <= 50:
            result.append("Sword of sharpness")
        elif 51 <= d100_roll <= 52:
            result.append("Wand of polymorph")
        elif 53 <= d100_roll <= 54:
            result.append("Wand of the war mage, +3")
        elif 55 <= d100_roll <= 55:
            result.append("Adamantine armor (Half plate)")
        elif 56 <= d100_roll <= 56:
            result.append("Adamantine armor (plate)")
        elif 57 <= d100_roll <= 57:
            result.append("Animated shield")
        elif 58 <= d100_roll <= 58:
            result.append("Belt of fire giant strength")
        elif 59 <= d100_roll <= 59:
            result.append(choices(["Belt of frost giant strength", "Belt of stone giant strength"]))
        elif 60 <= d100_roll <= 60:
            result.append("+1 breastplate")
        elif 61 <= d100_roll <= 61:
            result.append("Armor of resistance (breastplate)")
        elif 62 <= d100_roll <= 62:
            result.append("Candle of invocation")
        elif 63 <= d100_roll <= 63:
            result.append("+2 chain mail")
        elif 64 <= d100_roll <= 64:
            result.append("+2 chain shirt")
        elif 65 <= d100_roll <= 65:
            result.append("Cloak of arachnida")
        elif 66 <= d100_roll <= 66:
            result.append("Dancing sword")
        elif 67 <= d100_roll <= 67:
            result.append("Demon armor")
        elif 68 <= d100_roll <= 68:
            result.append("Dragon scale mail")
        elif 69 <= d100_roll <= 69:
            result.append("Dwarven plate")
        elif 70 <= d100_roll <= 70:
            result.append("Dwarven thrower")
        elif 71 <= d100_roll <= 71:
            result.append("Efreeti bottle")
        elif 72 <= d100_roll <= 72:
            result.append("Figurine of wondrous power (obsidian steed)")
        elif 73 <= d100_roll <= 73:
            result.append("Frost brand")
        elif 74 <= d100_roll <= 74:
            result.append("Helm of brilliance")
        elif 75 <= d100_roll <= 75:
            result.append("Horn of Valhalla (bronze)")
        elif 76 <= d100_roll <= 76:
            result.append("Instrument of the bards (Anstruth harp)")
        elif 77 <= d100_roll <= 77:
            result.append("Ioun stone (absorption)")
        elif 78 <= d100_roll <= 78:
            result.append("Ioun stone (agility)")
        elif 79 <= d100_roll <= 79:
            result.append("Ioun stone (fortitude)")
        elif 80 <= d100_roll <= 80:
            result.append("Ioun stone (insight)")
        elif 81 <= d100_roll <= 81:
            result.append("Ioun stone (intellect)")
        elif 82 <= d100_roll <= 82:
            result.append("Ioun stone (leadership)")
        elif 83 <= d100_roll <= 83:
            result.append("Ioun stone (strength)")
        elif 84 <= d100_roll <= 84:
            result.append("+2 leather")
        elif 85 <= d100_roll <= 85:
            result.append("Manual of bodily health")
        elif 86 <= d100_roll <= 86:
            result.append("Manual of gainful exercise")
        elif 87 <= d100_roll <= 87:
            result.append("Manual of golems")
        elif 88 <= d100_roll <= 88:
            result.append("Manual of quickness of action")
        elif 89 <= d100_roll <= 89:
            result.append("Mirror of life trapping")
        elif 90 <= d100_roll <= 90:
            result.append("Nine lives stealer")
        elif 91 <= d100_roll <= 91:
            result.append("Oathbow")
        elif 92 <= d100_roll <= 92:
            result.append("+2 scale mail")
        elif 93 <= d100_roll <= 93:
            result.append("Spellguard shield")
        elif 94 <= d100_roll <= 94:
            result.append("+1 splint")
        elif 95 <= d100_roll <= 95:
            result.append("Armor of resistance (splint)")
        elif 96 <= d100_roll <= 96:
            result.append("+1 studded leather")
        elif 97 <= d100_roll <= 97:
            result.append("Armor of resistance (studded leather)")
        elif 98 <= d100_roll <= 98:
            result.append("Tome of clear thought")
        elif 99 <= d100_roll <= 99:
            result.append("Tome of leadership and influence")
        elif 100 <= d100_roll <= 100:
            result.append("Tome of understanding")
        else:
            result.append("Dice roll exceeds 100")
    return result
def Magic_Item_Table_I(Number_of_Items=1):
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 5:
            result.append("Defender")
        elif 6 <= d100_roll <= 10:
            result.append("Hammer of thenderbolts")
        elif 11 <= d100_roll <= 15:
            result.append("Luck blade")
        elif 16 <= d100_roll <= 20:
            result.append("Sword of answering")
        elif 21 <= d100_roll <= 23:
            result.append("Holy avenger")
        elif 24 <= d100_roll <= 26:
            result.append("Ring of djinni summoning")
        elif 27 <= d100_roll <= 29:
            result.append("Ring of invisibility")
        elif 30 <= d100_roll <= 32:
            result.append("Ring of spell turning")
        elif 33 <= d100_roll <= 35:
            result.append("Rod of lordly might")
        elif 36 <= d100_roll <= 38:
            result.append("Staff of the magi")
        elif 39 <= d100_roll <= 41:
            result.append("Vorpal sword")
        elif 42 <= d100_roll <= 43:
            result.append("Belt of cloud giant strength")
        elif 44 <= d100_roll <= 45:
            result.append("+2 breastplate")
        elif 46 <= d100_roll <= 47:
            result.append("+3 chain mail")
        elif 48 <= d100_roll <= 49:
            result.append("+3 chain shirt")
        elif 50 <= d100_roll <= 51:
            result.append("Cloak of invisibility")
        elif 52 <= d100_roll <= 53:
            result.append("Crystal ball (legendary version)")
        elif 54 <= d100_roll <= 55:
            result.append("+1 half plate")
        elif 56 <= d100_roll <= 57:
            result.append("iron flask")
        elif 58 <= d100_roll <= 59:
            result.append("+3 leather")
        elif 60 <= d100_roll <= 61:
            result.append("+1 plate")
        elif 62 <= d100_roll <= 63:
            result.append("Robe of the archmagi")
        elif 64 <= d100_roll <= 65:
            result.append("Rod of resurrection")
        elif 66 <= d100_roll <= 67:
            result.append("+1 scale mail")
        elif 68 <= d100_roll <= 69:
            result.append("Scarab of protection")
        elif 70 <= d100_roll <= 71:
            result.append("+2 splint")
        elif 72 <= d100_roll <= 73:
            result.append("+2 studded leather")
        elif 74 <= d100_roll <= 75:
            result.append("Well of many worlds")
        elif 76 <= d100_roll <= 76:
            result.append(Random_Magic_Armor())
        elif 77 <= d100_roll <= 77:
            result.append("Apparatus of Kwalish")
        elif 78 <= d100_roll <= 78:
            result.append("Armor of invulnerability")
        elif 79 <= d100_roll <= 79:
            result.append("Belt of storm giant strength")
        elif 80 <= d100_roll <= 80:
            result.append("Cubic gate")
        elif 81 <= d100_roll <= 81:
            result.append("Deck of many things")
        elif 82 <= d100_roll <= 82:
            result.append("Efreeti chain")
        elif 83 <= d100_roll <= 83:
            result.append("Armor of resistance (half plate)")
        elif 84 <= d100_roll <= 84:
            result.append("Horn of Valhalla (iron)")
        elif 85 <= d100_roll <= 85:
            result.append("Instrument of the bards (ollamh harp)")
        elif 86 <= d100_roll <= 86:
            result.append("Ioun stone (greater absorption)")
        elif 87 <= d100_roll <= 87:
            result.append("Ioun stone (Mastery)")
        elif 88 <= d100_roll <= 88:
            result.append("Ioun stone (regeneration)")
        elif 89 <= d100_roll <= 89:
            result.append("Plate armor of etherealness")
        elif 90 <= d100_roll <= 90:
            result.append("Plate armor of resistance")
        elif 91 <= d100_roll <= 91:
            result.append("Ring of air elemental command")
        elif 92 <= d100_roll <= 92:
            result.append("Ring of earth elemental command")
        elif 93 <= d100_roll <= 93:
            result.append("Ring of fire elemental command")
        elif 94 <= d100_roll <= 94:
            result.append("Ring of three wishes")
        elif 95 <= d100_roll <= 95:
            result.append("Ring of water elemental command")
        elif 96 <= d100_roll <= 96:
            result.append("Sphere of annihilation")
        elif 97 <= d100_roll <= 97:
            result.append("Talisman of pure good")
        elif 98 <= d100_roll <= 98:
            result.append("Talisman of the sphere")
        elif 99 <= d100_roll <= 99:
            result.append("Talisman of ultimate evil")
        elif 100 <= d100_roll <= 100:
            result.append("Tome of the stilled tongue")
        else:
            result.append("Dice roll exceeds 100")
    return result

# TREASURE HOARD Tables from the Dungeon Master's Guide on pg. 137-139
def Treasure_Hoard_CR_0_t0_4(Number_of_Items=1):
    print((str(Xd6(6) * 100) + " CP,"), (str(Xd6(3) * 100) + " SP,"), (str(Xd6(2) * 10) + " GP"))
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 6:
            pass
        elif 7 <= d100_roll <= 16:
            result.append(Random_Gemstones_10GP(Xd6(2)))
        elif 17 <= d100_roll <= 26:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
        elif 27 <= d100_roll <= 36:
            result.append(Random_Gemstones_50GP(Xd6(2)))
        elif 37 <= d100_roll <= 44:
            result.append(Random_Gemstones_10GP(Xd6(2)))
            result.append(Magic_Item_Table_A(Xd6()))
        elif 45 <= d100_roll <= 52:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_A(Xd6()))
        elif 53 <= d100_roll <= 60:
            result.append(Random_Gemstones_50GP(Xd6(2)))
            result.append(Magic_Item_Table_A(Xd6()))
        elif 61 <= d100_roll <= 65:
            result.append(Random_Gemstones_10GP(Xd6(2)))
            result.append(Magic_Item_Table_B(Xd4()))
        elif 66 <= d100_roll <= 70:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_B(Xd4()))
        elif 71 <= d100_roll <= 75:
            result.append(Random_Gemstones_50GP(Xd6(2)))
            result.append(Magic_Item_Table_B(Xd4()))
        elif 76 <= d100_roll <= 78:
            result.append(Random_Gemstones_10GP(Xd6(2)))
            result.append(Magic_Item_Table_C(Xd4()))
        elif 79 <= d100_roll <= 80:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_C(Xd4()))
        elif 81 <= d100_roll <= 85:
            result.append(Random_Gemstones_50GP(Xd6(2)))
            result.append(Magic_Item_Table_C(Xd4()))
        elif 86 <= d100_roll <= 92:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_F(Xd4()))
        elif 93 <= d100_roll <= 97:
            result.append(Random_Gemstones_50GP(Xd6(2)))
            result.append(Magic_Item_Table_F(Xd4()))
        elif 98 <= d100_roll <= 99:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_G())
        elif 100 <= d100_roll <= 100:
            result.append(Random_Gemstones_50GP(Xd6()))
            result.append(Magic_Item_Table_G())
        else:
            result.append("Dice roll exceeds 100")
    return result
def Treasure_Hoard_CR_5_to_10(Number_of_Items=1):
    print((str(Xd6(2) * 100) + " CP,"), (str(Xd6(2) * 1000) + " SP,"), (str(Xd6(6) * 100) + " GP,"), (str(Xd6(3) * 10) + " PP"))
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if d100_roll <= 4:
            pass
        elif 5 <= d100_roll <= 10:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
        elif 11 <= d100_roll <= 16:
            result.append(Random_Gemstones_50GP(Xd6(3)))
        elif 17 <= d100_roll <= 22:
            result.append(Random_Gemstones_100GP(Xd6(3)))
        elif 23 <= d100_roll <= 28:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
        elif 29 <= d100_roll <= 32:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_A(Xd6()))
        elif 33 <= d100_roll <= 36:
            result.append(Random_Gemstones_50GP(Xd6(3)))
            result.append(Magic_Item_Table_A(Xd6()))
        elif 37 <= d100_roll <= 40:
            result.append(Random_Gemstones_100GP(Xd6(3)))
            result.append(Magic_Item_Table_A(Xd6()))
        elif 41 <= d100_roll <= 44:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_A(Xd6()))
        elif 45 <= d100_roll <= 49:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_B(Xd4()))
        elif 50 <= d100_roll <= 54:
            result.append(Random_Gemstones_50GP(Xd6(3)))
            result.append(Magic_Item_Table_B(Xd4()))
        elif 55 <= d100_roll <= 59:
            result.append(Random_Gemstones_100GP(Xd6(3)))
            result.append(Magic_Item_Table_B(Xd4()))
        elif 60 <= d100_roll <= 63:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_B(Xd4()))
        elif 64 <= d100_roll <= 66:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_C(Xd4()))
        elif 67 <= d100_roll <= 69:
            result.append(Random_Gemstones_50GP(Xd6(3)))
            result.append(Magic_Item_Table_C(Xd4()))
        elif 70 <= d100_roll <= 72:
            result.append(Random_Gemstones_100GP(Xd6(3)))
            result.append(Magic_Item_Table_C(Xd4()))
        elif 73 <= d100_roll <= 74:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_C(Xd4()))
        elif 75 <= d100_roll <= 76:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_D())
        elif 77 <= d100_roll <= 78:
            result.append(Random_Gemstones_50GP(Xd6(3)))
            result.append(Magic_Item_Table_D())
        elif 79 <= d100_roll <= 79:
            result.append(Random_Gemstones_100GP(Xd6(3)))
            result.append(Magic_Item_Table_D())
        elif 80 <= d100_roll <= 80:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_D())
        elif 81 <= d100_roll <= 84:
            result.append(Random_Art_Objects_25GP(Xd4(2)))
            result.append(Magic_Item_Table_F(Xd4()))
        elif 85 <= d100_roll <= 88:
            result.append(Random_Gemstones_50GP(Xd6(3)))
            result.append(Magic_Item_Table_F(Xd4()))
        elif 89 <= d100_roll <= 91:
            result.append(Random_Gemstones_100GP(Xd6(3)))
            result.append(Magic_Item_Table_F(Xd4()))
        elif 92 <= d100_roll <= 94:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_F(Xd4()))
        elif 95 <= d100_roll <= 96:
            result.append(Random_Gemstones_100GP(Xd6(3)))
            result.append(Magic_Item_Table_G(Xd4()))
        elif 97 <= d100_roll <= 98:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_G(Xd4()))
        elif 99 <= d100_roll <= 99:
            result.append(Random_Gemstones_100GP(Xd6(3)))
            result.append(Magic_Item_Table_H())
        elif 100 <= d100_roll <= 100:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_H())
        else:
            result.append("Dice roll exceeds 100")
    return result
def Treasure_Hoard_CR_11_to_16(Number_of_Items=1):
    print((str(Xd6(4) * 1000) + " GP,"), (str(Xd6(5) * 100) + " PP,"))
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if 1 <= d100_roll <= 3:
            pass
        elif 4 <= d100_roll <= 6:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
        elif 7 <= d100_roll <= 9:
            result.append(Random_Art_Objects_750GP(Xd4(2)))
        elif 10 <= d100_roll <= 12:
            result.append(Random_Gemstones_500GP(Xd6(3)))
        elif 13 <= d100_roll <= 15:
            result.append(Random_Gemstones_1000GP(Xd6(3)))
        elif 16 <= d100_roll <= 19:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_A(Xd4()))
            result.append(Magic_Item_Table_B(Xd6()))
        elif 20 <= d100_roll <= 23:
            result.append(Random_Art_Objects_750GP(Xd4(2)))
            result.append(Magic_Item_Table_A(Xd4()))
            result.append(Magic_Item_Table_B(Xd6()))
        elif 24 <= d100_roll <= 26:
            result.append(Random_Gemstones_500GP(Xd6(3)))
            result.append(Magic_Item_Table_A(Xd4()))
            result.append(Magic_Item_Table_B(Xd6()))
        elif 27 <= d100_roll <= 29:
            result.append(Random_Gemstones_1000GP(Xd6(3)))
            result.append(Magic_Item_Table_A(Xd4()))
            result.append(Magic_Item_Table_B(Xd6()))
        elif 30 <= d100_roll <= 35:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_C(Xd6()))
        elif 36 <= d100_roll <= 40:
            result.append(Random_Art_Objects_750GP(Xd4(2)))
            result.append(Magic_Item_Table_C(Xd6()))
        elif 41 <= d100_roll <= 45:
            result.append(Random_Gemstones_500GP(Xd6(2)))
            result.append(Magic_Item_Table_C(Xd6()))
        elif 46 <= d100_roll <= 50:
            result.append(Random_Gemstones_1000GP(Xd6(2)))
            result.append(Magic_Item_Table_C(Xd6()))
        elif 51 <= d100_roll <= 54:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_D(Xd4()))
        elif 55 <= d100_roll <= 58:
            result.append(Random_Art_Objects_750GP(Xd4(2)))
            result.append(Magic_Item_Table_D(Xd4()))
        elif 59 <= d100_roll <= 62:
            result.append(Random_Gemstones_500GP(Xd6(2)))
            result.append(Magic_Item_Table_D(Xd4()))
        elif 63 <= d100_roll <= 66:
            result.append(Random_Gemstones_1000GP(Xd6(2)))
            result.append(Magic_Item_Table_D(Xd4()))
        elif 67 <= d100_roll <= 68:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_E())
        elif 69 <= d100_roll <= 70:
            result.append(Random_Art_Objects_750GP(Xd4(2)))
            result.append(Magic_Item_Table_E())
        elif 71 <= d100_roll <= 72:
            result.append(Random_Gemstones_500GP(Xd6(2)))
            result.append(Magic_Item_Table_E())
        elif 73 <= d100_roll <= 74:
            result.append(Random_Gemstones_1000GP(Xd6(2)))
            result.append(Magic_Item_Table_E())
        elif 75 <= d100_roll <= 76:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_F())
            result.append(Magic_Item_Table_G(Xd4()))
        elif 77 <= d100_roll <= 78:
            result.append(Random_Art_Objects_750GP(Xd4(2)))
            result.append(Magic_Item_Table_F())
            result.append(Magic_Item_Table_G(Xd4()))
        elif 79 <= d100_roll <= 80:
            result.append(Random_Gemstones_500GP(Xd6(3)))
            result.append(Magic_Item_Table_F())
            result.append(Magic_Item_Table_G(Xd4()))
        elif 81 <= d100_roll <= 82:
            result.append(Random_Gemstones_1000GP(Xd6(3)))
            result.append(Magic_Item_Table_F())
            result.append(Magic_Item_Table_G(Xd4()))
        elif 83 <= d100_roll <= 85:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_H(Xd4()))
        elif 86 <= d100_roll <= 88:
            result.append(Random_Art_Objects_750GP(Xd4(2)))
            result.append(Magic_Item_Table_H(Xd4()))
        elif 89 <= d100_roll <= 90:
            result.append(Random_Gemstones_500GP(Xd6(2)))
            result.append(Magic_Item_Table_H(Xd4()))
        elif 91 <= d100_roll <= 92:
            result.append(Random_Gemstones_1000GP(Xd6(2)))
            result.append(Magic_Item_Table_H(Xd4()))
        elif 93 <= d100_roll <= 94:
            result.append(Random_Art_Objects_250GP(Xd4(2)))
            result.append(Magic_Item_Table_I())
        elif 95 <= d100_roll <= 96:
            result.append(Random_Art_Objects_750GP(Xd4(2)))
            result.append(Magic_Item_Table_I())
        elif 97 <= d100_roll <= 98:
            result.append(Random_Gemstones_500GP(Xd6(2)))
            result.append(Magic_Item_Table_I())
        elif 99 <= d100_roll <= 100:
            result.append(Random_Gemstones_1000GP(Xd6(2)))
            result.append(Magic_Item_Table_I())
        else:
            result.append("Dice roll exceeds 100")
    return result
def Treasure_Hoard_CR_17_Up(Number_of_Items=1):
    print((str(Xd6(12) * 1000) + " GP,"), (str(Xd6(8) * 1000) + " PP,"))
    result = []
    for i in range(Number_of_Items):
        d100_roll = Xd100()
        if 1 <= d100_roll <= 2:
            pass
        elif 3 <= d100_roll <= 5:
            result.append(Random_Gemstones_1000GP(Xd6(3)))
            result.append(Magic_Item_Table_C(Xd8()))
        elif 6 <= d100_roll <= 8:
            result.append(Random_Art_Objects_2500GP(Xd10()))
            result.append(Magic_Item_Table_C(Xd8()))
        elif 9 <= d100_roll <= 11:
            result.append(Random_Art_Objects_7500GP(Xd4()))
            result.append(Magic_Item_Table_C(Xd8()))
        elif 12 <= d100_roll <= 14:
            result.append(Random_Gemstones_5000GP(Xd8()))
            result.append(Magic_Item_Table_C(Xd8()))
        elif 15 <= d100_roll <= 22:
            result.append(Random_Gemstones_1000GP(Xd6(3)))
            result.append(Magic_Item_Table_D(Xd6()))
        elif 23 <= d100_roll <= 30:
            result.append(Random_Art_Objects_2500GP(Xd10()))
            result.append(Magic_Item_Table_D(Xd6()))
        elif 31 <= d100_roll <= 38:
            result.append(Random_Art_Objects_7500GP(Xd4()))
            result.append(Magic_Item_Table_D(Xd6()))
        elif 39 <= d100_roll <= 46:
            result.append(Random_Gemstones_5000GP(Xd8()))
            result.append(Magic_Item_Table_D(Xd6()))
        elif 47 <= d100_roll <= 52:
            result.append(Random_Gemstones_1000GP(Xd6(3)))
            result.append(Magic_Item_Table_E(Xd6()))
        elif 53 <= d100_roll <= 58:
            result.append(Random_Art_Objects_2500GP(Xd10()))
            result.append(Magic_Item_Table_E(Xd6()))
        elif 59 <= d100_roll <= 63:
            result.append(Random_Art_Objects_7500GP(Xd4()))
            result.append(Magic_Item_Table_E(Xd6()))
        elif 64 <= d100_roll <= 68:
            result.append(Random_Gemstones_5000GP(Xd8()))
            result.append(Magic_Item_Table_E(Xd6()))
        elif 69 <= d100_roll <= 69:
            result.append(Random_Gemstones_1000GP(Xd6(3)))
            result.append(Magic_Item_Table_G(Xd4()))
        elif 70 <= d100_roll <= 70:
            result.append(Random_Art_Objects_2500GP(Xd10()))
            result.append(Magic_Item_Table_G(Xd4()))
        elif 71 <= d100_roll <= 72:
            result.append(Random_Art_Objects_7500GP(Xd4()))
            result.append(Magic_Item_Table_G(Xd4()))
        elif 72 <= d100_roll <= 72:
            result.append(Random_Gemstones_5000GP(Xd8()))
            result.append(Magic_Item_Table_G(Xd4()))
        elif 73 <= d100_roll <= 74:
            result.append(Random_Gemstones_1000GP(Xd6(3)))
            result.append(Magic_Item_Table_H(Xd4()))
        elif 75 <= d100_roll <= 76:
            result.append(Random_Art_Objects_2500GP(Xd10()))
            result.append(Magic_Item_Table_H(Xd4()))
        elif 77 <= d100_roll <= 78:
            result.append(Random_Art_Objects_7500GP(Xd4()))
            result.append(Magic_Item_Table_H(Xd4()))
        elif 79 <= d100_roll <= 80:
            result.append(Random_Gemstones_5000GP(Xd8()))
            result.append(Magic_Item_Table_H(Xd4()))
        elif 81 <= d100_roll <= 85:
            result.append(Random_Gemstones_1000GP(Xd6(3)))
            result.append(Magic_Item_Table_I(Xd4()))
        elif 86 <= d100_roll <= 90:
            result.append(Random_Art_Objects_2500GP(Xd10()))
            result.append(Magic_Item_Table_I(Xd4()))
        elif 91 <= d100_roll <= 95:
            result.append(Random_Art_Objects_7500GP(Xd4()))
            result.append(Magic_Item_Table_I(Xd4()))
        elif 96 <= d100_roll <= 100:
            result.append(Random_Gemstones_5000GP(Xd8()))
            result.append(Magic_Item_Table_I(Xd4()))
        else:
            result.append("Dice roll exceeds 100")
    return result

# EVERYTHING SHOULD BE SET TO RUN ONCE IF YOU DO NOT ENTER A VALUE
if __name__ == "__main__":

    print(Random_Gemstones_100GP(2))
    # print(Random_Art_Objects_25GP(4))
    # print(Random_Weapon(3))
    # print(Cantrip_Spell_Scroll(9))
    # print(Level_1_Spell_Scroll(9))
    # print(Level_2_Spell_Scroll(3))
    # print((Level_3_Spell_Scroll(4)))
    # print((Level_4_Spell_Scroll(5)))
    # print((Level_5_Spell_Scroll(5)))
    # print((Level_6_Spell_Scroll()))
    # print((Level_7_Spell_Scroll()))
    # print((Level_8_Spell_Scroll()))
    # print((Level_9_Spell_Scroll()))
    # print(Indv_Treasure_CR_0_to_4(Xd6(1)))
    # print(Indv_Treasure_CR_5_to_10())
    # print(Indv_Treasure_CR_11_to_16())
    # print(Indv_Treasure_CR_17_Up())
    # print(Magic_Item_Table_A(Xd4(2)))
    # print(Magic_Item_Table_B())
    # print(Magic_Item_Table_C(Xd8(3)))
    # print(Magic_Item_Table_D(Xd8(3)))
    # print(Magic_Item_Table_E())
    # print(Magic_Item_Table_F())
    # print(Magic_Item_Table_G(5))
    # print(Magic_Item_Table_H(5))
    # print(Magic_Item_Table_I(5))
    # print(Treasure_Hoard_CR_0_t0_4())
    # print(Treasure_Hoard_CR_5_to_10())
    # print(Treasure_Hoard_CR_11_to_16())
    # print(Treasure_Hoard_CR_17_Up())



