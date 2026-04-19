class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the current maximum candies
        maximum = max(candies)
        answer = []

        # Check for each kid
        for candy in candies:
            if candy + extraCandies >= maximum:
                answer.append(True)
            else:
                answer.append(False)

        return answer