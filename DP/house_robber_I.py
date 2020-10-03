class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums = [0] + nums
        
        for k in range(2, len(nums)):
            nums[k] = max(nums[k-1], nums[k-2] + nums[k]) 
            
        return nums[-1]