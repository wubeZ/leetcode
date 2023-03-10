class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        count = defaultdict(int)
        self.arr = []
        maxVal = 0
        maxkey = 0
        for i in range(len(self.times)):
            count[self.persons[i]] += 1
            if maxVal <= count[self.persons[i]]:
                maxVal = count[self.persons[i]]
                maxkey = self.persons[i]
            
            self.arr.append(maxkey)
        
    def q(self, t: int) -> int:
        left = -1
        right = len(self.persons)
        
        while left + 1 < right:
            mid = left + (right - left )//2
            
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid
        
        return self.arr[left]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)