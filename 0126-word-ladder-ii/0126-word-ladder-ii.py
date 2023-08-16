class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        graph = defaultdict(int)
        wordlist = set(wordList)
        if endWord not in wordlist:
            return []
        
        shortest_path = float("inf")
        graph[endWord] = 1
        queue = deque([(endWord, 1)])
        
        while queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i+1:]
                    if (next_word in wordlist or (next_word == beginWord)) and next_word not in graph:
                        if next_word == beginWord:
                            shortest_path = min(shortest_path, length + 1)
                            graph[next_word] = length + 1
                            break
                        
                        graph[next_word] = length + 1
                        queue.append([next_word, length + 1])
        
        
        ans = []
        queue = deque([[beginWord]])
        
        while queue:
            arr = queue.popleft()
            word = arr[-1]
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in graph and graph[next_word] + len(arr) <= shortest_path:
                        if next_word == endWord:
                            ans.append(arr + [next_word])
                            break
                        queue.append(arr + [next_word])
                        
        return ans
                        
        