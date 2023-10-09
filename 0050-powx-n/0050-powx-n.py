class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n %2 == 0:
            half_res = self.myPow(x, n//2)
            return half_res * half_res
        else:
            half_res = self.myPow(x, (n-1) //2)
            
            return half_res * half_res * x
        
        