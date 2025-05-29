# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        p = head
        while True:
            for _ in range(m-1):
                if p:
                    p = p.next
            if not p: 
                return head
            p2 = p
            for _ in range(n+1):
                if p2:
                    p2 = p2.next
            p.next = p2
            p = p2
            if not p:
                return head