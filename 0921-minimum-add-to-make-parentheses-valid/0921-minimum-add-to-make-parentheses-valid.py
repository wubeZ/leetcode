class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        closing = { "(" : ")"}
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if stack:
                    if stack[-1] == ")":
                        stack.append(ch)
                    else:
                        stack.pop()
                else:
                    stack.append(ch)
                
        
        return len(stack)
                