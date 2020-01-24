class Solution:
    def suggestedProducts(self, products, searchWord):

        # O(N logN)
        products.sort()

        results = []

        searchArr = products[::]
        prefix = ""
        for char in searchWord:
            prefix += char

            helper = []

            for product in searchArr:
                if product.startswith(prefix):
                    helper.append(product)

                results.append(helper[:3])
            searchArr = helper

        return results