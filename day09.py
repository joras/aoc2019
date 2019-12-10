import base
from computer import Computer

filedata = base.file_to_string('input/day09.txt')
code = base.lmap(int, filedata.split(','))

c = Computer('c', code, [1])
c.run()
print('res1:', c.outputBuf[-1])

c = Computer('c', code, [2])
c.run()

print('res2:', c.outputBuf[-1])
