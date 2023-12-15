class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freqFreq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freqFreq[self.freq[number]] = max(0, self.freqFreq[self.freq[number]] - 1)
        self.freq[number] += 1
        self.freqFreq[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        self.freqFreq[self.freq[number]] = max(0, self.freqFreq[self.freq[number]] - 1)
        self.freq[number] = max(0, self.freq[number] - 1)
        if self.freq[number] == 0:
            del self.freq[number]
        else:
            self.freqFreq[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        
        return self.freqFreq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)