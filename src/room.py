# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description,):
        self.name = name
        self.description = description

    def __getitem__(self, key):
        return getattr(self, key)

    def has_key(self, k):
        return f'{k}_to' in self.__dict__
