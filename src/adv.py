from room import Room
from player import Player
from item import Item
from item import Tool
from item import Treasure
# Declare all the items
knife = Item('Knife', 'A blunt butcher\'s knife')
bow_and_arrow = Tool('Bow', 'A old but sturdy bow and arrow',
                     '''You find a rope near by and fasten it to the arrow. 
Taking aim you fire the rope into a piece of wood on the far 
side of the chasm and start to cross ''')
gold_cup = Treasure('Cup', 'A small but very valuable gold cup',
                    'You hear a creaking nose. I might not be able to return the way I came')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [knife]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there does not appear to be a way to cross the chasm.""", []),

    'exit': Room("A Winding Exit", """After crossing the chasm you find yourself facing a narrow passage that 
appears to take you outside to safety. I should go back and look for treasure before I leave """, []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [bow_and_arrow]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [gold_cup]),
}
# Declare what items can be used with what room
bow_and_arrow.use_with.append(room['overlook'])
bow_and_arrow.use_with.append(room['exit'])

gold_cup.room_to_close = room['foyer']
gold_cup.direction = 's_to'

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

line = '============================================'
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Lukasz', room['outside'], [])

# Write a loop that:
#
while True:
    # * Prints the current room name
    print(f'{line}\n{player.current_room.name}')
    # * Prints the current description (the text wrap module might be useful here).
    print(player.current_room.description)
    # if the room has items print them
    if(len(player.current_room.items) > 0):
        print(f'This room has the following items')
        for item in player.current_room.items:
            print(f'  - {item}')
    # * Waits for user input and decides what to do.
    #
    actions = input(f'{line}\nPick a direction: ').split(' ')
    # one word actions
    if len(actions) == 1:
        action = actions[0]
        # If the user enters a cardinal direction, attempt to move to the room there.
        if action == 'n' or action == 'e' or action == 's' or action == 'w':
            did_move = player.move(action)
            # Print an error message if the movement isn't allowed.
            if(did_move == False):
                print('That movement is not allowed, try again.')
        # show inventory
        elif action == 'i':
            player.show_inventory()
        # If the user enters "q", quit the game.
        elif action == 'q':
            print("Thanks for playing")
            break
        else:
            print(f'"{action}" was not a valid input, try again.')
    # two word actions
    elif len(actions) == 2:
        if actions[0] == 'take' or actions[0] == 'get':
            player.take_item(actions[1])
        # check if drop
        elif actions[0] == 'drop':
            # drop the item
            removed_item = player.drop_item(actions[1])
        elif actions[0] == 'use':
            # try to use the item
            used = player.use_item(actions[1])
        else:
            print('You are not speaking the games language, try again.')
    else:
        print('You are not speaking the games language, try again.')
    # CHECK IF THE PLAYER IS OUT WITH THE CUP
    if(player.current_room == room['exit'] and gold_cup in player.items):
        # print a win message
        print('''You find yourself facing a narrow passage that
takes you to safety. You escaped with the Gold Cup! 
            YOU WIN!!!!!!!!!!!!!!!!!''')
        # end the game
        break
