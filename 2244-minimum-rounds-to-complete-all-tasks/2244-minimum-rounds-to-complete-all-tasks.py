class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        values = list(counter.values())
            
        ans = 0
        for val in values:
            if val <= 1:
                return -1
            
            ans += (val + 2) // 3
        
        
        return ans