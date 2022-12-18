class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]* len(temperatures)
        stack = []
        
        for index ,val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                i,v = stack.pop()
                answer[i] = index - i
            stack.append((index,val))
        
        return answer