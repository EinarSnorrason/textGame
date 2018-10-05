"""Various actions that can be taken"""
from objects import *

# Setup functions

player = Player(None)


def opposite(direction):
    """Takes a cardinal direction and returns the opposite"""
    return (direction + 4) % 8


def connect(room1, room2, direction):
    """Connects two rooms. The direction shows the way from room1 to room2"""
    room1.connections[direction] = room2
    room2.connections[opposite(direction)] = room1


# Support functions

def current_room():
    return player.room


# Play functions


def move(direction):
    player.room = current_room().connections[direction]


def insert_object(obj, container):
    container.objects.append(obj)


def remove_object(obj, container):
    return container.objects.remove(obj)


def pickup_object(obj, container=None):
    if container is None:
        container = current_room()
    player.objects.append(remove_object(obj, container))


def visible_items(room):
    """Return an iterator with all visible items in a room, including things in open containers"""
    items = []
    for i in room.objects:
        items.append(i)
        if i is Container:
            items.extend(visible_items(i))
    return items


# String parsing
def choose_one(options):
    """If a player choice is ambiguous, this method asks them to elaborate and returns the chosen option"""
    print("Which one did you mean?")
    for i in options:
        print("{}: {}".format(i + 1, options[i].name))
    try:
        i = int(input("\nEnter the number you want to pick:\n"))
        return options[i - 1]
    except (ValueError, KeyError):
        print("Sorry, I don't understand")
        return choose_one(options)


def locate_name(s):
    """Takes a string and returns the object that matches that name (if any)"""
    matches = []
    for i in visible_items(current_room()):
        if i.name.startswith(s):
            matches.append(i)
        elif any(l.startswith(s) for l in i.name.split()):
            matches.append(i)
    if not matches:
        return None
    if len(matches) == 1:
        return matches[0]
    return choose_one(dict(enumerate(matches)))


def parse(s: str):
    """Parse user input"""
    directions = {'n': Dir.N, 's': Dir.S, 'e': Dir.E, 'w': Dir.W, 'nw': Dir.NW, 'ne': Dir.NE, 'sw': Dir.SW,
                  'se': Dir.SE}
    s = s.lower()
    command, rest = s.split()[0], s.partition(" ")[2]
    if command == 'take':
        take(rest)
    elif command == 'quit':
        print('bye!')
        exit(0)
    else:
        print("what?")


# Player commands

def take(s):
    """Attempt to take an object"""
    obj = locate_name(s)
    if obj is None:
        print("You can't see " + s + '!')
    elif not obj.portable:
        print("You can't take that.")
    else:
        pickup_object(obj, current_room())
        print("Taken.")
