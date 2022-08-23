class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        n = target
        
        while n != 1:
            if n%2 == 0 and maxDoubles > 0:
                n //= 2
                maxDoubles -= 1
                count += 1
            elif n%2 != 0 and maxDoubles > 0:
                n -= 1
                count += 1
            else:
                count += (n - 1)
                n = 1
                
        return count