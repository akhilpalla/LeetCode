class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        points=0
        if currentEnergy>=enemyEnergies[0]:
            haha=sum(enemyEnergies[1:])
            currentEnergy+=haha
            return currentEnergy//enemyEnergies[0]
        else:
            return 0
                
                