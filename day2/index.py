from data import input;

# a
horizontal = 0
depth = 0

for tup in input:
    cmd = tup[0]
    if cmd == 'forward':
        horizontal = horizontal + tup[1]
    if cmd == 'down':
        depth = depth + tup[1]
    if cmd == 'up':
        depth = depth - tup[1]

print(f'horizontal {horizontal}')
print(f'depth {depth}')

print(horizontal*depth)

# b
horizontal = 0
depth = 0
aim = 0

for tup in input:
    cmd = tup[0]
    if cmd == 'forward':
        horizontal = horizontal + tup[1]
        depth = depth + (aim * tup[1])
    if cmd == 'down':
        aim = aim + tup[1]
    if cmd == 'up':
        aim = aim - tup[1]

print(f'horizontal {horizontal}')
print(f'depth {depth}')

print(horizontal*depth)
