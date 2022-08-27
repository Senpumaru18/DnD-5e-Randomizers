from random import choice, randint, choices
from collections import Counter, defaultdict
from time import time

# Dice rolls
def Xd4(NumberOfRolls=1):
    result = 0
    for i in range(NumberOfRolls):
        result += randint(1, 4)
    return result
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

Name = []
# DragonBorn Names
def DragonbornFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Akra","Aasathra","Antrara","Arava","Biri","Blendaeth","Burana","Chassath","Daar","Dentratha","Doudra",
        "Driindar","Eggren","Farideh","Findex","Furrele","Gesrethe","Gilkass","Harann","Havilar","Hethress","Hillanot",
        "Jaxi","Jezean","Jheri","Kadana","Kava","Korinn","Megren","Mijira","Mishann","Nala","Nuthra","Perra","Pogranix",
        "Pyxrin","Quespa","Raiann","Rezena","Ruloth","Saphara","Savaran","Sora","Surina","Synthrin","Tatyan","Thava",
        "Uadjit","Vezera","Zykroff"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def DragonbornMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Adrex","Arjhan","Azzakh","Balasar","Baradad","Bharash","Bidreked","Dadalan","Dazzazn","Direcris","Donaar",
                "Fax","Gargax","Ghesh","Gorbundus","Greethen","Heskan","Hirrathak","Ildrex","Kaladan","Kerkad","Kiirith",
                "Kriv","Maagog","Medrash","Mehen","Mozikth","Mreksh","Mugrenden","Nadarr","Nithther","Norkruuth","Nykkan",
                "Pandjed","Patrin","Pijjirik","Quarethon","Rathkran","Rhogar","Rivaan","Sethrekar","Shamash","Shedinn",
                "Srorthen","Tarhun","Torinn","Trynnicus","Valorean","Vrondiss","Zedaar"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def DragonbornClan(NumberOfNames=1):
    for i in range(NumberOfNames):
         name = ["Akambherylilax","Argenthrixus","Baharoosh","Beryntolthropal","Bhenkumbyrznaax","Caavyliteradyn","Chumbyxirinnish",
                 "Clethinthiallor","Daardendrian","Delmirev","Dhyrktelonis","Ebynichtomonis","Esstyrlynn","Fharngnarthonost",
                 "Ghaalixirn","Grrrmmballlhyst","Gygazzylyshrift","Hashphronyxadyn","Imbixtellrhyst","Imbixtellrhyst","Jerynomonis",
                 "Jharthraxyn","Kerrhylon","Kimbatull","Lhamboldennish","Linxakasendalor","Mohradylion","Mystan","Nemmonis",
                 "Noprixius","Ophinshtalajiir","Orexijandilin","Pfaphnyrennish","Phrahdrandon","Pyraxtallinost","Qyxphrgh",
                 "Raghthronknaar","Shestendeliath","Skaarzborroosh","Sumnarghthrysh","Tiammanthyllish","Turnuroth","Umbryphrael",
                 "Vangdondalor","Verthisathurgiesh","Wivvyholdalphiax","Wystongjiir","Xwphyrbahnor","Yarjerit","Zzzxaaxthroth"]
         pick = (randint(0,len(name)-1))
         Name.append(name[pick])

