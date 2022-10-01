class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in memo: return memo[i]
            if int(s[i]) == 0:
                return 0
            if int(s[i])!= 0 and int(s[i]) < 10:
                res = dfs(i+1)
            if (i+1 < len(s)) and (int(s[i]) == 1 or int(s[i]) == 2 and int(s[i+1]) < 7):
                res += dfs(i+2)
            memo[i] = res
            return memo[i]
        
        return dfs(0)