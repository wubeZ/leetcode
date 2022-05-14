class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        indegree = defaultdict(int)
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        in_bound = lambda x, y : 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
        queue = deque()
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])): 
                for l, r in direction:
                    ni, nj = i + l, j + r
                    if in_bound(ni, nj) and matrix[i][j] < matrix[ni][nj]:
                        indegree[(ni,nj)] += 1
    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if indegree[(i,j)] == 0:
                    queue.append((i,j, 1))
        
        while queue:
            i, j, k = queue.popleft()
            ans = k
            
            for l, r in direction:
                ni, nj = i + l, j + r
                if in_bound(ni,nj) and matrix[i][j] < matrix[ni][nj]:
                    indegree[(ni,nj)] -= 1
                    if indegree[(ni,nj)] == 0:
                        queue.append((ni, nj, k + 1))
        
        return ans