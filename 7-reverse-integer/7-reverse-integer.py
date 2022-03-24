class Solution:
    def reverse(self, x: int) -> int:
        string = list(str(x))
        string = string[::-1]
        if string[0] == 0:
            string.pop(0)
        if string[-1] == '-':
            string.pop(-1)
            string.insert(0, '-')
        
        result = int("".join(string))
        
        if result >= -pow(2,31) and result <= pow(2, 31)-1:
            return result
        return 0