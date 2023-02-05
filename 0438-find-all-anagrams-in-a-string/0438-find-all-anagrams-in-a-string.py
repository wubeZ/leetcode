class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ans = []
        len_s = len(s)
        len_p = len(p)
        word = Counter(p)
        
        for i in range(len_s -len_p + 1):
            counter = Counter(s[i:i+len_p])
            if word == counter:
                ans.append(i)
        
        return ans