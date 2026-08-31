class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        prev, distance = head, -1
        while head.next:
            next = head.next
            if head.val > prev.val and head.val > next.val or head.val < prev.val and head.val < next.val:
                if distance == -1:
                    distance = 0
                else:
                    res[0] = distance if res[0] == -1 else min(res[0], distance)
                    res[1] += distance + (1 if res[1] == -1 else 0)
                    distance = 0
            prev, head = head, head.next
            if distance != -1:
                distance += 1
        return res