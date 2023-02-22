class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict_pairs = {}
        t_dict_pairs = {}
        
        for i in range(len(s)):
            if s[i] in s_dict_pairs:
                if s_dict_pairs[s[i]] != t[i]:
                    return False
            else:
                s_dict_pairs[s[i]] = t[i]
            
            if t[i] in t_dict_pairs:
                if t_dict_pairs[t[i]] != s[i]:
                    return False
            else:
                t_dict_pairs[t[i]] = s[i]
        
        return True