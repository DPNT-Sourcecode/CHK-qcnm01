
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    +------+-------+----------------+
    | Item | Price | Special offers |
    +------+-------+----------------+
    | A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
    | D    | 15    |                |
    +------+-------+----------------+
    """
    table_offer = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    checkout = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    total = 0
    # First, we read what's in the basket
    for char in skus:
        if char in checkout:
            checkout[char] += 1
        else:
            return -1
    total += checkout['A'] // 3 * 130 + checkout['A'] % 3 * 50 +\
             checkout['B'] // 2 * 45 + checkout['B'] % 2 * 30
    total += checkout['C'] * 20 + checkout['D'] * 15

    return total

