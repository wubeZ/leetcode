class Solution:
    
    def getCount(self, arr):
        count = 0
        stack = []
        for num in arr:
            if stack and stack[-1][0] == num:
                stack[-1][1] += 1
            else:
                stack.append([num, 1])
        temp = []
        for i in range(len(stack)):
            temp.append(stack[i][0])
            temp.append(str(stack[i][1]))
            
        return temp
                        
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        i = 2
        arr = ["1"]
        while i <= n:
            current = self.getCount(arr)
            arr = current
            i += 1
        return "".join(arr[::-1])