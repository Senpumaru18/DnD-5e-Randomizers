encounterKey = {1 : {25 : "Easy", 50 : "Medium", 75 : "Hard", 100 : "Deadly"},
            2 : {50 : "Easy", 100 : "Medium", 150 : "Hard", 200 : "Deadly"},
            3 : {75 : "Easy", 150 : "Medium", 225 : "Hard", 400 : "Deadly"},
            4 : {125 : "Easy", 250 : "Medium", 375 : "Hard", 500 : "Deadly"},
            5 : {250 : "Easy", 500 : "Medium", 750 : "Hard", 1100 : "Deadly"},
            6 : {300 : "Easy", 600 : "Medium", 900 : "Hard", 1400 : "Deadly"},
            7 : {350 : "Easy", 750 : "Medium", 1100 : "Hard", 1700 : "Deadly"},
            8 : {450 : "Easy", 900 : "Medium", 1400 : "Hard", 2100 : "Deadly"},
            9 : {550 : "Easy", 1100 : "Medium", 1600 : "Hard", 2400 : "Deadly"},
            10 : {600 : "Easy", 1200 : "Medium", 1900 : "Hard", 2800 : "Deadly"},
            11 : {800 : "Easy", 1600 : "Medium", 2400 : "Hard", 3600 : "Deadly"},
            12 : {1000 : "Easy", 2000 : "Medium", 3000 : "Hard", 4500 : "Deadly"},
            13 : {1100 : "Easy", 2200 : "Medium", 3400 : "Hard", 5100 : "Deadly"},
            14 : {1250 : "Easy", 2500 : "Medium", 3800 : "Hard", 5700 : "Deadly"},
            15 : {1400 : "Easy", 2800 : "Medium", 4300 : "Hard", 6400 : "Deadly"},
            16 : {1600 : "Easy", 3200 : "Medium", 4800 : "Hard", 7200 : "Deadly"},
            17 : {2000 : "Easy", 3900 : "Medium", 5900 : "Hard", 8800 : "Deadly"},
            18 : {2100 : "Easy", 4200 : "Medium", 6300 : "Hard", 9500 : "Deadly"},
            19 : {2400 : "Easy", 4900 : "Medium", 7300 : "Hard", 10900 : "Deadly"},
            20 : {2800 : "Easy", 5700 : "Medium", 8500 : "Hard", 12700 : "Deadly"}}

crEXP = {0 : 10, 
         .125 : 25,
         .25 : 50,
         .5 : 100,
         1 : 200,
         2 : 450,
         3 : 700,
         4 : 1100,
         5 : 1800,
         6 : 2300,
         7 : 2900,
         8 : 3900,
         9 : 5000,
         10 : 5900,
         11 : 7200,
         12 : 8400,
         13 : 10000,
         14 : 11500,
         15 : 13000,
         16 : 15000,
         17 : 18000,
         18 : 20000,
         19 : 22000,
         20 : 25000,
         21 : 33000,
         22 : 41000,
         23 : 50000,
         24 : 62000,
         25 : 75000,
         26 : 90000,
         27 : 105000,
         28 : 120000,
         29 : 135000,
         30 : 155000
         }

def DifficultyCalc(PartyLvl):
    xpTotal = 0
    for key in crEXP:
        creatures = int(input(f"How many CR {key} monsters are you using: "))
        xpTotal += (crEXP[key] * creatures)
    
    adjustedXP = xpTotal/PartyLvl
    Difficulty = "Trivial"
    for xp in encounterKey[PartyLvl]:
        if adjustedXP >= xp:
            Difficulty = encounterKey[PartyLvl][xp]
        else:
            break
    print(Difficulty)

        

def main():
    DifficultyCalc(15)


if __name__ == "__main__":
    main()


""" 
1. Check party level
2. Grab dictionary for that level
3. Check first amount to see if greater
4. Return Trivial if not above that
5. Continue checking each variable until it finds a greater value or reaches the end
"""
