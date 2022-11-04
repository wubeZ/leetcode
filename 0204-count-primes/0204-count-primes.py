class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * (n)
        if n < 2:
            return 0
        
        i = 2
        while i*i <= n:
            if isPrime[i]:
                j = i*i
                while j < n:
                    isPrime[j] = False
                    j += i
            i += 1
            
        isPrime[0] = False
        isPrime[1] = False
        count = 0 
        for val in isPrime:
            if val:
                count += 1
        
        return count
            