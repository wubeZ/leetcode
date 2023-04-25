class SmallestInfiniteSet:

    def __init__(self):
        self.visited = [False] * 1002

    def popSmallest(self) -> int:
        for i in range(1, 1002):
            if not self.visited[i]:
                self.visited[i] = True
                return i

    def addBack(self, num: int) -> None:
        self.visited[num] = False
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)