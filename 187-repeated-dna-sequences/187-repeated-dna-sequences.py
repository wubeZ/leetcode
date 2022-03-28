class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited, ans = set(), set()
        left = 0
        
        while left < len(s):
            cur = s[left: left+10]
            
            if cur in visited:
                ans.add(cur)
            
            visited.add(cur)
            left += 1
        
        return list(ans)
        