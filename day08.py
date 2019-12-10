
import base
from PIL import Image, ImageDraw

filedata = base.file_to_string('input/day08.txt')

W = 25
H = 6

layers = []
for i in range(0, len(filedata), W*H):
    layers.append(filedata[i: i+W*H])

minlayer = None
minzeros = 1000
for l in layers:
    zeros = base.countIf(lambda c: c == '0', l)
    if zeros < minzeros:
        minlayer = l
        minzeros = zeros

print('res1',   base.countIf(lambda c: c == '1', minlayer)
      * base.countIf(lambda c: c == '2', minlayer))


img = Image.new('RGBA', (W, H), (127, 127, 127, 0))
draw = ImageDraw.Draw(img)

for y in range(0, H):
    for x in range(0, W):
        color = 2

        for l in layers:
            if l[y*W+x] != '2':
                color = l[y*W+x]
                break

        if color == '1':
            draw.point((x,   y),  (255, 255, 255))
        elif color == '0':
            draw.point((x,   y),  (0, 0, 0))
        else:
            draw.point((x,   y),  (255, 0, 0))


img.show()
