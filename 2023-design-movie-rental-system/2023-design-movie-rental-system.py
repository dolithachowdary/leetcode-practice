from sortedcontainers import SortedList
import collections

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        # For each movie: a sorted list of (price, shop) for unrented copies
        self.unrented = collections.defaultdict(SortedList)
        # Mapping (shop, movie) -> price
        self.price_map = {}
        # Global sorted list of rented copies: (price, shop, movie)
        self.rented = SortedList()
        
        for shop, movie, price in entries:
            self.unrented[movie].add((price, shop))
            self.price_map[(shop, movie)] = price

    def search(self, movie: int) -> list[int]:
        # up to 5 cheapest shops with an unrented copy of movie
        lst = self.unrented.get(movie, [])
        res = []
        for i in range(min(5, len(lst))):
            res.append(lst[i][1])  # shop
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.unrented[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        res = []
        for i in range(min(5, len(self.rented))):
            price, shop, movie = self.rented[i]
            res.append([shop, movie])
        return res


        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()