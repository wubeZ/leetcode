class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        
        stack = []
        ans = 0
        
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                ans += 1
            stack.append(d)
            
        return ans