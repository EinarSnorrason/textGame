"""Room for game"""


class Dir:
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


class Room:
    opposite = {Dir.NORTH: Dir.SOUTH, Dir.SOUTH: Dir.NORTH, Dir.EAST: Dir.WEST, Dir.WEST: Dir.EAST}

    def __init__(self, desc, objects=None):
        self.desc = desc
        self.connections = {Dir.NORTH: None, Dir.SOUTH: None, Dir.EAST: None, Dir.WEST: None}
        self.objects = objects

    def __str__(self):
        return self.desc

    def connect(self, other_room, direction):
        # Connects room to other room
        self.connections[direction] = other_room
        other_room.connections[self.opposite[direction]] = self

    def move(self, direction):
        # Move to another room
        if not self.connections[direction]:
            raise LookupError("No connection")
        return self.connections[direction]

