class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for val in num:
            while stack and int(stack[-1]) > int(val) and k>0:
                stack.pop()
                k -= 1
            stack.append(str(val))

        while k:
            stack.pop()
            k -= 1

        answer = "".join(stack)
        
        if not stack:
            return "0"
        else:
            return str(int(answer))
        