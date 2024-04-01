"""
Calculate function
"""


def add(x, y):
    """Add x and y and return result"""
    return x + y


def subtract(x, y):
    """Subtract x from y and return value"""
    return y - x


def measure(what, where, num):
    c = timeit.default_timer()
    for _ in range(0, num):
        if what in where:
            pass
    end = timit.default_timer()-c
    return end