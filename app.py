from rooms import scenes
from characters import enemies
from items import items

import random

# TODO add list of loot/fight rooms that the player has already cleared, preventing them from returning
# Hero class for tracking of player properties/attributes
class Hero:
    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name
        self.inventory = {'consumables': []}

    # function for fighting enemies
    def fight(self, currentRoom):
        enemyId = currentRoom.get('enemy')
        enemy = enemies.get(enemyId)
        enemyName = enemy.get('name')
        enemyHealth = enemy.get('health')
        enemyDamage = enemy.get('damage')
        # TODO implement weapon damage increase if hero has one in inventory
        # TODO implement armour damage reduction if hero has one in inventory
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

    def loot(self, currentRoom):
        lootId = currentRoom.get('loot')
        loot = items.get(lootId)
        lootName = loot.get('name')
        lootType = loot.get('type')
        print(f'You found a {lootName}!')

        if lootType == 'weapon':
            lootDamage = loot.get('damage')
            if self.inventory.get('weapon') is None:
                print(f'This item gives you {lootDamage} extra damage.')
                self.inventory['weapon'] = lootId
            elif lootDamage > items.get(self.inventory.get('weapon')).get('damage'):
                damageDiff = lootDamage - items.get(self.inventory.get('weapon')).get('damage')
                print(f'This item is stronger than your current weapon by {damageDiff} damage.')
                self.inventory['weapon'] = lootId
            else:
                print('Nice find, but this item is weaker than your current weapon.')

        elif lootType == 'armour':
            lootArmour = loot.get('armour')
            if self.inventory.get('armour') is None:
                print(f'This item gives you {lootArmour} extra armour.')
                self.inventory['armour'] = lootId
            elif lootArmour > items.get(self.inventory.get('armour')).get('protection'):
                protectionDiff = lootArmour - items.get(self.inventory.get('armour')).get('protection')
                print(f'This piece of armour gives you {protectionDiff} armour points over what you\'re currently wearing.')
                self.inventory['armour'] = lootId
            else:
                print('A good piece of extra protection, but not as effective as what you already have.')

        # potions, etc.
        elif lootType == 'consumable':
            print(f'You found a {lootName}!')
            self.inventory['consumables'].append(lootId)
        
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

                elif nextRoom == 'loot':
                    hero.loot(currentRoom)

                elif nextRoom == 'fight':
                    hero.fight(currentRoom)

                else:
                    previousRoom = currentRoom
                    currentRoom = scenes.get(nextRoom)

                break





startGame()