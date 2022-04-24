class UndergroundSystem:

    def __init__(self):
        self.checkin = defaultdict(list)
        self.time = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t_start = self.checkin[id]
        self.time[(startStation,stationName)].append(t - t_start)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation,endStation)
        count = len(self.time[key])
        
        return sum(self.time[key])/count
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)