# Dwarf Names
def DwarfFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Arbera","Artin","Audhild","Balifra","Barbena","Bardryn","Bolhild","Dagnal","Darriff","Delre","Diesa","Eldeth",
                "Eridred","Falfrunn","Falthra","Finellen","Gillydd","Gunnloda","Gurdis","Helgret","Helja","Hlin","Ilde",
                "Jarana","Kathra","Kilia","Kristryd","Liftrasa","Marastyr","Mardred","Morana","Nalaed","Nora","Nurkara",
                "Oriff","Ovina","Riswynn","Sannl","Therlin","Thodris","Torbera","Tordrid","Torgga","Urshar","Valida","Vistra",
                "Vonana","Werydd","Whurdred","Yurgunn"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def DwarfMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Adrik","Alberich","Baern","Barendd","Beloril","Brottor","Dain","Dalgal","Darrak","Delf","Duergath","Dworic",
                "Eberk","Einkil","Elaim","Eras","Fallond","Fargrim","Gardain","Gilthur","Gimgen","Gimurt","Harbek","Kildrak",
                "Kilvar","Morgran","Morkral","Nalral","Nordak","Nuraval","Oloric","Olunt","Orsik","Oskar","Rangrim","Reirak",
                "Rurik","Taklinn","Thoradin","Thorin","Thradal","Tordek","Traubon","Travok","Ulfgar","Uraim","Veit","Vonbin",
                "Vondal","Whurbin"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def DwarfClan(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Aranore","Balderk","Battlehammer","Bigtoe","Bloodkith","Bofdann","Brawnanvil","Brazzik","Broodfist","Burrowfound",
                "Caebrek","Daerdahk","Dankil","Daraln","Deepdelver","Durthane","Eversharp","Fallack","Fireforge","Foamtankard",
                "Frostbeard","Glanhig","Goblinbane","Goldfinder","Gorunn","Graybeard","Hammerstone","Helcral","Holderhek",
                "Ironfist","Loderr","Lutgehr","Morigak","Orcfoe","Rakankrak","Ruby-eye","Rumnaheim","Silveraxe","Silverstone",
                "Steelfist","Stoutale","Strakeln","Strongheart","Thrahak","Torevir","Torunn","Trollbleeder","Trueanvil",
                "Trueblood","Ungart"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])

