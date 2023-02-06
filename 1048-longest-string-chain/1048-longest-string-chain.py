class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        counter = {word: 1 for word in words }
    
        ans = 1
        for i in range(len(words)):
            for j in range(len(words[i])):
                word = words[i]
                word = word[:j] + word[j+1:]
                
                if word in counter:
                    counter[words[i]] = max(counter[words[i]], counter[word] + 1)
                    ans = max(ans, counter[words[i]])

        return ans