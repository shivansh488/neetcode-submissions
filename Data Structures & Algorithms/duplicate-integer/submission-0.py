class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp=len(list(set(nums)))
        org=len(nums)
        if temp< org:
            return True
        else:
            return False
            
        
        