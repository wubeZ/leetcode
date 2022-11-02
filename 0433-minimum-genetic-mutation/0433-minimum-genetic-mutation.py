class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        def check(word1, word2):
            c = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    c += 1
                if c > 1:
                    return False
            return True
        
        queue = deque([start])
        level = 0
        visited = set()
        
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                
                if cur == end:
                    return level
            
                for i in range(len(bank)):
                    isValid =  check(cur, bank[i])
                    if isValid and bank[i] not in visited:
                        queue.append(bank[i])
                        visited.add(bank[i])
            level += 1
        
        return -1
                
                
                
                
                
        