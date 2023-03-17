class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 0 if k == 1 else 1
        
        length = 2 **(n - 1)
        mid = length//2
        
        if k > mid:
            res = self.kthGrammar(n - 1, k - mid)
            if res == 0:
                return 1
            return 0

        return self.kthGrammar(n - 1, k)