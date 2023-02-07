class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        
        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif logs[i] == "../":
                if stack > 0:
                    stack -= 1
            else:
                stack += 1
        
        
        return stack