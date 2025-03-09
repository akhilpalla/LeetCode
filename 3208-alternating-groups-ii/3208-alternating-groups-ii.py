class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        answer = 0

        colors = colors + colors[:k - 1]

        window = []

        for i in range(len(colors)):
            if len(window) == k:
                answer += 1
                window.pop(0)
            
            if window and colors[i] == window[-1]:
                window.clear()
            window.append(colors[i])
        
        if len(window) == k:
            answer += 1
        
        return answer