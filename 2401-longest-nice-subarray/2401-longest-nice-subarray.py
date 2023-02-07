class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_size = 1
        
        queue = deque()
        l = 0
        
        
        def check(queue):
            for i in range(len(queue)):
                for j in range(i + 1, len(queue)):
                    if (queue[i] & queue[j])  != 0:
                        return False
            return True
            
        
        for r in range(len(nums)):
            queue.append(nums[r])
            
            while not check(queue):
                queue.popleft()
                l += 1
                
            max_size = max(max_size, r - l + 1)
            
        return max_size