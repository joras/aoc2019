import base

data = base.file_to_string('input/day05.txt')
data = base.lmap(int, data.split(','))


def compute(code, input, debug=False):
    mem = code.copy()
    output = []
    idx = 0

    while True:
        instr = mem[idx]
        opcode = instr % 100
        modes = [(instr // 10**i) % 10 == 1 for i in range(2, 5)]

        def p(nr, forceValue=False):
            if forceValue or modes[nr]:
                return mem[idx+1+nr]
            else:
                return mem[mem[idx+1+nr]]

        if opcode == 1:
            if debug:
                print('&{} = {} + {}'.format(p(2, True),  p(0), p(1)))

            mem[p(2, True)] = p(0) + p(1)
            idx += 4
        elif opcode == 2:
            if debug:
                print('&{} = {} * {}'.format(p(2, True), p(0), p(1)))

            mem[p(2, True)] = p(0) * p(1)
            idx += 4
        elif opcode == 3:
            if debug:
                print('&{} = {}'.format(p(0, True), input))

            mem[p(0, True)] = input
            idx += 2
        elif opcode == 4:
            output.append(p(0))

            if debug:
                print('out: {} #(&{})'.format(p(0), p(0, True)))
            idx += 2
        elif opcode == 5:
            if p(0) != 0:
                if debug:
                    print('ip = {} ({}==0)'.format(p(0), p(1)))
                idx = p(1)
            else:
                idx += 3
        elif opcode == 6:
            if p(0) == 0:
                if debug:
                    print('ip = {} ({}==0)'.format(p(1), p(0)))
                idx = p(1)
            else:
                idx += 3
        elif opcode == 7:
            res = 1 if p(0) < p(1) else 0
            if debug:
                print('&{} = {} # ({}<{})'.format(
                    p(2, True), res, p(0), p(1)))

            mem[p(2, True)] = res
            idx += 4
        elif opcode == 8:
            res = 1 if p(0) == p(1) else 0
            if debug:
                print('&{} = {} # ({}=={})'.format(
                    p(2, True), res, p(0), p(1)))

            mem[p(2, True)] = res
            idx += 4
        elif opcode == 99:
            break
        else:
            print("crash", idx, mem[idx])
            break
    return output, mem


print('res1', compute(data, 1)[0][-1])
print('res2', compute(data, 5)[0][-1])
