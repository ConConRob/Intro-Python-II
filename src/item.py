# Item class holds a name and description


class Item:
    # set the name and description
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    def on_take(self):
        print(f'You have picked up {self.name}.')

    def on_drop(self):
        print(f'You have dropped {self.name}.')

    def use_on_room(self):
        print(f'You don\'t understand how to use {self.name}')
        return False


class Tool(Item):
    def __init__(self, name, description, use_text, use_with=None, ):
        super().__init__(name, description)
        self.use_text = use_text
        if use_with == None:
            self.use_with = []
        else:
            self.use_with = use_with

    def use_on_room(self, room):
        # checks if can be used with that room
        if room in self.use_with:
            # using the item, print text of it being used and return true
            print(f'{self.use_text}  in {room.name}')
            # return another location on the use_with
            for a_room in self.use_with:
                if a_room != room:
                    return a_room
        else:
            # cannot use the item. print a message and return false
            print(f'{self.name} cannot be used in ${room.name}')

# causes a room to be closed off when picked up


class Treasure(Item):
    def __init__(self, name, description, take_text, room_to_close=None, direction=None):
        super().__init__(name, description)
        self.take_text = take_text
        self.room_to_close = room_to_close
        self.direction = direction

    def on_take(self):
        super().on_take()
        # close the room in that direction
        if self.room_to_close:
            try:
                delattr(self.room_to_close, self.direction)
                print(self.take_text)
            except AttributeError:
                c = True
