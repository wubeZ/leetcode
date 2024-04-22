class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        deadset = set(deadends)
        
        queue = deque()
        queue.append(("0000", 0))
        
        if "0000" in deadset:
            return -1
        
        visited.add("0000")
        
        while queue:
            cur, count = queue.popleft()
            
            if cur == target:
                return count
            
            for i in range(len(cur)):
                prev = list(cur)
                nextt = list(cur)
                prev[i] = (int(prev[i]) + 1)
                if prev[i] == 10:
                    prev[i] = 0
                prev[i] = str(prev[i])
                
                nextt[i] = (int(nextt[i]) - 1)
                if nextt[i] == -1:
                    nextt[i] = 9
                nextt[i] = str(nextt[i])
                
                prev = "".join(prev)
                nextt = "".join(nextt)
                if prev not in deadset and prev not in visited:
                    queue.append((prev, count + 1))
                    visited.add(prev)
                if nextt not in deadset and nextt not in visited:
                    queue.append((nextt, count + 1))
                    visited.add(nextt)
                    
        return -1