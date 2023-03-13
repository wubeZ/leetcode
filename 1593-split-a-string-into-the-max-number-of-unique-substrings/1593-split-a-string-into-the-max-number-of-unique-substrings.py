class Solution:
    def backtrack(self, index, arr, s):
        if index >= len(s):
            if len(arr) == len(set(arr)):
                return len(arr)
            return 0
        
        res = 0
        
        for i in range(index, len(s)):
            val = s[index : i + 1]
            count = self.backtrack(i + 1, arr + [val], s)
            res = max(count, res)
        
        return res
    
    def maxUniqueSplit(self, s: str) -> int:
        
        return self.backtrack(0, [], s)