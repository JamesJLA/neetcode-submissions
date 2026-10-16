class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0

        front = 0
        back = len(heights)-1

        while front < back:
            ds = back - front
            ht = min(heights[back] , heights[front])

            mx = max(mx, abs(ds*ht))

            if heights[front] < heights[back]:
                front+=1
            else:
                back-=1

        return mx