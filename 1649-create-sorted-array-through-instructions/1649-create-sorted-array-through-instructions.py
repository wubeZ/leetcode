from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        array = SortedList()
        mod = 10**9 + 7
        count = 0
        for num in instructions:
            reps = array.count(num)
            before = array.bisect_left(num)
            after = len(array) - reps - before
            count += min(before, after)
            
            array.add(num)
        
        return count % mod