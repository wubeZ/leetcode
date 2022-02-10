class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isalnum() or i == '[':
                stack.append(i)
            else:
                ans = ""
                num = ""
                while not stack[-1].isdigit():
                    if stack[-1] != '[':
                        ans = stack[-1] + ans
                    stack.pop()
                
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num 
                
                stack.append(ans * int(num))
        
        return "".join(stack)