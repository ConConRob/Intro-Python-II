from room import Room
from player import Player
from item import Item
# Declare all the items
knife = Item('Knife', 'A blunt butcher\'s knife')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [knife]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Lukasz', room['outside'])

# Write a loop that:
#
while True:
    # * Prints the current room name
    print(f'\n{player.current_room.name}')
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    # if the room has items print them
    if(len(player.current_room.items) > 0):
        print(f'This room has the following items')
        for item in player.current_room.items:
            print(f'  - {item}')
    # * Waits for user input and decides what to do.
    #
    actions = input('Pick a direction: ').split(' ')
    # one word actions
    if len(actions) == 1:
        action = actions[0]
        # If the user enters a cardinal direction, attempt to move to the room there.
        # if action == 'n' and player.current_room.has_key('n'):
        #     player.current_room = player.current_room.n_to
        # elif action == 'e' and player.current_room.has_key('e'):
        #     player.current_room = player.current_room.e_to
        # elif action == 's' and player.current_room.has_key('s'):
        #     player.current_room = player.current_room.s_to
        # elif action == 'w' and player.current_room.has_key('w'):
        #     player.current_room = player.current_room.w_to
        if action == 'n' or action == 'e' or action == 's' or action == 'w':
            did_move = player.move(action)
            # Print an error message if the movement isn't allowed.
            if(did_move == False):
                print('That movement is not allowed, try again.')
        #
        # If the user enters "q", quit the game.
        elif action == 'q':
            print("Thanks for playing")
            break
        else:
            print(f'"{action}" was not a valid input, try again.')
    # two word actions
    elif len(actions) == 2:
        if actions[0] == 'take' or actions[0] == 'get':
            removed_item = player.current_room.take_item(actions[1])
            if removed_item:
                # add the item to the player
                player.add_item(removed_item)
            else:
                print(f'{actions[1]} does not exist in this room.')
        else:
            print('You are not speaking the games language, try again.')
    else:
        print('You are not speaking the games language, try again.')
