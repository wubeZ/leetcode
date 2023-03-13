class Solution:
    
    def backtrack(self, index, arr, s, wordDict):
        if index >= len(s):
            self.ans.append(" ".join(arr))
            return 
        
        
        for i in range(index, len(s)):
            val = s[index: i + 1]
            
            if val in wordDict:
                self.backtrack(i + 1, arr + [val], s, wordDict)
            
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        
        self.backtrack(0, [], s, wordDict)
        
        return self.ans