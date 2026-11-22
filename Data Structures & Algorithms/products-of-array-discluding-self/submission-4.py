class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        n = len(nums)

        left_total = 1
        for i in range(n):
            ans[i] = left_total 
            left_total *= nums[i]


        right_total = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right_total
            right_total *= nums[i]

        return ans