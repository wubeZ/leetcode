class DataStream:

    def __init__(self, value: int, k: int):
        self.arr = []
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if self.value != num:
            self.arr = []
        else:
            self.arr.append(num)
            
        if len(self.arr) >= self.k:
            return True
        
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)