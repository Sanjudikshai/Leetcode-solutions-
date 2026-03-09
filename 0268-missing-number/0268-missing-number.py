class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        exp_value=n*(n+1)//2
        actual_value=sum(nums)
        return exp_value-actual_value
        