class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        val = bisect.bisect_right(letters, target)
        
        return letters[val] if val != len(letters) else letters[0]