# Elf Names
def ElfChild(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Ael","Ang","Ara","Ari","Arn","Aym","Broe","Bryn","Cael","Cy","Dae","Del","Eli","Eryn","Faen","Fera","Gael",
                "Gar","Innil","Jar","Kan","Koeth","Lael","Lue","Mai","Mara","Mella","Mya","Naeris","Naill","Nim","Phann",
                "Py","Rael","Raer","Ren","Rinn","Rua","Sael","Sai","Sumi","Syllin","Ta","Thia","Tia","Traki","Vall","Von",
                "Wil","Za"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def ElfFemaleAdult(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Adire","Ahinar","Althaea","Anastrianna","Andraste","Antinua","Arara","Baelitae","Bethrynna","Birel","Caelynn",
                "Chaedi","Claira","Dara","Drusilia","Elama","Enna","Faral","Felosial","Hatae","Ielenia","Ilanis","Irann",
                "Jarsali","Jelenneth","Keyleth","Leshanna","Lia","Maiathah","Malquis","Meriele","Mialee","Myathethil","Naivara",
                "Quelenna","Quillathe","Ridaro","Sariel","Shanairla","Shava","Silaqui","Sumnes","Theirastra","Thiala","Tiaathque",
                "Traulam","Vadania","Valanthe","Valna","Xanaphia"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def ElfMaleAdult(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Adran","Aeiar","Aerdeth","Ahvain","Aramil","Arannis","Aust","Azaki","Beiro","Berrian","Caeldrim","Carric",
                "Dayereth","Dreali","Efferil","Eiravel","Enialis","Erdan","Erevan","Fivin","Galinndan","Gennal","Hadarai",
                "Halimath","Heian","Himo","Immeral","Ivellios","Korfel","Lamlis","Laucian","Lucan","Mindartis","Naal","Nutae",
                "Paelias","Peren","Quarion","Riardon","Rolen","Soveliss","Suhnae","Thamior","Tharivol","Theren","Theriatis",
                "Thervan","Uthemar","Vanuath","Varis"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def ElfFamily(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Aloro","Amakiir","Amastacia","Ariessus","Arnuanna","Berevan","Caerdonel","Caphaxath","Casilltenirra","Cithreth",
                "Dalanthan","Eathalena","Erenaeth","Ethanasath","Fasharash","Firahel","Floshem","Galanodel","Goltorah","Hanali",
                "Holimion","Horineth","Iathrana","Ilphelkiir","Iranapha","Koehlanna","Lathalas","Liadon","Meliamne","Mellerelel",
                "Mystralath","Nailo","Netyoive","Ofandrus","Ostoroth","Othronus","Qualanthri","Raethran","Rothenel","Selevarun",
                "Siannodel","Suithrasas","Sylvaranth","Teinithra","Tiltathrana","Wasanthi","Withrethin","Xiloscient","Xistsrith",
                "Yaeldrin"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])

# Gnome Names
def GnomeFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Abalaba","Bimpnottin","Breena","Buvvie","Callybon","Caramip","Carlin","Cumpen","Dalaba","Donella","Dubamil",
                "Ella","Ellyjoybell","Ellywick","Enidda","Lilli","Loopmottin","Lorilla","Luthra","Mardnab","Meena","Menny",
                "Mumpena","Nissa","Numba","Nyx","Oda","Oppah","Orla","Panana","Pyntle","Quilla","Ranala","Reddlepop","Roywyn",
                "Salanop","Shamil","Siffress","Symma","Tana","Tenena","Tervaround","Tippletoe","Ulla","Unvera","Veloptima",
                "Virra","Waywocket","Yebe","Zanna"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def GnomeMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Alston","Alvyn","Anverth","Arumawann","Bilbron","Boddynock","Brocc","Burgell","Cockaby","Crampernap","Dabbledob",
                "Delebean","Dimble","Eberdeb","Eldon","Erky","Fablen","Fibblestib","Fonkin","Frouse","Frug","Gerbo","Gibmle",
                "Glim","Igden","Jabble","Jebeddo","Kellen","Kipper","Namfoodle","Oppleby","Orryn","Paggen","Pallabar","Pog",
                "Qualen","Ribbles","Rimple","Roondar","Sapply","Seebo","Senteq","Sindri","Umpen","Warryn","Wiggens","Wobbles",
                "Wrenn","Zaffrab","Zook"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def GnomeClan(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Albaratie","Bafflestone","Beren","Boondiggles","Cobblelob","Daergel","Dunben","Fabblestabble","Fapplestamp",
                "Fiddlefen","Folkor","Garrick","Gimlen","Glittergem","Gobblefirn","Gummen","Horcusporcus","Humplebumple",
                "Ironhide","Leffery","Lingenhall","Loofollue","Maekkelferce","Miggledy","Munggen","Murnig","Musgraben",
                "Nackle","Ningel","Nopenstallen","Nucklestamp","Offund","Oomtrowl","Pilwicken","Pingun","Quilsharpener",
                "Raulnor","Reese","Rofferton","Scheppen","Shadowcloak","Silverthread","Sympony","Tarkelby","Timbers","Turen",
                "Umbodeben","Waggletop","Welber","Wildwander"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])

# Halfling Names
def HalflingFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Alain","Andry","Anne","Bella","Blossom","Bree","Callie","Chenna","Cora","Dee","Dell","Eida","Eran","Euphemia",
                "Georgina","Gynnie","Harriet","Jasmine","Jillian","Jo","Kithri","Lavinia","Lidda","Maegan","Marigold","Merla",
                "Myria","Nedda","Nikki","Nora","Olivia","Paela","Pearl","Pennie","Philomena","Portia","Robbie","Rose","Saral",
                "Seraphina","Shaena","Stacee","Tawna","Thea","Trym","Tyna","Vani","Verna","Wella","Willow"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HalflingMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Alton","Ander","Bernie","Bobbin","Cade","Callus","Corrin","Dannad","Danniel","Eddie","Egart","Eldon","Errich",
                "Fildo","Finnan","Franklin","Garret","Garth","Gilbert","Gob","Harol","Igor","Jasper","Keith","Kevin","Lazam",
                "Lerry","Lindal","Lyle","Merric","Mican","Milo","Morrin","Nebin","Nevil","Osborn","Ostran","Oswalt","Perrin",
                "Poppy","Reed","Roscoe","Sam","Shardon","Tye","Ulmo","Welby","Wendel","Wenner","Wes"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HalflingFamily(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Appleblossom","Bigheart","Brightmoon","Brushgather","Cherrycheeks","Copperkettle","Deephollow","Elderberry",
                "Fastfoot","Fatrabbit","Glenfellow","Goldfound","Goodbarrel","Goodearth","Greenbottle","Greenleaf","High-hill",
                "Hilltopple","Hogcollar","Honeypot","Jamjar","Kettlewhistle","Leagallow","Littlefoot","Nimblefingers","Porridgepot",
                "Quickstep","Reedfellow","Shadowquick","Silvereyes","Smoothhands","Stonebrdige","Stoutbrdige","Stoutman",
                "Strongbones","Sunmeadow","Swiftwhistle","Tallfellow","Tealeaf","Tenpenny","Thistletop","Thorngage","Tosscobble",
                "Underbough","Underfoot","Warmwater","Whispermouse","Wildcloak","Wildhear","Wiseacre"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])

