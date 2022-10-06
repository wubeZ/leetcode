class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)
        
    def binarySearch(self, key, timestamp):
        arr = self.timestamps[key]
        l, r = 0, len(arr)-1
        best = -1
        while l <= r:
            mid = l + (r - l)//2
            if timestamp >= arr[mid][0]:
                best = mid
                l = mid + 1
            else:
                r = mid - 1
        
        if best == -1:
            return ""
        return arr[best][1]
                
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        return self.binarySearch(key, timestamp)
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)