class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(":")", "{":"}", "[":"]"}
        
        for bracket in s:
            if bracket in d:
                stack.append(bracket)
            else:
                if stack and stack[-1] in d and d[stack[-1]] == bracket:
                    stack.pop()
                else:
                    return False
        
        return False if stack else True
            