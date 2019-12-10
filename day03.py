import base
import math

data = base.file_to_string('input/day03.txt')


def parseWire(wireStr):
    return base.lmap(lambda x: (x[0], int(x[1:])), wireStr.split(','))


lines = base.lmap(parseWire, data.splitlines())


def walkWire(wire):
    dirs = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    pos = (0, 0)
    positions = {}
    steps = 0
    for cmd in wire:
        dir = dirs[cmd[0]]
        times = cmd[1]
        for _ in range(times):
            steps += 1
            pos = (pos[0]+dir[0], pos[1]+dir[1])
            if pos not in positions:
                positions[pos] = steps
    return positions


def manhattanFromZero(pos):
    return abs(pos[0]) + abs(pos[1])


line1Pos = walkWire(lines[0])
line2Pos = walkWire(lines[1])

commonPos = set(line1Pos.keys()).intersection(set(line2Pos.keys()))

mahattanDistances = base.lmap(lambda x: manhattanFromZero(x), commonPos)
print('res1', min(mahattanDistances))

wireDistances = base.lmap(lambda x: line1Pos[x] + line2Pos[x], commonPos)
print('res2', min(wireDistances))
