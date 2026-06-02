class Solution:
    def earliestFinishTime(self, landStartTime : List[int],  landDuration: List[int],
                                 waterStartTime: List[int], waterDuration: List[int]) -> int:

        mx = lambda x, y: x if x > y else y
        mn = lambda x, y: x if x < y else y

        land1st = reduce(mn, map(add, landStartTime , landDuration ))   
        watr1st = reduce(mn, map(add, waterStartTime, waterDuration))

        waterStartTime = [mx(t, land1st) for t in waterStartTime]       
        landStartTime  = [mx(t, watr1st) for t in landStartTime ]
        
        land1st = reduce(mn, map(add, landStartTime , landDuration ))   
        watr1st = reduce(mn, map(add, waterStartTime, waterDuration))
        
        return mn(land1st, watr1st)