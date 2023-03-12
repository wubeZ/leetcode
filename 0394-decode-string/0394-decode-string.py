class Solution:
    
    def solve(self, index, prev_sum, prev_string, s):
        
        while index < len(s):
            while s[index].isdigit():
                prev_sum = prev_sum * 10 + int(s[index])
                index += 1
                
            if s[index] == "[":
                new_index, strings = self.solve(index + 1, 0, "", s)
                prev_string += (strings * prev_sum)
                index = new_index
                prev_sum = 0

            elif s[index] == "]":
                return index, prev_string

            else:
                prev_string += s[index]
            
            index += 1

        return index, prev_string
                    
        
    def decodeString(self, s: str) -> str:
        
        index, final_string = self.solve(0, 0, "", s)
        
        return final_string