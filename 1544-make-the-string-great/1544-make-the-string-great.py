class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        def check(first, second):
            if ord(first) == ord(second):
                return False
            one = first.lower() == second
            two = second.lower() == first
            
            return one or two
        
        for i in range(len(s)):
            if stack and check(stack[-1], s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        
        
        return "".join(stack)