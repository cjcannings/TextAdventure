scenes = {
    1:
    {
        'description': 'This is the starter room.\nThere is a door to your left, staircase to your right, and a large pit ahead of you.',
        'actions': {'Jump in the pit': 2, 'Walk through the door': 3, 'Go upstairs': 4}
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

    4:
    {
        'description': '',
        'actions': ''
    },

    7:
    {
        'description': 'As you walk down the stairs, a shadowy figure appears.\n"Who\'s there?\" the person exclaims.',
        'actions': {'Attack': 'fight'},
        'enemy': 1,
        'next': 8,
    },

    # this is a version of room 7 without the enemy present that
    # can only be accessed by winning the fight in that room
    8:
    {
        'description': 'Having defeated the basement dweller, you search around the room.',
        'actions': {'Go back to the starter room': 1, 'Search the body': 'loot', 'Light the candle': 10},
        'loot': 1,
        'next': 9
    },

    9:
    {
        'description': 'After looting the room, the only way from here is back to where you came from.',
        'actions': {'Go back to the starter room': 1}
    },

    10:
    {
        'description': '''On the walls, you spot a cryptic message, describing an evil being that stands at over
        12 feet tall, warning anybody reading this to avoid conflict with the monster.''',
        'actions': {'Go back to the starter room': 1}
    }
}