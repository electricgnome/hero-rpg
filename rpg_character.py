import random


class Character:
    def __init__(self, race, health, power):
        self.race=race
        self.health=health
        self.power=power

    def attack(self, monster):
        monster.health -=self.power
        if monster == zombie:
             monster.health +=self.power
        print("The {} bashed the {} for {} damage".format(self.race, monster.race, self.power))

    def __str__(self):
        return 'Character: {}, health: {}, power: {}'.format(self.race, self.health, self.power)

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def status(self):
        print("{}'s health is at {}".format(self.race, self.health))





class Hero(Character):
    def __init__(self, race, health, power):
        super().__init__(race,health,power)

    def attack(self, monster):
        if random.randint(0,100) < 20:
            pwr =self.power *2
        else:
            pwr=self.power
        monster.health -=pwr
        # if monster == zombie:
        #     monster.health +=self.power
        print("The {} bashed the {} for {} damage".format(self.race, monster.race, pwr))


class Goblin(Character):
    def __init__(self, race, health, power):
        super().__init__(race,health,power)

class Zombie(Character):
    def __init__(self, race, health, power):
        super().__init__(race,health,power)

class Medic(Character):
    def __init__(self, race, health, power):
        super().__init__(race,health,power)



# print(hero)
# print(goblin)
#
# hero.attack(goblin)
# goblin.attack(hero)
#
