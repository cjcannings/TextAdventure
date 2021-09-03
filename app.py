from rooms import scenes
from characters import enemies

# TODO add inventory system to manage items held by player

# Hero class for tracking of player properties/attributes
class Hero:
    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name

# game starter function
def startGame():
    heroName = input('Welcome to the game! What is your name?')
    hero = Hero(10, 2, heroName)

    currentRoom = scenes.get(1)
    loadScene(currentRoom)


# main logic for game
def loadScene(currentRoom):
    while True:
        desc = currentRoom.get('description')
        print(f'{desc} \n')

        actions = currentRoom.get('actions')
        for action in actions.keys():
            print(action)

        while True:
            ans = input('What would you like to do?\n')
            
            if ans not in actions:
                print('That isn\'t an option.')
            else:
                nextRoom = actions.get(ans)

                if nextRoom == 'previous':
                    currentRoom = previousRoom

                elif nextRoom == 'fight':
                    fightScene(currentRoom, nextRoom)

                else:
                    previousRoom = currentRoom
                    currentRoom = scenes.get(nextRoom)

                break

# TODO move fight function inside Hero class to allow proper tracking of health and damage

# function for fighting enemies
def fightScene(currentRoom, nextRoom):
    enemyId = currentRoom.get('enemy')
    enemy = enemies.get(enemyId)
    enemyName = enemy.get('name')
    enemyHealth = enemy.get('health')
    enemyDamage = enemy.get('damage')
    print(f'You attacked the {enemyName}!')
    return



startGame()