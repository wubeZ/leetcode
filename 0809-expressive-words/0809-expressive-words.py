class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s_arr = []
        
        for i in range(len(s)):
            if s_arr and s_arr[-1][0] == s[i]:
                s_arr[-1][1] += 1
            else:
                s_arr.append([s[i], 1])
                
        ans = 0
        
        for i in range(len(words)):
            word_arr = []
            ptr2 = -1
            ptr1 = 0
            for j in range(len(words[i])):
                if word_arr and word_arr[-1][0] == words[i][j]:
                    word_arr[-1][1] += 1
                else:
                    ptr2 += 1
                    word_arr.append([words[i][j], 1])
                
                if ptr1 >= len(s_arr):
                    break
                    
                if s_arr[ptr1][0] != word_arr[ptr2][0]:
                    diff = s_arr[ptr1][1] - word_arr[ptr2-1][1]
                    if s_arr[ptr1][1] <= 2 and diff != 0:
                        break
                    if diff < 0:
                        break
                    ptr1 += 1
            
            if ptr1 == len(s_arr) - 1:
                diff = s_arr[ptr1][1] - word_arr[ptr2][1]
                if (diff > 0 and s_arr[ptr1][1] > 2) or diff == 0:
                    ans += 1
        
        return ans