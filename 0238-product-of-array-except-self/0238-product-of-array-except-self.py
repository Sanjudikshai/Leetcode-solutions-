class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    product*=nums[j]
            answer.append(product)
        return answer


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # prefix product
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # suffix product
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

        