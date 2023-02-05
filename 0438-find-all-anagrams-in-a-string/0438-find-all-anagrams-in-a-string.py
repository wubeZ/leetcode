class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ans = []
        len_s = len(s)
        len_p = len(p)
        word = sorted(p)
        
        for i in range(len_s -len_p + 1):
            if word == sorted(s[i: i+len_p]):
                ans.append(i)
        
        return ans