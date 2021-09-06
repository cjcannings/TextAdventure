from rooms import scenes
from characters import enemies

import random

# TODO add inventory system to manage items held by player
# Hero class for tracking of player properties/attributes
class Hero:
    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name

    # function for fighting enemies
    def fight(self, currentRoom):
        enemyId = currentRoom.get('enemy')
        enemy = enemies.get(enemyId)
        enemyName = enemy.get('name')
        enemyHealth = enemy.get('health')
        enemyDamage = enemy.get('damage')

        while enemyHealth > 0:
            # damage dealt is within 20% of the enemy/hero's original damage, allowing same variation
            enemyDealt = random.randint(round(enemyDamage * 0.8), round(enemyDamage * 1.2))
            heroDealt = random.randint(round(self.damage * 0.8), round(self.damage * 1.2))

            enemyHealth -= heroDealt
            print(f'You dealt {heroDealt} damage!')
            # perform check to ensure enemy does not deal damage after health is already depleted
            if enemyHealth <= 0:
                break
            self.health -= enemyDealt
            if self.health <= 0:
                endGame()
            print(f'Ouch! You took {enemyDealt} damage!')

        print(f'You killed the {enemyName}! You have {self.health} health remaining.')

        nextRoomNum = currentRoom.get('next')
        nextRoom = scenes.get(nextRoomNum)
        loadScene(nextRoom, self)

        return

# game starter function
def startGame():
    heroName = input('Welcome to the game! What is your name?')
    print(f'Hello there, {heroName}!')
    hero = Hero(10, 2, heroName)

    currentRoom = scenes.get(1)
    loadScene(currentRoom, hero)


def endGame():
    print('You died.')
    print('Would you look to play again?')
    ans = ''
    while ans.lower() != 'y' or ans.lower() != 'n':
        ans = input('Enter \'y\' for yes, or \'n\' for no.')
        if ans.lower() == 'y':
            startGame()
        elif ans.lower() == 'n':
            print('Thanks for playing! Goodbye.')
            quit()
        else:
            print('I didn\'t understand that.')
    return

# main logic for game
def loadScene(currentRoom, hero):
    while True:
        desc = currentRoom.get('description')
        print(f'{desc} \n')

        actions = currentRoom.get('actions')
        i = 0
        options = {}
        for action in actions.keys():
            i += 1
            options[i] = action
            print(f'{i} - {action}')

        while True:
            ans = int(input('What would you like to do?\n'))
            
            '''
            if ans not in actions:
                print('That isn\'t an option.')
            '''

            if ans not in options.keys():
                print('That is not an option.')
            else:
                #nextRoom = actions.get(ans)
                nextRoom = actions.get(options.get(ans))

                if nextRoom == 'previous':
                    currentRoom = previousRoom

                elif nextRoom == 'fight':
                    hero.fight(currentRoom)

                else:
                    previousRoom = currentRoom
                    currentRoom = scenes.get(nextRoom)

                break





startGame()