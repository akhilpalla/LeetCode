class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        degMin = minutes * 6
        degPer = degMin / 360
        degHour = (hour % 12) * 5 * 6 + (30 * degPer)
        angle = abs(degMin - degHour)
        return min(abs(360 - angle), angle)