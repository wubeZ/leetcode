class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_dict = {order[i]:i for i in range(len(order)) }
        
        def compareWords(word1, word2):
            length = min(len(word1), len(word2))
            for i in range(length):
                if order_dict[word1[i]] < order_dict[word2[i]]:
                    return True
                elif order_dict[word1[i]] > order_dict[word2[i]]:
                    return False
            return len(word1) <= len(word2)
                
        for i in range(1, len(words)):
            isValid = compareWords(words[i-1], words[i])
            if not isValid:
                return False
            
        return True
            