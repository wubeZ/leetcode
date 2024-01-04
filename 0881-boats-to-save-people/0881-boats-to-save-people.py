class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        
        left = 0
        right = len(people)-1
        
        count = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                left += 1
            
            count += 1
        
        return count
        