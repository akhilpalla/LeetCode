class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.availableNumbers = set(i for i in range(maxNumbers))

    def get(self) -> int:
        if len(self.availableNumbers) == 0:
            return -1
        else: 
            return self.availableNumbers.pop()

    def check(self, number: int) -> bool:
        return number in self.availableNumbers

    def release(self, number: int) -> None:
        self.availableNumbers.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)