# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    # set the init value
    def __init__(self, name, current_room, items):
        self.current_room = current_room
        self.name = name
        self.items = items

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        self[key] = value

    # moving method
    def move(self, direction):
        # checks if can move in that direction
        if self.current_room.has_key(direction):
            # moves in that direction
            self.current_room = self.current_room[f'{direction}_to']
            # return that the move has a success
            return True
        # return that the move was not possible
        return False
    # add a item to the player

    def take_item(self, item_name):
        # remove the item from the room
        item = self.current_room.take_item(item_name)
        if item:
             # add the item to the player
            self.items.append(item)
            item.on_take()
        else:
            # item was not found in the room
            print(f'{item_name} does not exist in this room.')

    def drop_item(self, item):
        dropped = False
        # check if the room has the item
        for item_dic in self.items:
            if item_dic.name == item:
                # true -> remove item from the items and return true
                self.items.remove(item_dic)
                # put the item in the current room
                self.current_room.drop_item(item_dic)
                # run drop method
                item_dic.on_drop()
                dropped = True

        if dropped == False:
            print(f'You don\'t have a "{item}" to drop.')

    def use_item(self, item_name):
        # check if you have the item
        has_item = False
        for item in self.items:
            if item.name == item_name:
                next_room = item.use_on_room(self.current_room)
                if next_room:
                    self.current_room = next_room
                has_item = True
        if has_item == False:
            print(f'You don\'t have a "{item_name}" to use.')

    def show_inventory(self):
        if len(self.items) > 0:
            print('You are holding:')
            for item in self.items:
                print(f'  - {item}')
        else:
            print('You are not holding anything.')
