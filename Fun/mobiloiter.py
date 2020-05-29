import time

products = ["Product {}".format(i) for i in range(1, 50)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 50)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 50)]
print(customers)

combinations = []


class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        '''self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0'''

    def __getitem__(self, item):
        if item > (len(products) * len(promotions) * len(customers)):
            raise StopIteration()
        else:
            pos_products = item // (len(promotions) * len(customers))
            item %= (len(promotions) * len(customers))
            pos_promotions = item // len(customers)
            item %= len(customers)
            pos_customers = item

            return f'{pos_products} - {pos_promotions} - {pos_customers}'

    '''def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1
        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1
        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration()
        item_to_return = f"{self.current_product} - {self.current_promotion} - {self.current_customer}"
        self.current_customer += 1
        return item_to_return

    def __iter__(self):
        return self'''


def combinator(products, promotions, customers):

    for pr in range(len(products)):
        for po in range(len(promotions)):
            for cu in range(len(customers)):
                yield(f'{pr} - {po} - {cu}')


combinations = Combinations(products, promotions, customers)

'''combinations = iter(combinations)
print(next(combinations))
print(next(combinations))
print(next(combinations))'''

print(combinations[99])
for i in range(70):
    print(combinations[i])
for c in combinations:
    # here an analysis will be done - currently, just nothing happens :)
    pass