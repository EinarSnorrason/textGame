"""Room for game"""


class Dir:
    N = 0
    E = 1
    NW = 2
    NE = 3
    S = 4
    W = 5
    SE = 6
    SW = 7


class Player:
    def __init__(self, room):
        self.room = room
        self.objects = []


class Room:
    def __init__(self, desc, objects=None):
        self.desc = desc
        # Shows objects in room
        self.objects = [] if objects is None else objects
        self.connections = {}

    def __str__(self):
        return self.desc


class Item:
    def __init__(self, name, description, portable=False):
        self.portable = portable
        self.name = name
        self.description = description

    def __str__(self):
        return self.description


class Door(Item):
    def __init__(self, name, description, connection=None):
        super().__init__(name, description)
        self.connection = connection


class Container(Item):
    def __init__(self, name, description, objects=None, locked=False):
        super().__init__(name, description)
        self.objects = objects
        self.open = False
        self.locked = locked
        self.objects = [] if objects is None else objects
