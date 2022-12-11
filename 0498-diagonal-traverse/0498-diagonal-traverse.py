class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i+j].append(mat[i][j])

        ans = []
        c = 0
        for i in diagonals.keys():
            if c < 2:
                ans.extend(diagonals[i])
                c += 1
            else:
                ans.extend(diagonals[i][::-1])
                c = 1
        
        return ans