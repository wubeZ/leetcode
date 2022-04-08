class Solution(object):
    def fib(self, n):
        memo = {0:0,1:1}
        
        def fibonaci(i):
            if i in memo:
                return memo[i]
            memo[i] = fibonaci(i-1) + fibonaci(i-2)
            return memo[i]
        
        return fibonaci(n)
        