class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        
        for i in range(len(sequence)-len(word)+1):
            cur = 0
            j = i
            while j+len(word) <= len(sequence) and sequence[j:j+len(word)] == word:
                cur += 1
                j += len(word)
                
            ans = max(ans, cur)
        
        
        return ans