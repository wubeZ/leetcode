from sortedcontainers import SortedList

class SummaryRanges:

    def __init__(self):
        self.intervals = SortedList()

    def addNum(self, value: int) -> None:
        n = len(self.intervals)
        i = self.intervals.bisect((value, math.inf))
        
        lt = self.intervals[i - 1] if 0 <= i - 1 < n else (-inf, -inf)
        rt = self.intervals[i] if 0 <= i < n else (inf, inf)
        
        if lt[0] <= value <= lt[1]: 
            return

        a, b = value, value
        if lt[1] + 1 == value:
            self.intervals.remove(lt)
            a = lt[0]
        if value == rt[0] - 1:
            self.intervals.remove(rt)
            b = rt[1]

        self.intervals.add((a, b))

    def getIntervals(self) -> list[list[int]]:
        return self.intervals
