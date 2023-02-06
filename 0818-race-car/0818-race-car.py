class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque()
        
        queue.append((0, 1, 0))
        
        while queue:
            cur_pos, cur_speed, level = queue.popleft()
            
            if cur_pos == target:
                return level
            
            new_pos = cur_pos + cur_speed
            queue.append((new_pos, cur_speed * 2, level + 1 ))
            
            if new_pos > target and cur_speed > 0:
                queue.append((cur_pos, -1, level + 1))
            if new_pos < target and cur_speed < 0:
                queue.append((cur_pos, 1, level + 1))
            