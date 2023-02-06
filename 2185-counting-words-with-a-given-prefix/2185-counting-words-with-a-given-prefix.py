class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(pref)
        
        for word in words:
            if pref == word[:n]:
                count += 1
            
        return count