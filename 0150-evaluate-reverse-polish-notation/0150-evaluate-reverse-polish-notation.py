class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","*","-","/"]
        for ch in tokens:
            if ch in ops:
                val2 = stack.pop()
                val1 = stack.pop()
                val = 0
                if ch == "+": val = val1 + val2
                elif ch == "-": val = val1 - val2
                elif ch == "*": val = val1 * val2
                else: 
                    val = val1 / val2
                stack.append(int(val))
                
            else:
                stack.append(int(ch))
            
        return stack[0]