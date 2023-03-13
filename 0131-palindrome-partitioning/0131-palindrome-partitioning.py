class Solution:
    
    def backtrack(self, index, arr, s):
        if index >= len(s):
            self.ans.append(arr[:])
            return 
        
        for i  in range(index, len(s)):
            val = s[index : i + 1]
            if val == val[::-1]:
                self.backtrack(i + 1, arr + [val], s)
            
    
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        
        self.backtrack(0, [], s)
        
        return self.ans
       