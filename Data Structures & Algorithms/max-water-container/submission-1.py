class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        Max = 0
        while l < r:
            w = abs(l - r)
            h = min(heights[l], heights[r])
            Max = max(h*w, Max)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return Max