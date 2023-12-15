class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freqFreq = defaultdict(int)

    def add(self, number: int) -> None:
        if number in self.freq:
            self.freqFreq[self.freq[number]] -= 1
            if self.freqFreq[self.freq[number]] == 0:
                del self.freqFreq[self.freq[number]]
            self.freq[number] += 1
            self.freqFreq[self.freq[number]] += 1 
        else:
            self.freq[number] += 1
            self.freqFreq[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            self.freqFreq[self.freq[number]] -= 1
            if self.freqFreq[self.freq[number]] == 0:
                del self.freqFreq[self.freq[number]]
            self.freq[number] -= 1
            if self.freq[number] == 0:
                del self.freq[number]
            else:
                self.freqFreq[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freqFreq:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)