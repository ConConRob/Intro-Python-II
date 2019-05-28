# Item class holds a name and description


class Item:
    # set the name and description
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'
