class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    hour = str(h)
                    minute = str(m)
                    if m < 10:
                        minute = "0" + minute
                    time = hour + ":" + minute
                    result.append(time)
        
        return result