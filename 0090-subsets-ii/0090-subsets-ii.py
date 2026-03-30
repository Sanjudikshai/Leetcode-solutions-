class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def sub(i,subset):
            res.append(subset)
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                sub(j+1,subset+[nums[j]])
        
        sub(0,[])
        return res
        