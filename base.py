def file_to_string(filename):
    with open(filename, 'r') as file:
        return file.read().strip()


def test(received, expected):
    assert expected == received, 'expected {} got {}'.format(
        expected, received)


def lmap(fn, items):
    return list(map(fn, items))


def ilen(items):
    return sum(1 for _ in items)


def pairwise(items):
    return zip(items, items[1:])


def hasValue(fn, iter):
    return next(filter(fn, iter), False) != False


def countIf(fn, iter):
    return sum(1 for x in iter if fn(x))
