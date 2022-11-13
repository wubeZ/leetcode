class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            key = sorted(word)
            ans[str(key)].append(word)
        
        return ans.values()