# Half-Orc Names
def Half_OrcFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Arha","Baggi","Bendoo","Bilga","Brakka","Creega","Drenna","Ekk","Emen","Engong","Fistula","Gaaki","Gorga",
                "Grai","Greeba","Grigi","Gynk","Hrathy","Huru","Ilga","Kabbarg","Kansif","Lagazi","Lezre","Murgen","Murook",
                "Myev","Nagrette","Neega","Nella","Nogu","Oola","Ootah","Ovak","Ownka","Puyet","Reeza","Shautha","Silgre",
                "Sutha","Tagga","Tawar","Tomph","Ubada","Vanchu","Vola","Volen","Vorka","Yevelda","Zagga"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def Half_OrcMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Argran","Braak","Brug","Cagak","Dench","Dorn","Dren","Druuk","Feng","Gell","Gnarsh","Grumbar","Gubrash",
                "Hagren","Henk","Hogar","Holg","Imsh","Karash","Karg","Keth","Korag","Krusk","Lubash","Megged","Mhurren",
                "Mord","Morg","Nil","Nybarg","Odorr","Ohr","Rendar","Resh","Ront","Rrath","Sark","Scrag","Sheggen","Shump",
                "Tanglar","Tarak","Thar","Thokk","Trag","Ugarth","Varg","Vilberg","Yurk","Zed"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])

# Tiefling Names
def TieflingFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Akta","Anakis","Armara","Astaro","Aym","Azza","Beleth","Bryseis","Bune","Criella","Damaia","Decarabia",
                "Ea","Gadreel","Gomory","Hecat","Ishte","Jezebeth","Kali","Kallista","Kasdeya","Lerissa","Lilith","Makaria",
                "Manea","Markosian","Mastema","Naamah","Nemeia","Nija","Orianna","Osah","Pheliaia","Prosperine","Purah",
                "Pyra","Rieta","Ronobe","Ronwe","Seddit","Seere","Sekhmet","Semyaza","Shava","Shax","Sorath","Uzza","Vapula",
                "Vepar","Verin"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def TieflingMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Abad","Ahrim","Akemen","Ammon","Andram","Astar","Balam","Barakas","Bathin","Caim","Chem","Cimer","Cressel",
                "Damakos","Ekemon","Euron","Fenriz","Forcas","Habor","Iados","Kairon","Leucis","Mammen","Mantus","Marbas",
                "Melech","Merihim","Modean","Mordai","Mormo","Morthos","Nicor","Oriax","Paymon","Pelaios","Purson","Qemuel",
                "Raam","Rimmon","Sammal","Skamos","Tethren","Thamuz","Therai","Valafar","Vassago","Xappan","Zepar","Zephan"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def TieflingVirtue(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Ambition","Art","Carrion","Chant","Creed","Death","Debauchery","Despair","Doom","Doubt","Dread","Ecstassy",
                "Ennui","Entropy","Excellence","Fear","Glory","Gluttony","Grief","Hate","Hope","Horror","Ideal","Ignominy",
                "Laughter","Love","Lust","Mayhem","Mockery","Murder","Muse","Music","Mystery","Nowhere","Open","Pain","Passion",
                "Poetry","Quest","Random","Reverence","Sorrow","Temerity","Torment","Tragedy","Vice","Virtue","Weary","Wit"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])

