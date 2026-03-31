class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort(); res = set()
        for i in range(len(nums)):
            if i and nums[i]==nums[i-1]: continue
            seen = set()
            for j in range(i+1, len(nums)):
                x = -nums[i]-nums[j]
                if x in seen: res.add((nums[i], x, nums[j]))
                seen.add(nums[j])
        return [list(t) for t in res]




"""
        n = len(nums)
        res = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(three) for three in res]
               """