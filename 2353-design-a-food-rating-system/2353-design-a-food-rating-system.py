class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.m = defaultdict(list)
        self.removed = defaultdict(list)
        self.food_cuisine_map = {}
        self.food_rating = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            heapq.heappush(self.m[cuisine], (-rating, food))
            self.food_cuisine_map[food] = cuisine
            self.food_rating[food] = rating
        

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine_map[food]
        heapq.heappush(self.m[cuisine], (-newRating, food))
        previous_rating = self.food_rating[food]
        heapq.heappush(self.removed[cuisine], (-previous_rating, food))
        self.food_rating[food] = newRating         

    def highestRated(self, cuisine: str) -> str:
        while self.removed[cuisine] and self.m[cuisine][0][0] == self.removed[cuisine][0][0] and self.m[cuisine][0][1] == self.removed[cuisine][0][1]:
            heapq.heappop(self.m[cuisine])
            heapq.heappop(self.removed[cuisine])

        return self.m[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)