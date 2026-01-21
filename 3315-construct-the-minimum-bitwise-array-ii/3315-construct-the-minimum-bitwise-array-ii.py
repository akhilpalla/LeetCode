class Solution :
    def minBitwiseArray( self, nums : List[int] ) -> List[int] :
        return [-1 if number == 2 else number - ((((~number) & (-(~number))) >> 1)) for number in nums]