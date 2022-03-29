class Solution:
    def findval(self, d):
        m_key = 0
        m_val = 0
        for k,v in d.items():
            if v > m_val:
                m_key = k
                m_val = v
        return (m_key,m_val)
        
    def minimumOperations(self, nums: List[int]) -> int:
        even_dict, odd_dict = defaultdict(int), defaultdict(int)
        
        for i in range(len(nums)):
            if i%2 == 0:
                even_dict[nums[i]] += 1
            else:
                odd_dict[nums[i]] += 1
                
        even_val = self.findval(even_dict)
        odd_val = self.findval(odd_dict)
        
        if  even_val[0] != odd_val[0]:
            return len(nums) - odd_val[1] - even_val[1]
        
        del even_dict[even_val[0]]
        del odd_dict[odd_val[0]]
        
        even_val2 = self.findval(even_dict)
        odd_val2 = self.findval(odd_dict)
        
        if even_val[1] + odd_val2[1] > odd_val[1] + even_val2[1]:
            return len(nums) - even_val[1] - odd_val2[1]
        
        return len(nums) - odd_val[1] - even_val2[1]
        
        