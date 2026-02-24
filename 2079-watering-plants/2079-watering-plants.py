class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        step = 0
        value = capacity 
        li = []
        river = 0
        i=0
        while i <n:
            if capacity >= plants[i]:
                capacity = capacity-plants[i]
                step = 1
                li.append(step)
            else:
                river = i
                li.append(river)
                capacity = value 
                capacity = capacity - plants[i]
                step = river +1
                li.append(step)
            i+=1
        return sum(li)