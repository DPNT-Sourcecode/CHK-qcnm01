
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    table_offer, for_special_offers, get_special_offers, any_special_offers = read_item_list(5)
    checkout = {f"{char}": 0 for char in table_offer}
    total = 0
    # First, we read what's in the basket
    for char in skus:
        if char in checkout:
            checkout[char] += 1
        else:
            return -1

    # First, we remove "free products"
    for product, qty in checkout.items():
        product_get_offers = {get_number(elt): free for elt, free in get_special_offers.items() if product in elt}
        for qty_req, free_p in product_get_offers.items():
            checkout[free_p] -= checkout[product] // (qty_req + int(free_p == product))
            if checkout[free_p] < 0:
                checkout[free_p] = 0

    # Then, we do "any" offers:
    for offer in any_special_offers:
        qty, products, price = offer
        checkout_qty = sum([checkout[product] for product in products])

        if checkout_qty >= qty:
            # We take the most expensive ones in priority:
            prices = sorted([(product, table_offer[product]) for product in products], reverse=False, key=lambda x: x[1])
            nb_offers = checkout_qty // qty
            total += nb_offers * price

            # We keep the cheapest products
            nb_products_left = checkout_qty % qty
            for product, _ in prices:
                if nb_products_left > 0:
                    if checkout[product] >= nb_products_left:
                        checkout[product] = nb_products_left
                        nb_products_left = 0
                    else:
                        nb_products_left -= checkout[product]
                else:
                    checkout[product] = 0

    # Then, we apply discounts
    for product, qty in checkout.items():
        product_for_offers = sorted([get_number(elt) for elt in for_special_offers if product in elt], reverse=True)
        if product_for_offers:
            for qty in product_for_offers:
                total += checkout[product] // qty * for_special_offers[f"{qty}{product}"]
                checkout[product] = checkout[product] % qty

    total += sum([checkout[sku] * table_offer[sku] for sku in table_offer if checkout[sku] >= 0])

    return total


def get_number(elt):
    """ Input like 10H, returns 10"""
    # print(f"elt: {elt}")
    buff = ''
    for i in elt:
        if i in '0123456789':
            buff += i
    # print(f"nd: {int(buff)}")
    return int(buff)


def read_item_list(nb_round):
    """
    Reads file in item_list_r4.txt containing the products, their price and their offers to build talbe_offer and
    special_offer_lists.
    """
    table_offer = {}
    for_special_offer_list = {}
    get_special_offer_list = {}
    any_special_offer_list = []
    file_path = '/'.join(__file__.split('/')[:len(__file__.split('/')) - 1])

    with open(file_path + f'/item_list_r{nb_round}.txt', 'r') as f:
        lines = f.readlines()
        for line in lines[3:len(lines) - 1]:    # First 3 lines are for aesthetics and so is the last one
            line = [elt.strip() for elt in line.strip().split('|') if elt != '']
            # print(f"Line is: {line}")
            product, price, special_offers = line
            table_offer[product] = int(price)

            if 'any' in special_offers:
                offer = special_offers.split(' ')
                qty = int(offer[2])
                products = offer[4][1:len(offer[4]) - 1].split(',')
                price = int(offer[-1])

                if (qty, products, price) not in any_special_offer_list:
                    any_special_offer_list.append((qty, products, price))
                # print(f'qty: {qty}\nproducts: {products}')

            else:
                offers = [elt.strip() for elt in special_offers.split(',')]
                for offer in offers:
                    if "for" in offer:
                        product_o, price_o = [elt.strip() for elt in offer.split('for')]
                        for_special_offer_list[product_o] = int(price_o)
                    elif 'get' in offer:
                        product_o, free_product = [elt.strip() for elt in offer.split('get one')]
                        get_special_offer_list[product_o] = free_product[0]

    # print(f"for offer: {for_special_offer_list}")
    # print(f"get offer: {get_special_offer_list}")
    # print(f"any offer: {any_special_offer_list}")

    return table_offer, for_special_offer_list, get_special_offer_list, any_special_offer_list



