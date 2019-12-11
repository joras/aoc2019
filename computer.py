from collections import deque


class Computer:
    def __init__(self, name, code=[], input=[]):
        self.__name = name
        self.__input = deque(input)
        self.__mem = code[:] + [0]*1000
        self.__ip = 0
        self.__relbase = 0
        self.__stopped = False
        self.__output = None
        self.__outputBuf = []
        self.debug = False

    @property
    def stopped(self):
        return self.__stopped

    @property
    def crashed(self):
        return self.__crashed

    @property
    def output(self):
        return self.__output

    @property
    def outputBuf(self):
        return self.__outputBuf

    def pushInput(self, input):
        self.__input.append(input)
        return self

    def setDebug(self, debug):
        self.debug = debug

    def run(self, untilOutput=False):
        while True:
            instr = self.__mem[self.__ip]
            opcode = instr % 100
            modes = [(instr // 10**i) % 10 for i in range(2, 5)]

            def p(nr):
                if modes[nr] == 1:
                    return self.__mem[self.__ip+1+nr]
                elif modes[nr] == 2:
                    return self.__mem[self.__relbase + self.__mem[self.__ip+1+nr]]
                else:
                    return self.__mem[self.__mem[self.__ip+1+nr]]

            def o(nr):
                if modes[nr] == 2:
                    return self.__relbase + self.__mem[self.__ip+1+nr]
                else:
                    return self.__mem[self.__ip+1+nr]

            if opcode == 1:
                if self.debug:
                    print(self.__name, '&{} = {} + {}'.format(o(2),  p(0), p(1)))

                self.__mem[o(2)] = p(0) + p(1)
                self.__ip += 4
            elif opcode == 2:
                if self.debug:
                    print(self.__name, '&{} = {} * {}'.format(o(2), p(0), p(1)))

                self.__mem[o(2)] = p(0) * p(1)
                self.__ip += 4
            elif opcode == 3:
                inp = self.__input.popleft()
                if self.debug:
                    print(self.__name, '&{} = {}'.format(o(0), inp))

                self.__mem[o(0)] = inp
                self.__ip += 2
            elif opcode == 4:
                self.__output = p(0)
                self.__outputBuf.append(p(0))

                if self.debug:
                    print(self.__name, 'out: {} #(&{})'.format(p(0), o(0)))
                self.__ip += 2

                if untilOutput:
                    return self
            elif opcode == 5:
                if p(0) != 0:
                    if self.debug:
                        print(self.__name, 'ip = {} ({}==0)'.format(p(0), p(1)))
                    self.__ip = p(1)
                else:
                    self.__ip += 3
            elif opcode == 6:
                if p(0) == 0:
                    if self.debug:
                        print(self.__name, 'ip = {} ({}==0)'.format(p(1), p(0)))
                    self.__ip = p(1)
                else:
                    self.__ip += 3
            elif opcode == 7:
                res = 1 if p(0) < p(1) else 0
                if self.debug:
                    print(self.__name, '&{} = {} # ({}<{})'.format(
                        o(2), res, p(0), p(1)))

                self.__mem[o(2)] = res
                self.__ip += 4
            elif opcode == 8:
                res = 1 if p(0) == p(1) else 0
                if self.debug:
                    print(self.__name, '&{} = {} # ({}=={})'.format(
                        o(2), res, p(0), p(1)))

                self.__mem[o(2)] = res
                self.__ip += 4
            elif opcode == 9:
                self.__relbase += p(0)
                if self.debug:
                    print(self.__name, 'relbase = {} # ({})'.format(
                        self.__relbase, p(0)))
                self.__ip += 2
            elif opcode == 99:
                self.__stopped = True
                break
            else:
                self.__stopped = True
                self.__crashed = True
                break
        return self
