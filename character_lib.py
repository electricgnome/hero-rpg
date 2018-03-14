from random import randint as randint

class Character(object):
    def __init__(self, race, health, power, coins, items=[], attacked=False):
        self.race=race
        self.health=health
        self.power=power
        self.coins=coins
        self.items=items
        self.attacked=attacked

    def __str__(self):
        return 'Character: {} has {} health, {} power and {} coins'.format(self.race, self.health, self.power, self.coins)

    def status(self):
        return 'Character: {} has {} health, {} power and {} coins'.format(self.race, self.health, self.power, self.coins)

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def special(self):
        if self.attacked:
            self.attacked = False


    def attack(self, monster):
        # monster.health, self.health -=self.power, monster.power
        monster.health -=self.power
        if monster.alive:
            monster.attacked = True
        print("The {} bashed the {} for {} damage".format(self.race, monster.race, self.power))
        print("The {} hit the {} back for {} damage".format(monster.race, self.race, monster.power))
        monster.special()




class Hero(Character):
    def __init__(self, race, health, power, coins, attacked=False):
        super().__init__(race, health, power, coins, attacked=False)

    def attack(self, monster):
        if randint(0,100) <20:
            pwr=self.power *2
        else:
            pwr=self.power
        # monster.health, self.health -=pwr, monster.power
        monster.health -=pwr
        if monster.alive:
            monster.attacked = True
        print("The {} bashed the {} for {} damage".format(self.race, monster.race, pwr))
        print("The {} hit the {} back for {} damage".format(monster.race, self.race, monster.power))
        monster.special()


class Medic(Character):
    def __init__(self, race, health, power, coins, attacked=False):
        super().__init__(race, health, power, coins, attacked=False)

    def special(self):
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
