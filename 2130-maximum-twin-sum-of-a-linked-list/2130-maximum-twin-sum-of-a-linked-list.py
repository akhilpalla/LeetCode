# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # S : O(1) T: O(N)
        max_sum = 0
        # delink the middle
        s , f = head , head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        nxt = s.next # start of second half
        s.next = None # delink first half from second half
        prev , curr = None , nxt
        while curr:    # reverse the second half
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        # add each twin sum , maintain the largest only
        while head and prev:
            total = head.val + prev.val
            max_sum = max(max_sum , total)
            head = head.next
            prev = prev.next
        return max_sum
        

        
        