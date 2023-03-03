class Solution:
    
    def searchRight(self, letters, target):
        left = -1
        right = len(letters)
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if letters[mid] <= target:
                left = mid
            else:
                right = mid
        
        return letters[right] if right != len(letters) else letters[0]
        
        
        
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        return self.searchRight(letters, target)