class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        stack2 = [*popped[::-1]]
        
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack2 and stack[-1] == stack2[-1]:
                stack.pop()
                stack2.pop()

        if stack:
            return False
        else:
            return True
                
            