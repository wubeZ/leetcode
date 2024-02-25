class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]*(i+1) for i in range(rowIndex + 1)]
        
        for i in range(2, len(ans)):
            for j in range(1, len(ans[i])-1):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
                
        return ans[-1]