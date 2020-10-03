class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        d = sorted(nums)
        sum = 0
        j = 0
        while (j<len(d)):
            sum += d[j]
            j +=2
            
        return sum
            
            