class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        seen = set()
        counter = Counter(s)
        
        for ch in s:
            while stack and ch not in seen and stack[-1] > ch and counter[stack[-1]] > 0:
                seen.remove(stack[-1])
                stack.pop()
            if ch not in seen:
                stack.append(ch)
                seen.add(ch)
            
            counter[ch] -= 1
        
        
        return "".join(stack)