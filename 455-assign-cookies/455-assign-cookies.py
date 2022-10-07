class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                j += 1
            else:
                i += 1
                j += 1
                count += 1
        
        return count
                
                