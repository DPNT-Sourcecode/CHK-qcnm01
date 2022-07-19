# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if 0 <= x <= 100 and 0 <= y <= 100:
        return x + y
    else:
        raise Exception("Error: x and y are not within the authorized range.")
