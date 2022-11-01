class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = []
        idx = 0
        inbound = lambda x: 0 <= x < len(grid[0])
        for i in range(len(grid[0])):
            idx = i
            flag = True
            for j in range(-1, len(grid) - 1):
                if grid[j + 1][idx] == 1:
                    if inbound(idx + 1) and grid[j + 1][idx + 1] == 1:
                        idx += 1
                    else:
                        answer.append(-1)
                        flag = False
                        break
                else:
                    if inbound(idx - 1) and grid[j + 1][idx - 1] == -1:
                        idx -= 1
                    else:
                        answer.append(-1)
                        flag = False
                        break
            if flag:
                answer.append(idx)
        return answer
                