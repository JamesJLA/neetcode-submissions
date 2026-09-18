class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left_total = 1
        for i in range(len(nums)):
            res[i] = left_total
            left_total = nums[i] * left_total
        right_total = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = right_total * res[j]
            right_total = nums[j] * right_total

        return res