class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited, cur = set(), ""
        left, window = 0, 0
        ans = []
        while left < len(s):
            cur = ""
            while (left+window) < len(s) and window < 10:
                cur += s[left+window]
                window += 1
            if cur in visited:
                ans.append(cur)
            visited.add(cur)
            window = 0
            left += 1
        
        return list(set(ans))
        