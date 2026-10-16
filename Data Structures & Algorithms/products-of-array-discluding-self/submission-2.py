class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_total = 1
        left_arr = [1] * len(nums)
        for i in range (1,len(nums)):
            left_arr[i] = left_total * nums[i-1]
            left_total *= nums[i-1]
        right_total = 1
        right_arr = [1] * len(nums)
        for i in range (len(nums)-2, -1, -1):
            right_arr[i] = right_total * nums[i+1]
            right_total *= nums[i+1]
        res = [1] * len(nums)
        for i in range (0,len(left_arr)):
            res[i] = left_arr[i] * right_arr[i]
        return res