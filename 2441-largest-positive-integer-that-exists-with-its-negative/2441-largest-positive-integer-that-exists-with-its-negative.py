class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hashmap = dict()
        maxx = -1
        
        for elem in nums:
            if -1*elem in hashmap:
                maxx = max(maxx, abs(elem))    
            hashmap[elem] = 1

        
        return maxx
                    