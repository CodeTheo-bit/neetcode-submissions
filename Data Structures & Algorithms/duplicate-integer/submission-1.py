class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i in nums:
            hm[i] = hm.get(i,0)+1
        
        for val in hm.values():
            if val>1:
                return True
        else:
            return False