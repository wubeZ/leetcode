class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        adjlist = defaultdict(list)
        visited = set()
        visited.add(0)
        
        for i in range(len(rooms)):
            adjlist[i].extend(rooms[i])
        
        def dfs(node):
            for n in adjlist[node]:
                if n not in visited and node != n:
                    visited.add(n)
                    dfs(n)
        
        
        for val in rooms[0]:
            if val not in visited:
                visited.add(val)
                dfs(val)
        
        return True if len(visited) == len(rooms) else False
                