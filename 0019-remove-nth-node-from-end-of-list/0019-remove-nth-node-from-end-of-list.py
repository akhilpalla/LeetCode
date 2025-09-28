# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Naive: Find the length and delete in second pass

# Optimal: fast and slow pointer

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)  # Create a dummy node
        dummy.next = head
        fast = dummy
        slow = dummy

        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(n + 1):  # Move first n+1 steps ahead to maintain the gap
            fast = fast.next

        # Move first to the end, maintaining the gap
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next  # Return the new head of the list

# T = N
# S = 1