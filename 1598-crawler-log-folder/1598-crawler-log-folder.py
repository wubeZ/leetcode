class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif logs[i] == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(logs[i])
        
        
        return len(stack)