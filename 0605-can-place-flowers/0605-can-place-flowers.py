class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        lst = [0] + flowerbed + [0]
        print(lst)

        for i in range(1, len(lst)-1):
            if lst[i] == 0 and lst[i+1] == 0 and lst[i-1] == 0:
                lst[i] = 1 
                n -= 1
        return n <= 0
        