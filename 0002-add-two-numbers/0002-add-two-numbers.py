# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry_over = 0
        
        while (list1 is not None or list2 is not None) or carry_over:
            current_sum = 0
            if list1 is not None:
                current_sum += list1.val
                list1 = list1.next
            if list2 is not None:
                current_sum += list2.val
                list2 = list2.next
                
            current_sum += carry_over
            carry_over = current_sum // 10
            new_node = ListNode(current_sum % 10)
            current.next = new_node
            current = current.next
        
        return dummy.next

# T = O(max(m,n))
# S = O(max(m,n)) + 1