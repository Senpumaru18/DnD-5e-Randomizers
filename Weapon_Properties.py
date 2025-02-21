from random import randint

def main():
    Minor_Benefical(1)
    # Major_Benefical(1)
    # Minor_Detrimental(1)
    # Major_Detrimental(1)

def XdX(NumberOfRolls=1, NumberOfSides=2):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, NumberOfSides)
    return result

def Minor_Benefical(num=1):
    for x in range(num):
        pick = XdX(1,100)
        if pick <=20:
            print("While attuned to the artifact, you gain proficiency in one skill of the DM’s choice\n")
        if pick >= 21 and pick <= 30:
            print("While attuned to the artifact, you are immune to disease.\n")
        if pick >= 31 and pick <= 40:
            print("While attuned to the artifact, you can’t be charmed or frightened.\n")
        if pick >= 41 and pick <= 50:
            print("While attuned to the artifact, you have resistance against one damage type of the DM’s choice.\n")
        if pick >= 51 and pick <= 60:
            print("While attuned to the artifact, you can use an action to cast one cantrip (chosen by the DM) from it.\n")
        if pick >= 61 and pick <= 70:
            print("While attuned to the artifact, you can use an action to cast one lst-level spell (chosen by the DM) from it. After you cast the spell, roll a d6. On a roll of 1-5, you can’t cast it again until the next dawn.\n")
        if pick >= 71 and pick <= 80:
            print("While attuned to the artifact, you can use an action to cast one 2nd-level spell (chosen by the DM) from it. After you cast the spell, roll a d6. On a roll of 1-5, you can’t cast it again until the next dawn.\n")
        if pick >= 81 and pick <= 90:
            print("While attuned to the artifact, you can use an action to cast one 3rd-level spell (chosen by the DM) from it. After you cast the spell, roll a d6. On a roll of 1-5, you can’t cast it again until the next dawn.\n")
        if pick >= 91 and pick <= 100:
            print("While attuned to the artifact, you gain a +1 bonus to Armor Class.\n")

def Major_Benefical(num=1):
    for x in range(num):
        pick = XdX(1,100)
        if pick <=20:
            print("While attuned to the artifact, one of your ability scores (DM’s choice) increases by 2, to a maximum of 24.\n")
        if pick >= 21 and pick <=30:
            print("While attuned to the artifact, you regain ld6 hit points at the start of your turn if you have at least 1 hit point.\n")
        if pick >= 31 and pick <=40:
            print("When you hit with a weapon attack while attuned to the artifact, the target takes an extra ld6 damage of the weapon’s type.\n")
        if pick >= 41 and pick <=50:
            print("While attuned to the artifact, your walking speed increases by 10 feet.\n")
        if pick >= 51 and pick <=60:
            print("While attuned to the artifact, you can use an action to cast one 4th-!evel spell (chosen by the DM) from it. After you cast the spell, roll a d6. On a roll of 1-5, you can’t cast it again until the next dawn.\n")
        if pick >= 61 and pick <=70:
            print("While attuned to the artifact, you can use an action to cast one 5th-!evel spell (chosen by the DM) from it. After you cast the spell, roll a d6. On a roll of 1-5, you can’t cast it again until the next dawn.\n")
        if pick >= 71 and pick <=80:
            print("While attuned to the artifact, you can use an action to cast one 6th-!evel spell (chosen by the DM) from it. After you cast the spell, roll a d6. On a roll of 1-5, you can’t cast it again until the next dawn.\n")
        if pick >= 81 and pick <=90:
            print("While attuned to the artifact, you can use an action to cast one 7th-!evel spell (chosen by the DM) from it. After you cast the spell, roll a d6. On a roll of 1-5, you can’t cast it again until the next dawn.\n")
        if pick >= 91 and pick <=100:
            print("While attuned to the artifact, you can’t be blinded, deafened, petrified, or stunned\n")

def Minor_Detrimental(num=1):
    for x in range(num):
        pick = XdX(1,100)
        if pick <= 5:
            print("While attuned to the artifact, you have disadvantage on saving throws against spells,\n")
        if pick >= 6 and pick <= 10:
            print("The first time you touch a gem or piece of jewelry while attuned to this artifact, the value of the gem or jewelry is reduced by half,\n")
        if pick >= 11 and pick <= 15:
            print("While attuned to the artifact, you a re b I i nded when you are more than 10 feet away from it.\n")
        if pick >= 16 and pick <= 20:
            print("While attuned to the artifact, you have disadvantage on saving throws against poison,\n")
        if pick >= 21 and pick <= 30:
            print("While attuned to the artifact, you emit a sour stench noticeable from up to 10 feet away,\n")
        if pick >= 31 and pick <= 35:
            print("While attuned to the artifact, all holy water within 10 feet of you is destroyed,\n")
        if pick >= 36 and pick <= 40:
            print("While attuned to the artifact, you are physically it! and have disadvantage on any ability check or saving throw that uses Strength or Constitution,\n")
        if pick >= 41 and pick <= 45:
            weight = XdX(1,4)*10
            print(f"While attuned to the artifact, your weight increases by {weight} pounds\n")
        if pick >= 46 and pick <= 50:
            print("While attuned to the artifact, your appearance changes as the DM decides\n")
        if pick >= 51 and pick <= 55:
            print("While attuned to the artifact, you are deafened when you are more than 10 feet away from it,\n")
        if pick >= 56 and pick <= 60:
            weight = XdX(1,4)*5
            print(f"While attuned to the artifact, your weight drops by {weight} pounds.\n")
        if pick >= 61 and pick <= 65:
            print("While attuned to the artifact, you can't smell,\n")
        if pick >= 66 and pick <= 70:
            print("While attuned to the artifact, nonmagical flames are extinguished within 30 feet of you.\n")
        if pick >= 71 and pick <= 80:
            print("While you are attuned to the artifact, other creatures can't take short or long rests while within 300 feet of you.\n")
        if pick >= 81 and pick <= 85:
            print("While attuned to the artifact, you deal ld6 necrotic damage to any plant you touch that isn't a creature,\n")
        if pick >= 86 and pick <= 90:
            print("While you are attuned to the artifact, animals within 30 feet of you are hostile toward you\n")
        if pick >= 91 and pick <= 95:
            print("While attuned to the artifact, you must eat and drink six times the normal amount each day.\n")
        if pick >= 96 and pick <= 100:
            print("While you are attuned to the artifact, your flaw is amplified in a way determined by the DM.\n")
        
