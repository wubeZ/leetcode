class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.count = defaultdict(int);
        self.types = [big, medium, small];

    def addCar(self, carType: int) -> bool:
        val = self.count[carType];
        if val >= self.types[carType - 1]:
            return False
        self.count[carType] += 1
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)