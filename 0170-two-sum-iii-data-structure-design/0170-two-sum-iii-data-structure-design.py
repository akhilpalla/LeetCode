class TwoSum:

    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.nums.sort()

    def find(self, value: int) -> bool:
        i = 0
        j = len(self.nums) - 1
        while i < j:
            sum = self.nums[i] + self.nums[j]
            if sum < value:
                i += 1
            elif sum > value:
                j -= 1
            else:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)