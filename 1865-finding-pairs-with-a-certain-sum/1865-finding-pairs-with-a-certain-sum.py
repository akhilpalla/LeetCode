class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.value_nums2 = {}

        for i,j in enumerate(nums2):
            if j in self.value_nums2:
                self.value_nums2[j]+=1
            else:
                self.value_nums2[j]=1
            
        

    def add(self, index: int, val: int) -> None:
        num_to_add_to = self.nums2[index]
        self.nums2[index]+=val
        self.value_nums2[num_to_add_to] -=1
        changed_value = num_to_add_to+val
        if changed_value in self.value_nums2:
            self.value_nums2[changed_value]+=1
        else:
            self.value_nums2[changed_value]=1

    
    def count(self, tot: int) -> int:
        ans = 0
        for i in self.nums1:
            to_find = tot-i
            if to_find in self.value_nums2:
                ans+=self.value_nums2[to_find]
        return ans
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)