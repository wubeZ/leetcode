class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for ch in ransomNote:
            if ch not in counter or counter[ch] == 0:
                return False
            counter[ch] -= 1
        
        return True