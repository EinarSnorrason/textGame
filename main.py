from room import *
a = Room("Room a")
b = Room("Room b")
c = Room("Room c")
d = Room("Room d")

a.connect(b, Dir.NORTH)
b.connect(c, Dir.EAST)
d.connect(c, Dir.SOUTH)

print(a)
print(a.move(Dir.NORTH))
print(a.move(Dir.NORTH).move(Dir.EAST).move(Dir.NORTH))

