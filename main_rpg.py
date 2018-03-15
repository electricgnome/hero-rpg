enemies= ['goblin', 'medic', 'shadow', 'wizard', 'zombie']
def choose_enemy():
    print ('Choose an enemy to fight!')
    for i in range(len(enemies)):
        print (i+1, enemies[i])
    print("> ", end=' ')
    keyinput = int(input())
    if keyinput == 1:
        hero.attack(enemy)
    elif keyinput == 2:
        pass
    elif keyinput == 3:
        print("Goodbye.")
        main_menu()
    else:
        print("Invalid input {}".format(input))
        continue

def main_manu():
    print("""What do you want to do?
        1. Do battle
        2. Go shopping
        3. View my stats
        9. Exit game""")

    keyinput = int(input())
    if keyinput == 1:
        choose_enemy()
    elif keyinput == 2:
        Store.shop(hero)
    elif keyinput == 3:
        hero.status()
    elif keyinput == 9:
        print("Goodbye.")
        exit(0)
    else:
        print("Invalid input {}".format(input))
        continue
