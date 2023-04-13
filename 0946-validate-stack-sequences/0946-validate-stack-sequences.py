class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        i = 0
        while i < len(popped):
            if stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
            else:
                if j < len(pushed):
                    stack.append(pushed[j])
                    j += 1
            if j == len(pushed) and (i < len(popped)) and stack[-1] != popped[i]:
                break
                
        return len(stack) == 0