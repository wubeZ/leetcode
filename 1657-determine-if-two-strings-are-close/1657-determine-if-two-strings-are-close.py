class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        val1 = Counter(word1)
        val2 = Counter(word2)
        
        return val1.keys() == val2.keys() and sorted(val1.values()) == sorted(val2.values())
    