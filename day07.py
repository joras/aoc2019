import base
import itertools
from computer import Computer

filedata = base.file_to_string('input/day07.txt')
data = base.lmap(int, filedata.split(','))

result = 0
maxsetting = 0
for setting in itertools.permutations([0, 1, 2, 3, 4]):
    c1 = Computer('c1', data, [setting[0], 0]).run()
    c2 = Computer('c2', data, [setting[1], c1.output]).run()
    c3 = Computer('c3', data, [setting[2], c2.output]).run()
    c4 = Computer('c4', data, [setting[3], c3.output]).run()
    c5 = Computer('c5', data, [setting[4], c4.output]).run()

    if c5.output > result:
        result = c5.output
        maxsetting = setting

print('res1:', result, maxsetting)


result = 0
maxsetting = 0

for setting in itertools.permutations([5, 6, 7, 8, 9]):
    c1 = Computer('c1', data, [setting[0]])
    c2 = Computer('c2', data, [setting[1]])
    c3 = Computer('c3', data, [setting[2]])
    c4 = Computer('c4', data, [setting[3]])
    c5 = Computer('c5', data, [setting[4]])

    lastoutput = 0

    while not c5.stopped:
        c1.pushInput(lastoutput).run(True)
        c2.pushInput(c1.output).run(True)
        c3.pushInput(c2.output).run(True)
        c4.pushInput(c3.output).run(True)
        c5.pushInput(c4.output).run(True)
        lastoutput = c5.output

    if c5.output > result:
        result = c5.output
        maxsetting = setting

print('res2:', result, maxsetting)
