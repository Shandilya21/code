class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original_size = len(nums)
        if len(set(nums)) < original_size:
            return True
        else:
            return False
        