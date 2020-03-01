class Cashier:

    def __init__(self, n: int, discount: int, products, prices):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = {products[i]: prices[i] for i in range(len(products))}
        self.curr = 1

    def getBill(self, product, amount) -> float:
        self.curr %= self.n
        totalBill = 0
        for i in range(len(product)):
            totalBill += (self.prices[product[i]] * amount[i])

        if self.curr == 0:
            totalBill = totalBill - (self.discount * totalBill) / 100
        self.curr += 1
        self.curr %= self.n

        return totalBill
