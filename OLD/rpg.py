from rpg_character import *

hero=Hero('Hero', 10, 5)
goblin=Goblin('Goblin', 6, 2)
wizzard=Hero('wizzard',20,1)
zombie=Zombie("Zombie",20,1)

if __name__=="__main__":
    while goblin.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.\n".format(goblin.health, goblin.power))
        print("""What do you want to do:
            1. Choose opponent
            2. Go to the shop
            3. quit!""")
        print(">", end=' ')
        raw_input =input()
        if raw_input == "1":
            print("""
                1. Goblin
                2. Wizzard
                3. Shadow
                4. Medic
                5. Zombie""")






        if raw_input == "1":
            hero.attack(goblin)
            if not goblin.alive():
                print("The goblin died!")
        elif raw_input =="2":
            if goblin.alive:
                goblin.attack(hero)
                if not hero.alive():
                    print ("you died!")
        elif raw_input =='3':
            print("Goodbye!!")
            break
        else:
            print("invalid input {}".format(raw_input))
