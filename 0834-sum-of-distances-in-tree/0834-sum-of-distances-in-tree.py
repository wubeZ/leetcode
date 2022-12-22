class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)
            
        visited = set([0])
        memo = {}
        ans = [0] * n
        
        def calculate(node):
            
            node_size, node_dis = 0, 0
            
            for childnode in graph[node]:
                if childnode not in visited:
                    visited.add(childnode)
                    new_dis, new_size = calculate(childnode)
                    node_size += new_size
                    node_dis += new_dis
                    
            memo[node] = (node_dis + node_size, node_size)
            
            return (node_dis + node_size, node_size + 1)
        
        def find(node):
            
            for childnode in graph[node]:
                if childnode not in visited:
                    par_dis, par_size = memo[node]
                    child_dis, child_size = memo[childnode]
                    value = par_dis - child_size - 1
                    value += n - (child_size + 1)
                    ans[childnode] = value
                    memo[childnode] = (value, child_size)
                    visited.add(childnode)
                    find(childnode)
            
        calculate(0)
        
        visited = set([0])
        
        find(0)
        ans[0] = memo[0][0]
        return ans
            
            
            
            
            
            
        
        