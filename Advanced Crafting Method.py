from random import randint  
from colorama import Fore

#Checking Possible Crafts
def PossibleArmourCrafts():
    pCA = ('Body Armor, Boots, Gloves, Helmet')
    print(pCA)
def PossibleWeaponCrafts():
    pCW = ('One Handed Weapon, Two Handed Weapon')
    print(pCW)
#Checkimg the Possible Bases for the craft
def PossibleOneHWeaponBases():
    pW = ('Claw, Dagger, One Hand Axe, One Hand Mace,One H and Sword, Rune Dagger, Sceptre, Wand')
    print(pW)
def PossibleTwoHWeaponBases():
    p2W = ('Bow, Staff, Two Hand Axe, Two Hand Mace, Two Hand Sword, Warstaff')
def PossibleArmorBases():
    pA = ('STR, DEX, INT, STR/DEX, STR/INT/ DEX/INT')
    print(pA)
#Check possible currencies to use
def PossibleCurrenciesNormal():
    pCN = ('Transmutation, Alchemy, Chance')
    print(pCN)
def PossibleCurrenciesMagic():
    pCM = ('Alteration, Regal, Annul, Scour')
    print(pCM)
def PossibleCurrenciesRare():
    pCR = ('Chaos, Exalted, Annul, Scour')
    print(pCR)

#Random Item Names
BS = ['Brow', 'Corona', 'Cowl', 'Crest', 'Crown', 'Dome', 'Glance', 'Guardian', 'Halo', 'Horn', 'Keep', 'Peak', 'Salvation', 'Shelter', 'Star', 'Veil', 'Visage', 'Visor', 'Ward']

BP = ['Agony', 'Apocalypse', 'Armageddon', 'Beast', 'Behemoth', 'Blight', 'Blood', 'Bramble', 'Brimstone', 'Brood', 'Carrion', 'Cataclysm', 'Chimeric', 'Corpse', 'Corruption', 'Damnation', 'Death', 'Demon', 'Dire', 'Dragon', 'Dread', 'Doom', 'Dusk', 'Eagle', 'Empyrean', 'Fate', 'Foe', 'Gale', 'Ghoul', 'Gloom', 'Glyph', 'Golem', 'Grim', 'Hate', 'Havoc', 'Honour', 'Horror', 'Hypnotic', 'Kraken', 'Loath', 'Maelstrom', 'Mind', 'Miracle', 'Morbid', 'Oblivion', 'Onslaught', 'Pain', 'Pandemonium', 'Phoenix', 'Plague', 'Rage', 'Rapture', 'Rune', 'Skull', 'Sol', 'Soul', 'Sorrow', 'Spirit', 'Storm', 'Tempest', 'Torment', 'Vengeance', 'Victory', 'Viper', 'Vortex', 'Woe', 'Wrath']


