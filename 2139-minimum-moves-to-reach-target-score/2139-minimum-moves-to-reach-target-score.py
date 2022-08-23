class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        n = target
        
        while n and maxDoubles:
            if n%2 == 0:
                n //= 2
                maxDoubles -= 1
            else:
                n -= 1
            count += 1
            
        return count + n - 1