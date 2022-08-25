class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(magazine)
        for i in ransomNote:
            if d[i] >= 1:
                d[i] -= 1
            else:
                return False
        return True