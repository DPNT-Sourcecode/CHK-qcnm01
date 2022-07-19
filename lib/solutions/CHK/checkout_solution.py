
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
        +------+-------+------------------------+
        | Item | Price | Special offers         |
        +------+-------+------------------------+
        | A    | 50    | 3A for 130, 5A for 200 |
        | B    | 30    | 2B for 45              |
        | C    | 20    |                        |
        | D    | 15    |                        |
        | E    | 40    | 2E get one B free      |
        | F    | 10    | 2F get one F free      |
        | G    | 20    |                        |
        | H    | 10    | 5H for 45, 10H for 80  |
        | I    | 35    |                        |
        | J    | 60    |                        |
        | K    | 80    | 2K for 150             |
        | L    | 90    |                        |
        | M    | 15    |                        |
        | N    | 40    | 3N get one M free      |
        | O    | 10    |                        |
        | P    | 50    | 5P for 200             |
        | Q    | 30    | 3Q for 80              |
        | R    | 50    | 3R get one Q free      |
        | S    | 30    |                        |
        | T    | 20    |                        |
        | U    | 40    | 3U get one U free      |
        | V    | 50    | 2V for 90, 3V for 130  |
        | W    | 20    |                        |
        | X    | 90    |                        |
        | Y    | 10    |                        |
        | Z    | 50    |                        |
        +------+-------+------------------------+
    """
    table_offer = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
    checkout = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
    total = 0
    # First, we read what's in the basket
    for char in skus:
        if char in checkout:
            checkout[char] += 1
        else:
            return -1
    checkout['B'] -= checkout['E'] // 2  # Every 2E bought, we remove a B from the checkout (= free)

    if checkout['F'] > 2:   # Only works if we have at least 3Fs in our basket
        checkout['F'] -= checkout['F'] // 3

    # In case there is less B in our basket than we can get for free
    if checkout['B'] < 0:
        checkout['B'] = 0

    total += checkout['A'] // 5 * 200 + checkout['A'] % 5 // 3 * 130 + checkout['A'] % 5 % 3 * 50 +\
             checkout['B'] // 2 * 45 + checkout['B'] % 2 * 30
    total += sum([checkout[sku] * table_offer[sku] for sku in 'CDEF'])

    print(f"Total of {skus}: {total}")

    return total


def read_item_list():
    table_offer = {}
    file_path = '/'.join(__file__.split('/')[:len(__file__.split('/')) - 1])
    print('__file__:    ', file_path)
    with open(file_path + '/item_list.txt', 'r') as f:
        lines = f.readlines()
        for line in lines[3:len(lines) - 1]:
            line = [elt.strip() for elt in line.strip().split('|') if elt != '']
            print(f"Line is: {line}")
            product, price, special_offers = line
            table_offer[product] = price







