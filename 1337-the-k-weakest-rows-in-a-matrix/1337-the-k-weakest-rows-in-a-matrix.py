class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        stack = []
        ans = []
        sums = 0
        for i in range(len(mat)):
            sums = sum(mat[i])
            stack.append((sums, i))
            sums = 0
            
        stack.sort()
        
        for i in stack:
            ans.append(i[1])
        
        return ans[:k]