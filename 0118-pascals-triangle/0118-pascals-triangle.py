class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0]*(i+1) for i in range(numRows)]
        for i in range(len(ans)):
            ans[i][0] = 1
            ans[i][-1] = 1
        
        for i in range(2, len(ans)):
            for j in range(1, len(ans[i])-1):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
                
        return ans
        