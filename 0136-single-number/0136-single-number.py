class Solution:
    def singleNumber(self, nums):
        s=set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return s.pop()
# class Solution:
#     def singleNumber(self, nums):
#         result=0
#         for num in nums:
#             result=result^num
#         return result 
          