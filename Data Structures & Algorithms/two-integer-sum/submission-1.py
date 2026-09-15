class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sums:
                res = [sums[diff], i]
            sums[nums[i]] = i
        return res