class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = Counter(tasks)
        freq = [val for val in arr.values()]
        freq.sort()
        maxNum = max(freq)
        final = (maxNum-1) * (n+1)
        count = 0
        for v in freq:
            if v == maxNum:
                count += 1
        result = max(final + count , len(tasks))        
        return result
    