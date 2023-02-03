class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = [w[0]]
        for i in range(1, len(self.w)):
            self.prefix.append(self.prefix[-1] + self.w[i])
        

    def pickIndex(self) -> int:
        random_index = random.randint(1, self.prefix[-1])
        return bisect.bisect_left(self.prefix, random_index)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()