class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        freq = [defaultdict(int) for _ in range(len(words[0]))]
        mod = pow(10, 9) + 7
        memo = {}
        
        for word in words: 
            for i, c in enumerate(word): 
                freq[i][c] += 1
        
        
        def dfs(i, k): 
            
            if (i, k) in memo:
                return memo[(i,k)]
            
            if i == len(target):
                return 1
            if k == len(words[0]):
                return 0
            
            memo[(i, k)] = (freq[k][target[i]] * dfs(i + 1, k + 1)) + dfs(i, k + 1)
            return memo[(i, k)]
        
        ans =  dfs(0, 0)
        
        return ans % mod