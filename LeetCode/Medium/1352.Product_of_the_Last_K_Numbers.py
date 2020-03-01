class ProductOfNumbers:

    def __init__(self):
        self.prefixProduct = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProduct = [1]
        else:
            self.prefixProduct.append(self.prefixProduct[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.prefixProduct) - 1 < k:
            return 0

        return self.prefixProduct[-1] // self.prefixProduct[-k - 1]