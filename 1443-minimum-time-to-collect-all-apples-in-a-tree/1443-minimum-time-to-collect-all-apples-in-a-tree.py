class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        def collectApples(node, parent):
            if (node != 0) and len(tree[node]) == 1:
                return int(hasApple[node]) * 2
            
            value = 0
        
            for child in tree[node]:
                if child != parent:
                    value += collectApples(child, node)
            
            if (node != 0) and (hasApple[node] or value > 0):
                value += 2
                
            return value
            
        return collectApples(0, 0)