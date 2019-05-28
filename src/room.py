# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __getitem__(self, key):
        return getattr(self, key)

    def has_key(self, k):
        return f'{k}_to' in self.__dict__

    def take_item(self, item):
         # check if the room has the item
        for itemDic in self.items:
            if itemDic.name == item:
                # true -> remove item from the items and return true
                self.items.remove(itemDic)
                return True
        # false -> return false
        return False
