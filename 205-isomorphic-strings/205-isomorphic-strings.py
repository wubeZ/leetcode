class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        i = 0
        while i < len(s):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
            i+= 1
        
        return True
            