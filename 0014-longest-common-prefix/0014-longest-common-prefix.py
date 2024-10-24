class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")
        min_word = ""
        for w in strs:
            if len(w) < min_length:
                min_word = w
                min_length = len(w)
                
            
        
        for i in range(min_length):
            flag = False
            curr = min_word[i]
            for w in strs:
                if w[i] != curr:
                    return w[:i]
        
        
        return min_word