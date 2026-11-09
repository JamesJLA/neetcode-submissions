class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        best = nums[0]

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            best = max(best, cur)

        return best