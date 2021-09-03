scenes = {
    1:
    {
        'description': 'This is the starter room.',
        'actions': {'Jump in the pit': 2, 'Walk through the door to your left': 3, 'Go upstairs': 4}
    },

    2:
    {
        'description': 'You fell down into the pit and hurt your knee.',
        'actions': {'Get up and limp towards the door infront of you': 5, 'Call for help': 6}
    },

    3:
    {
        'description': 'You\'ve found the entrance to the basement. Who knows what might be down there...',
        'actions': {'Walk down the stairs': 7, 'Turn around': 'previous'}
    },



    7:
    {
        'description': 'As you walk down the stairs, a shadowy figure appears.\n"Who\'s there?\" the person exclaims.',
        'actions': {'Attack': 'fight'}
    }
}