def main():
    rarity = 'Normal'
    maxPrefix = 0
    maxSuffix = 0
    prefixes = 0
    suffixes = 0
    mods = list()
    #showing and choosing an item base
    PossibleArmourCrafts()
    PossibleWeaponCrafts()
    iN = str(input('What item do you wanna craft in? '))
    #Checking if the item is in the list

    #Armor Bases
    if iN.upper() in 'Body Armor, Boots, Gloves, Helmet'.upper():
        PossibleArmorBases()
        iB = str(input(f'What base do you want the {iN} to be? '))
        if iB.upper() in 'STR, DEX, INT, STR/DEX, STR/INT/ DEX/INT':
            iL = int(input(f'What ilvl do you want the {iN} to be? '))
    #Weapon Bases
    elif iN.upper() in 'One Handed Weapon'.upper():
        PossibleOneHWeaponBases()
        iB = str(input(f'What base do you want the {iN} to be? '))
        if iB.upper() in 'Claw, Dagger, One Hand Axe, One Hand Mace,One Hand Sword, Rune Dagger, Sceptre, Wand'.upper():
            iL = int(input(f'What ilvl do you want the {iB} to be? '))

    elif iN.upper() in 'Two Handed Weapon'.upper():
        PossibleTwoHWeaponBases()
        iB = str(input(f'What base do you want the {iN} to be? '))
        if iB.upper() in 'Bow, Staff, Two Hand Axe, Two Hand Mace, Two Hand Sword, Warstaff'.upper():
            iL = int(input(f'What ilvl do you want the {iB} to be? '))
    
    print(f'You are starting with a {rarity} rarity {iB} {iN} ilvl {iL}')
    while True:
        if rarity == 'Normal':
            maxPrefix = 0
            maxSuffix = 0
            prefixes = 0
            suffixes = 0
            PossibleCurrenciesNormal()
            q = str(input(f'What do you wanna do with the {iN}? Press Anything else to Exit: '))
            if q.upper() == 'Transmutation'.upper():
                rarity = 'Magic'
                prefixes = randint(0, 1)
                suffixes = randint(0,1)
            elif q.upper() == 'Chance'.upper():
                chance = randint(1,100)
                if chance < 75:
                    rarity = 'Magic'
                    prefixes = randint(0, 1)
                    suffixes = randint(0,1)
                elif chance > 75 and chance < 100:
                    rarity = 'Rare'
                    prefixes = randint(1, 3)
                    suffixes = randint(1, 3)
                else:
                    rarity = 'Unique'
                    False
            elif q.upper() == 'Alchemy'.upper():
                rarity = 'Rare'
                prefixes = randint(1, 3)
                suffixes = randint(1, 3)
            else:
                print('Thanks for Crafting!')
                exit()


        elif rarity == 'Magic':
            maxPrefix = 1
            maxSuffix = 1
            PossibleCurrenciesMagic()
            q = str(input(f'What do you wanna do with the {iN}? '))
            if q.upper() == 'Alteration'.upper():
                rarity = 'Magic'
                prefixes = randint(0, 1)
                suffixes = randint(0,1)
            elif q.upper() == 'Regal'.upper():
                regal = randint(0,1)
                if regal == 0:
                    prefixes += 1
                elif regal == 1:
                    suffixes += 1
                rarity = 'Rare'

                
            elif q.upper() == 'Annul'.upper():
                if prefixes == 0 and suffixes == 0:
                    print('You cannot use an Annul')
                elif prefixes == 0:
                    suffixes -= 1
                elif suffixes == 0:
                    prefixes -= 1                
                rarity = 'Magic'
            elif rarity == 'Augmentation':
                rarity = 'Magic'
                if prefixes == 1 and suffixes == 1:
                    print('You Cannot use an Augment orb')
                else:
                    if prefixes == 1:
                        suffixes += 1
                    elif suffixes == 1:
                        prefixes += 1
                    else:
                        Aug = randint(0,1)
                        if Aug == 0:
                            prefixes += 1
                        elif Aug == 1:
                            suffixes += 1                
            elif q.upper() == 'Scour'.upper():
                rarity = 'Normal'
                prefixes = 0
                suffixes = 0
            else:
                print('Thanks for Crafting!')
                exit()

        elif rarity == 'Rare':
            maxPrefix = 3
            maxSuffix = 3
            PossibleCurrenciesRare()
            q = str(input(f'What do you wanna do with the {iN}? '))
            if q.upper() == 'Chaos'.upper():
                rarity = 'Rare'
                prefixes = randint(1,3)
                suffixes = randint(1,3)
            elif q.upper() == 'Exalted'.upper():
                if prefixes == 3 and suffixes == 3:
                    print('You Cannot use an Exalted orb')
                else:
                    if prefixes == maxPrefix:
                        suffixes += 1
                    elif suffixes == maxSuffix:
                        prefixes += 1
                    else:
                        ex = randint(0,1)
                        if ex == 0:
                            prefixes += 1
                        elif ex == 1:
                            suffixes += 1
                rarity = 'Rare'
            elif q.upper() == 'Scour'.upper():
                rarity = 'Normal'
                prefixes = 0
                suffixes = 0
            elif q.upper() == 'Annul'.upper():
                if prefixes == 0 and suffixes == 0:
                    print('You cannot use an Annul')
                elif prefixes == 0:
                    suffixes -= 1
                elif suffixes == 0:
                    prefixes -= 1
                else:
                    annul = randint(0,1)
                    if annul == 0:
                        prefixes -= 1
                    elif annul == 1:
                        suffixes -= 1
                rarity = 'Rare'
            else:
                print('Thanks for Crafting!')
                exit()

        namePrefix = randint(0,66)
        nameSuffix = randint(0,16)
        global BP
        global BS
        if rarity == 'Normal':
            print(Fore.LIGHTBLACK_EX + rarity)
            print(BP[namePrefix], BS[nameSuffix])
            print(iN + Fore.RESET)
        elif rarity == 'Magic':
            print(Fore.BLUE + rarity)
            print(BP[namePrefix], BS[nameSuffix])
            print(iN + Fore.RESET)
        elif rarity == 'Rare':
            print(Fore.YELLOW + rarity)
            print(BP[namePrefix], BS[nameSuffix])
            print(iN + Fore.RESET)
        print(f'Prefixes = {prefixes}')
        print(f'Suffixes = {suffixes}')

main()