scenes = {
    1:
    {
        'description': 'This is the starter room.\nThere is a door to your left, staircase to your right, and a large pit ahead of you.',
        'actions': {'Go outside': 200, 'Walk through the door': 300, 'Go upstairs': 400}
    },

    200:
    {
        'description': 'You make your way outside, and notice a fire in the distance within the forest.',
        'actions': {'Walk into the forest': 201, 'Turn around and go back inside': 'previous'}
    },

    201:
    {
        'description': 'As you walk towards the fire, you notice a group of explorers gathered around it. '
        'One of them starts to move away from the rest of the group, but you are unsure why.',
        'actions': {'Slowly approach the group': 202, 'Sneak around behind the straggler': 203}
    },

    202:
    {
        'description': 'Someone from the group spots you approaching, and immediately alerts the others. Suddenly, you find yourself surrounded...',
        'actions': {'Attack the group': 'fight', 'Try to talk with the group': 205, 'Turn away, deeper into the forest': 206},
        'enemy': 3,
        'next': 204
    },

    204:
    {
        'description': 'You survived.. they\'re all dead but one managed to flee.',
        'actions': {'Loot the bodies': 'loot', 'Chase after the straggler': 207, 'Look around the camp': 208},
        'loot': 2,
        'next': 208
    },

    205:
    {
        'description': '',
        'actions': {}
    },

    206:
    {
        'description': '',
        'actions': {}
    },

    207:
    {
        'description': '',
        'actions': {}
    },

    208:
    {
        'description': 'There isn\'t anything of much use to you lying around here, maybe you should\'ve followed the surivor instead.',
        'actions': {'Go back into the starter room': 1, 'Go in the same direction you saw the survivor run': 209}
    },

    300:
    {
        'description': 'You\'ve found the entrance to the basement. Who knows what might be down there...',
        'actions': {'Walk down the stairs': 301, 'Turn around': 'previous'},
        'next': 302
    },

    301:
    {
        'description': 'As you walk down the stairs, a shadowy figure appears.\n"Who\'s there?\" the person exclaims.',
        'actions': {'Attack': 'fight', 'State your name': 307},
        'enemy': 1,
        'next': 302
    },

    # this is a version of room 301 without the enemy present that
    # can only be accessed by winning the fight in that room
    302:
    {
        'description': 'Having defeated the basement dweller, you search around the room.',
        'actions': {'Go back to the starter room': 1, 'Search the body': 'loot', 'Light the candle': 304},
        'loot': 1,
        'next': 303
    },

    303:
    {
        'description': 'After looting the room, the only way from here is back to where you came from.',
        'actions': {'Go back to the starter room': 1, 'Take a closer look': 304}
    },

    304:
    {
        'description': ('On the walls, you spot a cryptic message, describing an evil being that stands at over '
        '12 feet tall, warning anybody reading this to avoid conflict with the monster.\n'
        'Before leaving to go back, you notice a hatch in the ground that someone clearly tried to cover up.'),
        'actions': {'Go back to the starter room': 1, 'Investigate the hatch': 305}
    },

    305:
    {
        'description': ('As you move the bookshelf that stands between you and the hatch, you notice that it is locked.\n'
        'You\'ll need to find the right key to unlock it.'),
        'actions': {'Open the hatch': 'locked', 'Go back to search for the missing key': 1},
        'required': 2,
        'next': 306
    },

    306:
    {
        'description': ('The hatch creaks open, revealing a ladder that leads into darkness. It would be unwise to\n'
        'descend without a source of light, but that\'s never stopped you from taking an adventure in the past...'),
        'actions': {'test': 'test'},
        'required': 3,
        'next': 0
    },

    307:
    {
        'description': ('You confidently tell the basement dweller your name, and he proceeds to question why you are here.\n'
        '"I\'m an adventurer!" you proclaim, before stating that you are trying to solve the mystery behind the strange noises '
        'every night.\nSo far, your clues have lead you here, and with such a strange looking being stood before you, you\'re '
        'confident you\'ve come to the right place.'),
        'actions': {}
    },

}