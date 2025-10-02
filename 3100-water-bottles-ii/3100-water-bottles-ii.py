class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottle_drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            bottle_drunk += 1       
            empty += 1              
            empty -= numExchange    
            numExchange += 1        

        return bottle_drunk