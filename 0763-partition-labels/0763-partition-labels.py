class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        lastOccurrence = {c: i for i, c in enumerate(s)}
        partitions = []
        start = 0
        end = 0
        for i in range(0, n):
            end = max(end, lastOccurrence[s[i]])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        return partitions        