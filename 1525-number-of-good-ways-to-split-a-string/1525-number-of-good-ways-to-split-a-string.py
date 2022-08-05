class Solution:
    def numSplits(self, s: str) -> int:
        left = [0 for i in range(len(s))]
        right =  [0] * len(s)
        visited = set()
        
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
            left[i] = len(visited)
        
        visited = set()
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in visited:
                visited.add(s[i])
            right[i] = len(visited)
        count = 0

        for i in range(len(left) - 1):
            if left[i] == right[i+1]:
                count += 1

        return count