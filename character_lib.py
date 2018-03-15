from random import randint as randint

class Character(object):
    def __init__(self, race, health, power, coins, items=[], attacked=False, armor=0):
        self.race=race
        self.health=health
        self.power=power
        self.coins=coins
        self.items=items
        self.attacked=attacked
        self.armor=armor

    def __str__(self):
        return 'Character: {} has {} health, {} power and {} coins'.format(self.race, self.health, self.power, self.coins)

    def status(self):
        return 'Character: {} has {} health, {} power and {} coins'.format(self.race, self.health, self.power, self.coins)

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def special(self, monster):
        if self.attacked:
            defense= monster.power - self.armor
            print("OW!")
            self.health -= defense
            self.attacked = False

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def attack(self, monster):
        # monster.health, self.health -=self.power, monster.power
        if monster.alive():
            monster.health -=self.power
            monster.attacked = True
            print("The {} bashed the {} for {} damage".format(self.race, monster.race, self.power))
            print("The {} hit the {} back for {} damage".format(monster.race, self.race, monster.power))
            monster.special(monster)
        else:
            self.coins +=monster.coins
            print(monster.race, "is dead, you can move on now!")




class Hero(Character):
    def __init__(self, race, health, power, coins, attacked=False):
        super().__init__(race, health, power, coins, attacked=False)

    def attack(self, monster):
        if monster.alive():
            if randint(0,100) <20:
                pwr=self.power *2
            else:
                pwr=self.power
            # monster.health, self.health -=pwr, monster.power
            monster.health -=pwr
            monster.attacked = True
            self.attacked=True
            print("The {} bashed the {} for {} damage".format(self.race, monster.race, pwr))
            print("The {} hit the {} back for {} damage".format(monster.race, self.race, monster.power))
            monster.special(self)
            self.special(monster)
        else:
            self.coins +=monster.coins
            print(monster.race, " is dead, you can move on now!")



class Medic(Character):
    def __init__(self, race, health, power, coins, attacked=False):
        super().__init__(race, health, power, coins, attacked=False)

    def special(self, monster):
        if self.attacked:
            if randint(0,100) <20:
                self.health =self.health +2
                print("The medic healed!")
            self.attacked = False

class Zombie(Character):
    def __init__(self, race, health, power, coins, attacked=False):
        super().__init__(race, health, power, coins, attacked=False)

    def alive(self):
        return True

class Shadow(Character):
    def __init__(self, race, health, power, coins, attacked=False):
        super().__init__(race, health, power, coins, attacked=False)

    def special(self):
        if self.attacked:
            if randint(0,100) <90:
                self.health = 1
                print("You missed!!")
            self.attacked = False


class Wizard(Character):
    def __init__(self, race, health, power, coins, attacked=False):
        super().__init__(race, health, power, coins, attacked=False)

    def attack(self, monster):
        swap =randint(0,100) < 50
        if swap:
            print ("{} swaps power with {} during attack!".format(self.race, monster.race))
            self.power, monster.power = monster.power, self.power
        super(Wizard, self).attack(monster)
        if swap:
            self.power, monster.power = monster.power, self.power


class Tonic(object):
    cost = 5
    name = 'Tonic'

    def apply(self, character):
        character.health +=5
        print("{}'s health increased to {}".format(character.race, character.health))

class Sword(object):
    cost = 10
    name='Sword'

    def apply(self, character):
        character.power +=2
        print("{}'s power increased to {}".format(character.race, character.power))

class Armor(object):
    cost=15
    name='Armor'

    def apply(self, character):
        character.armor= 2

class Store(object):
    items=[Armor, Sword, Tonic]

    def shop(character):
        while True:
            print("=======*==============")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(character.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            choice = int(input("> "))
            if choice == 10:
                break
            elif character.coins >= Store.items[choice - 1].cost:
                ItemToBuy = Store.items[choice - 1]
                item = ItemToBuy()
                character.buy(item)
            else:
                print("You can't afford that!")


goblin=Character('Goblin', 50, 2, 5)
hero=Hero('Hero', 100, 5, 20)
medic=Medic('Medic', 65,3,8)
shadow=Shadow('Shadow',1,2,10)
wizard=Wizard('Wizard', 8,1,6)
zombie=Zombie('Zombie', 5, 1, 200)

print(goblin)
print(hero)
print(medic)
print(shadow)
print(wizard)
print(zombie)


# hero.attack(goblin)
# goblin.attack(hero)
# while goblin.health > 0 and hero.health > 0:
#     print(' ')
