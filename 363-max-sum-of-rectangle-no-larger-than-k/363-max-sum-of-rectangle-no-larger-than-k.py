class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:  return 0

        res = float('-inf')
        M, N = len(matrix), len(matrix[0])


        for i in range(N):
            sums = [0] * M
            for j in range(i, N):
                for r in range(M):
                    sums[r] += matrix[r][j]

                cum_sum = [0]
                cum, max_sum = 0, float('-inf')
                for item in sums:
                    cum += item
                    target = cum - k 
                    left = bisect.bisect_left(cum_sum, target)
                    if left < len(cum_sum):
                        max_sum = max(max_sum, cum - cum_sum[left])
                    bisect.insort(cum_sum, cum)

                res = max(res, max_sum)

        return res