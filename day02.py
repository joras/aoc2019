import base

data = base.file_to_string('input/day02.txt')
data = base.lmap(int, data.split(','))


def compute(input):
    mem = input.copy()
    idx = 0
    while True:
        if mem[idx] == 1:
            mem[mem[idx+3]] = mem[mem[idx+1]] + mem[mem[idx+2]]
            idx += 4
        elif mem[idx] == 2:
            mem[mem[idx+3]] = mem[mem[idx+1]] * mem[mem[idx+2]]
            idx += 4
        elif mem[idx] == 99:
            break
        else:
            print("crash", idx, mem[idx])
            break
    return mem


base.test([30, 1, 1, 4, 2, 5, 6, 0, 99],
          compute([1, 1, 1, 4, 99, 5, 6, 0, 99]))

data[1] = 12
data[2] = 2
print('res1', compute(data)[0])

for noun in range(0, 99):
    for verb in range(0, 99):
        data[1] = noun
        data[2] = verb
        res = compute(data)[0]
        if res == 19690720:
            print('res2', 100*noun+verb)
            exit
