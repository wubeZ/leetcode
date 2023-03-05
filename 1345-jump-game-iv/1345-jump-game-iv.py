class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        graph = defaultdict(set)
        
        in_bound = lambda i : i >= 0 and i < len(arr)
        
        for i in range(len(arr)):
            graph[arr[i]].add(i)
        
        
        
        seen = set()
        group_seen = set()
        seen.add(0)
        queue = deque()
        queue.append((0, 0))
        
        while queue:
            
            cur_node, level = queue.popleft()
            
            if cur_node == len(arr)-1:
                return level
            
            if in_bound(cur_node - 1) and cur_node - 1 not in seen:
                queue.append((cur_node-1, level + 1))
                seen.add(cur_node - 1)

            if in_bound(cur_node + 1)  and cur_node + 1 not in seen:
                queue.append((cur_node+1, level + 1))
                seen.add(cur_node + 1)
            
            if arr[cur_node] not in group_seen:
                for next_node in graph[arr[cur_node]]:

                    if next_node not in seen:
                        queue.append((next_node, level + 1))
                        seen.add(next_node)
                group_seen.add(arr[cur_node])


                
        