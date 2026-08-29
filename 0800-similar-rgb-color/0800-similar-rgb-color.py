class Solution:
    def similarRGB(self, color: str) -> str:
        return '#' + ''.join([
            hex(round(int(color[i:i+2], 16) / 17) * 17)[2:].zfill(2)
            for i in range(1, 7, 2)
        ])