class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def f(l,r):
            if l>=r: return 0
            m=(l+r)//2
            c=f(l,m)+f(m+1,r)
            j=m+1
            for i in range(l,m+1):
                while j<=r and nums[i]>2*nums[j]: j+=1
                c+=j-(m+1)
            nums[l:r+1]=sorted(nums[l:r+1])
            return c
        return f(0,len(nums)-1)

        