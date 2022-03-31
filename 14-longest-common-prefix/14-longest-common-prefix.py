class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        tag = False
        flag = []
        if len(strs) == 0:
            return result
        
        for index in range(len(min(strs))):
            char = strs[0][index]
            for string in strs:
                if string[index] == char:
                    tag = True
                flag.append(tag)
                tag = False
            if all(flag):        
                result += char
            else:
                break
                
        return result