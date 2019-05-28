from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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
player = {
    room: room['outside']
}
# Write a loop that:
#
while True:
    # * Prints the current room name
    print(player.room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.room.description)
    # * Waits for user input and decides what to do.
    #
    action = input('pick a direction')
    # If the user enters a cardinal direction, attempt to move to the room there.
    if action == 'n' and 'n_to' in player.room:
        player.room = room[player.room.n_to]
    elif action == 'e' and 'e_to' in player.room:
        player.room = room[player.room.e_to]
    elif action == 's' and 's_to' in player.room:
        player.room = room[player.room.s_to]
    elif action == 'w' and 'w_to' in player.room:
        player.room = room[player.room.w_to]
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    elif action == 'q':
        print("Thanks for playing")
        break
    else:
        print()
