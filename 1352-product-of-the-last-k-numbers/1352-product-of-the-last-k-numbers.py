class ProductOfNumbers:

    def __init__(self):
        self.s = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.s = [1] # reset prefix product
        else:
            self.s.append(self.s[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.s) <= k:
            return 0
        else:
            # Calculate the product of the last k integers.
            return self.s[-1] // self.s[-k - 1] 
       
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)