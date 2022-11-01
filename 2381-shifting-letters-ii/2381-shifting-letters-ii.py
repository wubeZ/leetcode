class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = list(s)
        numberline = [0] * (len(s)+1)
        for i in range(len(shifts)):
            start, end, direction = shifts[i]
            if direction == 1:
                numberline[start] += 1
                numberline[end+1] -= 1
            else:
                numberline[start] -= 1
                numberline[end+1] += 1
        prefixsum = [0] * (len(numberline))
        for i in range(len(numberline)):
            prefixsum[i] = prefixsum[i-1] + numberline[i]
        
        for i in range(len(letters)):
            ch_idx = ord(letters[i]) - 97
            ch_idx += prefixsum[i]
            ch_idx = ch_idx%26
            letters[i] = chr(97+ch_idx)
            
            
        return "".join(letters)
            
        
                
            