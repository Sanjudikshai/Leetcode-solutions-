class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        res=0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res



"""        res = 0
        for i in range(len(heights)):
            h = heights[i]
            l = i
            while l > 0 and heights[l-1] >= h:
                l -= 1
            r = i
            while r < len(heights)-1 and heights[r+1] >= h:
                r += 1
            area = h * (r - l + 1)
            res = max(res, area)
        return res
        """
"""
        stack=[]
        res=0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res """