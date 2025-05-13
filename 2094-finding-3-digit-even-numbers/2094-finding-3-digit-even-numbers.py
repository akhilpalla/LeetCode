class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hashmap = collections.Counter(digits)
        result = []

        for i in range(1, 10):
            if hashmap[i] == 0:
                continue
            hashmap[i] -= 1
            for j in range(10):
                if hashmap[j] == 0: 
                    continue
                hashmap[j] -= 1
                for k in range(0, 10, 2):
                    if hashmap[k] == 0: 
                        continue
                    result.append(i*100 + j*10 + k)
                hashmap[j] += 1
            hashmap[i] += 1
        return result