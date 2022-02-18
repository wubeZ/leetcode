class Solution:
    
    def inverse(self, n: int):
        if n == 1:
            return 0
        else:
            return 1
        
    def kthGrammar(self, n: int, k: int) -> int:
        middle = pow(2, n-1)//2
        if n == 1:
            return 0
        elif k > middle:
            return self.inverse(self.kthGrammar(n-1, k - middle))
        else:
            return self.kthGrammar(n-1, k)
    
    