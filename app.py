from rooms import scenes
from characters import enemies
from items import items

import random

# Hero class for tracking of player properties/attributes
class Hero:
    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name
        self.inventory = {'consumables': []}
        self.visited = []

    # function for fighting enemies
    def fight(self, currentRoom):
        enemyId = currentRoom.get('enemy')
        enemy = enemies.get(enemyId)
        enemyName = enemy.get('name')
        enemyHealth = enemy.get('health')
        enemyDamage = enemy.get('damage')

        damageModified = 0
        armourModified = 0

        if self.inventory.get('weapon'):
            damageModified = items.get(self.inventory.get('weapon')).get('damage')
        if self.inventory.get('armour'):
            armourModified = items.get(self.inventory.get('armour')).get('protection')
        while enemyHealth > 0:
            # damage dealt is within 20%, rounded, of the enemy/hero's original damage, allowing same variation
            # subtract armour protection from damage dealt by enemy, and add weapon damage to damage dealt by hero
            enemyDealt = random.randint(round((enemyDamage - armourModified) * 0.8), round((enemyDamage - armourModified) * 1.2))
            heroDealt = random.randint(round((damageModified + self.damage) * 0.8), round((damageModified + self.damage) * 1.2))

            enemyHealth -= heroDealt
            print(f'You dealt {heroDealt} damage!')
            # perform check to ensure enemy does not deal damage after its health is already depleted
            if enemyHealth <= 0:
                break
            self.health -= enemyDealt
            if self.health <= 0:
                endGame()
            print(f'Ouch! You took {enemyDealt} damage!')

        print(f'You killed the {enemyName}! You have {self.health} health remaining.')

        self.visited.append(currentRoom)
        nextRoomNum = currentRoom.get('next')
        nextRoom = scenes.get(nextRoomNum)
        loadScene(nextRoom, self)

        return

    def loot(self, currentRoom):
        lootId = currentRoom.get('loot')
        loot = items.get(lootId)
        lootName = loot.get('name')
        lootType = loot.get('type')

        if currentRoom not in self.visited:
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
            
            self.visited.append(currentRoom)

        # prevent player from visiting loot room more than once
        else:
            print('You have already looted this item!')

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


# end game function called when player dies
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
            if ans not in options.keys():
                print('That is not an option.')
            else:
                nextRoom = actions.get(options.get(ans))

                # if player chooses special room type
                if nextRoom == 'previous':
                    currentRoom = previousRoom
                elif nextRoom == 'loot':
                    hero.loot(currentRoom)
                elif nextRoom == 'fight':
                    hero.fight(currentRoom)

                # if player chooses standard room
                elif scenes.get(nextRoom) not in hero.visited:
                    previousRoom = currentRoom
                    currentRoom = scenes.get(nextRoom)

                # if next room has already been visited in case of fight
                else:
                    print('You can\'t go there again!')
                    continue

                break





startGame()