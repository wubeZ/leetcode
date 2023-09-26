class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        seen = set()
        
        for ch in s:
            while stack and stack[-1] >= ch and ch not in seen and counter[stack[-1]] > 0:
                seen.discard(stack[-1])
                stack.pop()
            
            if ch not in seen:
                stack.append(ch)
                seen.add(ch)
            counter[ch] -= 1
        
              
        return "".join(stack)