class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()                                 #[1,1,2,3]
        for i in range(1,len(nums)):                #[1,5]=>1-4
            if nums[i]==nums[i-1]:                  #nums[1]==nums[1]=> 2nd iteration
                return True
        return False