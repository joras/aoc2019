import base
from computer import Computer
from PIL import Image, ImageDraw


inputdata = base.file_to_string('input/day11.txt')
code = base.lmap(int, inputdata.split(','))


def paint(code, startcolor=0):
    c = Computer('r', code, [])

    painted = dict()
    pos = (0, 0)
    dir = 0+1j
    painted[pos] = startcolor

    while not c.stopped:
        tcolor = painted.get(pos, 0)
        c.pushInput(tcolor)

        color = c.run(True).output
        direction = c.run(True).output

        painted[pos] = color

        if direction == 1:
            dir *= - 1j
        else:
            dir *= + 1j

        pos = (int(pos[0] + dir.real), int(pos[1] + dir.imag))
    return painted


print('res1:', len(paint(code, 0)))


painted = paint(code, 1)
img = Image.new('RGBA', (200, 200), (127, 127, 127, 0))
draw = ImageDraw.Draw(img)
for p in painted.keys():
    color = painted[p]
    if color == 1:
        draw.point((p[0]+100, -p[1]+100),  (255, 255, 255))
    elif color == 0:
        draw.point((p[0]+100, -p[1]+100),  (0, 0, 0))

img.show()
