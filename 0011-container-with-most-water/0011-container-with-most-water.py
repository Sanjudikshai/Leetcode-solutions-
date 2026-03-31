class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            max_area = max(max_area, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]: i += 1
            else: j -= 1
        return max_area

"""
        big = 0
        n = len(height) 
        for i in range(n):
            for j in range(i+1, n):
                area = min(height[i], height[j]) * (j - i)
                big = max(big, area)
        return big
        """