class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = cur_min = 1
        for n in nums:
            cur_max, cur_min = max(n, cur_max * n, cur_min * n), min(n, cur_max * n, cur_min * n)
            res = max(res, cur_max)

        return res