# Human Names
def HumanArabicFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanArabicMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanCelticFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanCelticMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanChineseFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanChineseMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanEgyptianFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["A'at","Ahset","Amunet","Aneksi","Atet","Baketamon","Betrest","Bunefer","Dedyet","Hatshepsut","Hentie",
                "Herit","Hetepheres","Intakaes","Ipwet","Itet","Joba","Kasmut","Kemanub","Khemut","Kiya","Maia","Menhet",
                "Merit","Meritamen","Merseger","Muyet","Nebet","Nebetah","Nedjemmut","Neferiti","Neferu","Neihotep","Nit",
                "Nofret","Nubemiunu","Peseshet","Pypuy","Qalhata","Rai","Redji","Sadeh","Sadek","Sitamun","Sitre","Takhat",
                "Tarset","Werenro"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanEgyptianMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Ahmose","Akhom","Amasis","Amenemhet","Anen","Banefre","Bek","Djedefre","Djoser","Hekaib","Henemu","Horemheb",
                "Horwedja","Huya","Ibebi","Idu","Imhotep","Ineni","Ipuki","Irsu","Kagemni","Kawab","Kenamon","Kewap","Khaemwaset",
                "Khafra","Khusebek","Masaharta","Meketre","Merenre","Metjen","Nebamun","Nebetka","Nehi","Nekure","Nessumontu",
                "Pakhom","Pwah","Pawero","Ramose","Rudjek","Sabaf","Sebek-khu","Sebni","Senusret","Shabaka","Somintu",
                "Thaneni","Thethi"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanEnglishFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanEnglishMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanFrenchFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanFrenchMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanGermanFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanGermanMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanGreekFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Acantha","Aella","Alektos","Alkippe","Andromeda","Antigone","Ariadne","Astraea","Chloros","Chryseos","Daphne",
                "Desponia","Dione","Eileithyia","Elektra","Euadne","Eudora","Eunomia","Hekabe","Helene","Hermoione","Hippolyte",
                "Ianthe","Iokaste","Iole","Iphigenia","Ismene","Kalliope","Kallisto","Kalypso","Karme","Kassandra","Kassiopeia",
                "Kirke","Kleio","Klotho","Klytie","Kynthia","Leto","Megaera","Melaina","Melpomene","Nausikaa","Nemesis",
                "Niobe","Ourania","Phaenna","Polymnia","Semele","Theia"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanGreekMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Adonis","Adrastos","Aeson","Aias","Aineias","Aiolos","Alekto","Alkeides","Argos","Brontes","Damazo","Dardanos",
                "Deimos","Diomedes","Endymion","Epimetheus","Erebos","Euandros","Ganymedes","Glaukos","Hektor","Heros","Hippolytos",
                "Iacchus","Iason","Kadmos","Kastor","Kephalos","Kepheus","Koios","Kreios","Laios","Leandros","Linos","Lykos",
                "Melanthios","Menelaus","Mentor","Neoptolemus","Okeanos","Orestes","Pallas","Patroklos","Philandros","Phoibos",
                "Phrixus","Priamos","Pyrrhos","Xanthos","Zephyros"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanIndianFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanIndianMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanJapaneseFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanJapaneseMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanMesoamericanFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanMesoamericanMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanNiger_CongoFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanNiger_CongoMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanNorseFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Alfhild","Arnbjorg","Ase","Aslog","Astrid","Auda","Audhid","Bergljot","Birghild","Bodil","Brenna","Brynhild",
                "Dagmar","Eerika","Eira","Gudrun","Gunborg","Gunhild","Gunvor","Helga","Hertha","Hilde","Hilievi","Ingrid",
                "Iona","Jorunn","Kari","Kenna","Magnhild","Nanna","Olga","Ragna","Ragnhild","Ranveig","Runa","Saga","Sigfrid",
                "Signe","Sigrid","Sigunn","Solveg","Svanhild","Thora","Torborg","Torunn","Tove","Unn","Vigdis","Ylva","Yngvild"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanNorseMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Agni","Alaric","Anvindr","Arvid","Asger","Asmund","Bjarte","Bjorg","Bjorn","Brandr","Brandt","Brynjar",
                "Calder","Colborn","Cuyler","Egil","Einar","Eric","Erland","Fiske","Folvar","Fritjof","Frode","Geir","Halvar",
                "Hemming","Hjalmar","Hjortr","Ingimarr","Ivar","Knud","Leif","Liufr","Manning","Oddr","Olin","Ormr","Ove",
                "Rannulfr","Sigurd","Skari","Snorri","Sten","Stigandr","Stigir","Sven","Trygve","Ulf","Vali","Vidar"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanPolynesianFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanPolynesianMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanRomanFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Aelia","Aemilla","Agrippina","Alba","Aquila","Augusta","Aurelia","Balbina","Blandina","Caeilia","Camilla",
                "Casia","Claudia","Cloelia","Domitia","Drusa","Fabia","Fabricia","Fausta","Flavia","Floriana","Fulvia","Germana",
                "Glaucia","Gratiana","Hadriana","Hermina","Horatia","Hortensia","Iovita","iulia","Laelia","Laurentia","Livia",
                "Longina","Lucilla","Lucretia","Marcella","Marcia","Maxima","Nona","Octavia","Paulina","Petronia","Porcia",
                "Tacita","Tulia","Verginia","Vita"]
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanRomanMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = ["Agni","Alaric","Anvindr","Arvid","Asger","Asmund","Bjarte","Bjorg","Bjorn","Brandr","Brandt","Brynjar",
                "Calder","Colborn","Cuyler","Egil","Einar","Eric","Erland","Fiske","Folvar","Fritjof","Frode","Geir","Halvar",
                "Hemming","Hjalmar","Hjortr","Ingimarr","Ivar","Knud","Leif","Manning","Oddr","Olin","Ormr","Ove","Rannulfr",
                "Sigurd","Skari","Snorri","Sten","Stigandr","Stigr","Sven","Trygve","Ulf","Vali","Vidar"]
        pick = (randint(0,len(name)-1))
        index = name[pick]
        Name.append(index)
def HumanSlavicFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanSlavicMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanSpanishFemale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])
def HumanSpanishMale(NumberOfNames=1):
    for i in range(NumberOfNames):
        name = []
        pick = (randint(0,len(name)-1))
        Name.append(name[pick])

# Other Random Generators
List = []

def MagicShopNames(num=1):
    List.clear()
    ShopName = ["The Wonky Wand", "The Hex Haberdashery", "Blink, Blight & Beyond", "Antilife Shelf", "The Arcane Artisan",
                "Warding Warehouse", "Curse & Carry", "The Counter Counter", "Cone Of Sold", "The Big Box of Boons",
                "The Acolyte Boutique", "Pixies Pick", "The Dangling Orbs", "The Noble Staff", "Scry & Save", "The Crystal Booth",
                "Enchanters Emporium", "Hunters Mark-et", "Barksin & Broomsticks", "Conjure Valley", "Countersells", "Dimension Store",
                "The Flaming Phylactery", "Elder Runes", "Taboo Foundry", "The Crafty Arcanist", "Artifacts R Us", "The Bubbling Cauldron",
                "Elements Emporium", "Fey Factory", "The Wild Draught", "The Mortar & Pestle", "The Wrym & The Wand",
                "The Chromatic Counter", "To The Bitter Ent", "Glyph You Were Here", "Hallucinatory Trade", "Holy Flora",
                "Fireball Forge", "Visionary Illusions", "Wall Of Stone-Mart", "Poltergeists Potions", "The Black Vial",
                "The Whispering Wisp", "Happy Hag Hexes", "Hocus Poultice", "Potions Parlour", "The Brewers Bazaar", "Divine World",
                "Witches & Ward-Robes", "Ooh, New Runes!", "Spirit Talkers", "Chems & Soulgems", "The Corrupt Caster",
                "Onyx Tonics", "Abracadashery", "Spells & Spriggans", "The Golden Oak", "Glyphs & Sundry", "Botanical Boutique",
                "Animate Emporium", "Far Step Florist", "Gust Of Wares", "Homemade Healing", "The Welcoming Whispers",
                "Phoenix Reviving", "The Quivering Amulet", "The Humble Herbalist", "Mage To Order", "Mage To Order",
                "Castcutter", "The Fanciful Druid", "Feylocker", "Conjurenation", "The Casters Warehouse", "Ashes To Acids",
                "Astral Protections", "Presto Charmo", "Glamour Manor", "Myths & Magics", "The Mirrored Chalice",
                "Nowhere To Rune", "Arcane Aficionado", "Bless & Bestow", "Arcana Antiques", "Boons Of The Earth",
                "The Silent Banshee", "Fire & Frost", "The Trembling Talisman", "Scry Me A River", "Fantastical Fey Foray",
                "Trinkets Please", "Radiant Rituals", "The Glowing Sphere", "Suggestion Subhastation", "Forsaken Fortunes",
                "Salamanders Pomander", "Toadstools & Toadstones", "The Magic Box", "Ethereal Emporium", "Mojo Juju"]
    for i in range(num):
        List.append(choice(ShopName))
    return List
def RandomCheck(list_name):
    print(Counter(list_name).most_common())

if __name__ == "__main__":
    # DragonbornClan()
    # rolls = []
    # for x in range(500):
    #     y = XdX(1,50)
    #     rolls.append(y)
    # n = Counter(rolls)
    # m = n.most_common()
    # print(m)
    # print(HumanRomanMale(500))
    DragonbornMale(5)
    print(Name)