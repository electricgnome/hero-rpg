class Character:
    def __init__(self, race, health, power):
        self.race=race
        self.health=health
        self.power=power

    def attack(self, monster):
        monster.health -=self.power
        print("The {} bashed the {} for {} damage".format(self.race, monster.race, self.power))

    def __str__(self):
        return 'Person: {} {} {}'.format(self.race, self.health, self.power)


hero=Character('Hero', 10, 5)
goblin=Character('Goblin', 6, 2)

print(hero)
print(goblin)

hero.attack(goblin)
goblin.attack(hero)
while goblin.health > 0 and hero.health > 0:
    print(' ')
