class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        memo = {}
        answer = [0 for i in range(n)]
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        def first_dfs(num, parent):
            val1, val2 = 0, 0
            
            for nei in graph[num]:
                if nei != parent:
                    x, y = first_dfs(nei, num)
                    val1 += x + y
                    val2 += y
            memo[num] = [val1, val2 + 1]   
            return memo[num]
        
        answer[0] = first_dfs(0, -1)[0]
        
        def get_result(num, parent):
            for nei in graph[num]:
                if nei != parent:
                    answer[nei] = answer[num] + n - (2 * memo[nei][1])
                    get_result(nei, num)
                    
        get_result(0, 0)
        return answer