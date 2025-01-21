import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# array of weapons
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

# # Inputs for combat strength of hero
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid Combat Strength , please select between 1-6")
    # default value for invalid input
    combatStrength = 1


# input combat strength for monster
mcombatStrength = int(input("Enter monster's combat strength (1-6): "))
if mcombatStrength < 1 or mcombatStrength > 6:
    print("Invalid Combat Strength , please select between 1-6")
    mcombatStrength = 1


# combatStrength = max(1, min(6, int(input("Hero strength (1-6): "))))
# mCombatStrength = max(1, min(6, int(input("Monster strength (1-6): "))))

#  Simulate the battle rounds

for j in range(1,21,2): # simulation of 20 rounds stepping by 2
    # Dice rolls
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    #calculate the weapon
    heroWeapon = weapons[heroRoll -1 ]
    monsterWeapon = weapons[monsterRoll -1 ]


    # calculate total strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = combatStrength + monsterRoll




    # print round details
    print(f"\nRound {j} Hero Rolled {heroRoll} ,  Monster Rolled {monsterRoll}")
    print(f"Hero selected: {heroWeapon} , Monster Selected: {monsterWeapon}")
    print(f"Hero total strength: {heroTotal} , Monster Total Strength: {monsterTotal}")


    # determine winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round!")
    else:
        print("Its a tie!")

    if j == 11:
        print("\nBattle Truce declared in round 11. Game Over")
        break
if j !=11:
         print("\n Battle concluded after 20 rounds")