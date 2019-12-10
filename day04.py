import base
import math
import itertools


def isOk(passwd):
    if base.hasValue(lambda p: p[0] > p[1], base.pairwise(passwd)):
        return False
    return max([base.ilen(g) for _, g in itertools.groupby(passwd)]) > 1


def isOk2(passwd):
    if base.hasValue(lambda p: p[0] > p[1], base.pairwise(passwd)):
        return False
    return 2 in [base.ilen(g) for _, g in itertools.groupby(passwd)]


def countPasswords(start, end, fn):
    return base.countIf(fn, map(str, range(start, end)))


base.test(isOk('111111'), True)
base.test(isOk('223450'), False)
base.test(isOk('123789'), False)

print('res1', countPasswords(145852, 616942, isOk))

base.test(isOk2('111111'), False)
base.test(isOk2('123444'), False)
base.test(isOk2('111122'), True)

print('res2', countPasswords(145852, 616942, isOk2))