def Major_Detrimental(num=1):
    for x in range(num):
        pick = XdX(1,100)
        if pick <= 5:
            print("While you are attuned to the artifact, your body rots over the course of four days, after which the rotting stops. You lose your hair by the end of day 1, finger tips and toe tips by the end of day 2, lips and nose by the end of day 3, and ears by the end of day 4. A regenerate spell restores lost body pans\n")
        if pick >= 6 and pick <= 10:
            print("While you are attuned to the artifact, you determine your alignment daily at dawn by rolling a d6 twice. On the first roll, a 1-2 indicates lawfu 3-4 neutral, and 5-6 chaotic. On the second roll. ^ 1-2 indicates good, 3-4 neutral, and 5-6 evil\n")
        if pick >= 11 and pick <= 15:
            print("When you first attune to the artifact, it gives you a quest determined by the DM. You must complete this quest as if affected by the geas spell. Once yo complete the quest, you are no longer affected b> this property\n")
        if pick >= 16 and pick <= 20:
            print("The artifact houses a bodiless Ire force that is hostile toward you. Each time you use an action to use one of the artifact’s properties, there is a 50 percent chance that the life force tries to leave the artifact and enter your body. If you fail a DC 20 Charisma saving throw, it succeeds, and you become an NPC under the DM's control until the intruding life force is banished using magic such the dispel evil and good spell\n")
        if pick >= 21 and pick <= 25:
            print("Creatures with a challenge rating of 0, as well as plants that aren’t creatures, drop to 0 hit points when within 10 feet of the artifact.\n")
        if pick >= 26 and pick <= 30:
            print("The artifact : mprisons a death slaad (see the Monster Manual ), Each time you use one of the artifact's properties as an action, the slaad has a 10 percent chance of escaping, whereupon it appears within 15 feet of you and attacks you\n")
        if pick >= 31 and pick <= 35:
            print("While you are attuned to the artifact, creatures of i particular type other than humanoid (as chosen by the DM) are always hostile toward you\n")
        if pick >= 36 and pick <= 40:
            print("The artifact dilutes magic potions within 10 feet o r it, rendering them nonmagical,\n")
        if pick >= 41 and pick <= 45:
            print("The artifact erases magic scrolls within 10 feet of it, rendering them nonmagical,\n")
        if pick >= 46 and pick <= 50:
            print("Before using one of the artifact’s properties as an action, you must use a bonus action to draw blood, either from yourself or from a willing or incapacitated creature within your reach, using a piercing or slashing melee weapon. The subject takes ld4 damage of the appropriate type.\n")
        if pick >= 51 and pick <= 60:
            print("When you become attuned to the artifact, you gain a form of long-term madness (see chapter 8. Running the Game)\n")
        if pick >= 61 and pick <= 65:
            print("You take 4dl0 psychic damage when you become attuned to the artifact,\n")
        if pick >= 66 and pick <= 70:
            print("You take Sdl0 psychic damage when you become attuned to the artifact,\n")
        if pick >= 71 and pick <= 75:
            print("Before you can become attuned to the artifact, you must kill a creature of your alignment\n")
        if pick >= 76 and pick <= 80:
            print("When you become attuned to the artifact, one of your ability scores is reducedc by 2 at random. A greater restoration spell restores the ability to normal\n")
        if pick >= 81 and pick <= 85:
            print("Each time you become attuned to ve artifact. you age 3d1G years. You must succeed on a DC 10 Constitution saving throw or die from the shock, [f you die, you are instantly transformed into a wight (see the Monster Manual) under the DM’s control that ts sworn to protect the artifact\n")
        if pick >= 86 and pick <= 90:
            print("While attuned to the artifact, you lose the ability to speak\n")
        if pick >= 91 and pick <= 95:
            print("While attuned to the artifact, you have vulnerability to ail damage\n")
        if pick >= 96 and pick <= 100:
            print("When you become attuned to the artifact, there is a 10 percent chance that you attract the attention of a god that sends an avatar to wrest the artifact from you. The avatar has the same alignment as its creator and the statistics of an empyrean (see the Monster Manual). Once it obtains the artifact, the avatar vanishes\n")
        



if __name__ == "__main__":
    main()