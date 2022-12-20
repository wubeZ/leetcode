class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        
        queue = deque()
        visited.add(0)
        for node in rooms[0]:
            queue.append(node)
            visited.add(node)
        
        while queue:
            
            cur = queue.popleft()
            
            for i in range(len(rooms[cur])):
                new_node = rooms[cur][i]
                if new_node not in visited:
                    queue.append(new_node)
                    visited.add(new_node)
        
        return len(visited) == len(rooms)