import base
import math
import operator
from computer import Computer

inputdata = base.file_to_string('input/day10.txt')

asteroids = list()
y = 0
for xs in inputdata.splitlines():
    x = 0
    for point in xs:
        if point == '#':
            asteroids.append((x, y))
        x += 1
    y += 1


def distance(pA, pB):
    return math.sqrt((pA[0]-pB[0])**2 + (pA[1]-pB[1])**2)


def points_on_line(pA, pB, pC):
    return math.isclose(distance(pA, pB) + distance(pB, pC), distance(pA, pC))


def visible_asteroids(source, asteroids):
    res = []
    for dest in asteroids:
        if dest == source:
            continue
        visible = True
        for other in asteroids:
            if other == source or other == dest:
                continue
            if points_on_line(source, other, dest):
                visible = False
                break
        if visible:
            res.append(dest)
    return res


counts = dict()
for source in asteroids:
    visible = visible_asteroids(source, asteroids)
    counts[source] = len(visible)

print('res1:', max(counts.values()))
best_asteroid = max(counts.items(), key=operator.itemgetter(1))[0]


def angle(pA, pB):
    return math.atan2((pB[0] - pA[0]), (pB[1] - pA[1]))


remaining = asteroids[:]
destructions = []
while len(destructions) < 200:
    visible = visible_asteroids(best_asteroid, remaining)
    destroyed_in_order = sorted(
        visible, lambda a: angle(best_asteroid, a), True)

    destructions += destroyed_in_order

    remaining = list(set(remaining) - set(destroyed_in_order))


print('res2:', destructions[199][0]*100+destructions[199][1])
