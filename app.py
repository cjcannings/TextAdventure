from rooms import scenes

def startGame():
    currentRoom = scenes.get(1)
    loadScene(currentRoom)


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
                else:
                    previousRoom = currentRoom
                    currentRoom = scenes.get(nextRoom)
                break


startGame()