class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        in_bound = lambda x: 0 <= x < len(arr)
        
        queue = deque()
        visited = set()
        queue.append(start)
        visited.add(start)
        
        while queue:
            
            cur = queue.popleft()
            
            if arr[cur] == 0:
                return True
            
            new_cur_right = cur + arr[cur]
            new_cur_left = cur - arr[cur]
             
            if in_bound(new_cur_right) and (new_cur_right) not in visited:
                queue.append(new_cur_right)
                visited.add(new_cur_right)
            if in_bound(new_cur_left) and (new_cur_left) not in visited:
                queue.append(new_cur_left)
                visited.add(new_cur_left)
            
        return False