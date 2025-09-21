class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):

        self.prices = {}

        #Track movies in shops
        self.movies = defaultdict(list)
        self.rented = set()
        for shop, movie, price in entries:
            self.prices[shop, movie] = price
            self.movies[movie].append((price, shop, movie))
        for item in self.movies:
            heapify(self.movies[item])

        #Track rented movies
        self.heap = []
        self.returned = set()

    def search(self, movie: int) -> List[int]:

        #Search for the 5 cheapest shops
        arr = []
        while len(arr) < 5 and self.movies[movie]:
            while self.movies[movie] and self.movies[movie][0] in self.rented:
                self.rented.remove(heappop(self.movies[movie]))
            if self.movies[movie]:
                arr.append(heappop(self.movies[movie]))

        #Return the removed items back to shops
        for item in arr:
            heappush(self.movies[movie], item)

        return [item[1] for item in arr]

    def rent(self, shop: int, movie: int) -> None:
        item = (self.prices[shop, movie], shop, movie)
        self.rented.add(item)
        if item in self.returned:
            self.returned.remove(item)
        else:
            heappush(self.heap, item)
        return

    def drop(self, shop: int, movie: int) -> None:
        item = (self.prices[shop, movie], shop, movie)
        self.returned.add(item)
        if item in self.rented:
            self.rented.remove(item)
        else:
            heappush(self.movies[movie], item)
        return

    def report(self) -> List[List[int]]:

        #Search for the 5 cheapest movies
        arr = []
        while len(arr) < 5 and self.heap:
            while self.heap and self.heap[0] in self.returned:
                self.returned.remove(heappop(self.heap))
            if self.heap:
                arr.append(heappop(self.heap))
        
        #Return the removed items back to the heap
        for item in arr:
            heappush(self.heap, item)

        return [item[1:] for item in arr]        

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()