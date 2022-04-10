class Solution(object):
    def calPoints(self, ops):
        stack = []
        
        for i in ops:
            if i == "+":
                x = stack.pop()
                z = x + stack[-1]
                stack.append(x)
                stack.append(z)
            elif i == "D":
                stack.append(stack[-1]*2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        
        return sum(stack)