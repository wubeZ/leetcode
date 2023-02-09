class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        counter = defaultdict(set)
        
        for names in ideas:
            counter[names[0]].add(tuple(names[1:]))
        
        res = 0
        for ch1, word1 in counter.items():
            for ch2, word2 in counter.items():
                same = len(word1 & word2)
                res += (len(word1) - same) * (len(word2) - same)
        
        return res