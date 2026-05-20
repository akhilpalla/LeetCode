class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hmapA = defaultdict(int)
        hmapB = defaultdict(int)
        ans = []
        count = 0
        for i in range(len(A)):
            hmapA[A[i]] += 1
            hmapB[B[i]] += 1
            if A[i]==B[i]:
                count += 1
                print(count)
                ans.append(count)
                continue
            if A[i] in hmapB:
                count += 1
            if B[i] in hmapA:
                count += 1
            print(count)
            ans.append(count)
        print(ans)
        return ans

            
        