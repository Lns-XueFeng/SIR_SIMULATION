from vector import Vector
import random

position = Vector(
    random.randrange(0, 400),
    random.randrange(0, 400)
)

target = position.copy()

print(position.x, position.y)
print(target.x, target.y)
print(position == target)
