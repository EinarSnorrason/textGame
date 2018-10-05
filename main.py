from actions import *
a = Room("Room a", objects=[Item("big box", "a big brown box", portable=False),
                            Item("small box", "a small box", portable=True),
                            Item("clock", "a big grandfather clock", portable=False)])
b = Room("Room b")
c = Room("Room c")
d = Room("Room d")

player.room = a

connect(a, b, Dir.N)
connect(b, c, Dir.E)
connect(d, c, Dir.S)

print(a)
print(current_room())

print(locate_name("box"))