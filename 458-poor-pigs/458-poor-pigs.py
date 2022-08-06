class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        count = 0
        
        while (minutesToTest / minutesToDie + 1) ** count < buckets:
            count += 1
        
        return count