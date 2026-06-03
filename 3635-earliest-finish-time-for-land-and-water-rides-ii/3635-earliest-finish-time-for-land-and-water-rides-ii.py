class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        earliest_land_finish = min(s + d for s, d in zip(landStartTime, landDuration))
        earliest_water_finish = min(s + d for s, d in zip(waterStartTime, waterDuration))

        return min(
            min(max(s, earliest_land_finish) + d for s, d in zip(waterStartTime, waterDuration)),
            min(max(s, earliest_water_finish) + d for s, d in zip(landStartTime, landDuration)),
        )