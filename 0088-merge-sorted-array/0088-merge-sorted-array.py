class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        S = []
        for i in range(m):
            S.append(nums1[i])
        for j in range(n):
            S.append(nums2[j])
        S.sort()
        for k in range(m + n):
            nums1[k] = S[k]

"""
        s=[]
        for i in nums1[:m]:
            if i>0:
                s.append(i)

        for j in nums2[:n]:
            if j>0:
                s.append(j)
        s.sort()

        for k in range(m+n):
            nums1[k]=s[k]

    """    