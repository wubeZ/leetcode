class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        def check(word1):
            temp = []
            for i in range(len(word1)):
                for idx in range(26):
                    if ord(word1[i]) - 97 != idx:
                        char = word1[i]
                        word1[i] = chr(97+idx)
                        curword = "".join(word1)
                        if curword in wordset and curword not in seen:
                            seen.add(curword)
                            temp.append(curword)
                        word1[i] = char
            return temp
        
        queue = deque([beginWord])
        level = 1
        seen = set()
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if cur == endWord:
                    return level
                queue.extend(check(list(cur)))
                
            level += 1
        
        return 0