class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        
        set_lst = []
        
        for k in range(0,len(nums) - 2):
            if k > 0 and nums[k] == nums[k -1]:
                continue
            self.find_two_sum(nums, k+1, len(nums) - 1, -nums[k], set_lst)
            
        return set_lst
    
    def find_two_sum(self,nums,left,right,target,results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target,nums[left],nums[right]])
                left +=1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1