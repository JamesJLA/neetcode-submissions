class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 # must be last valid index ex: [1] r would be out of bounds using len(nums) = 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: # left half is sorted
                if nums[l] <= target < nums[m]: # target is within l and m
                    r = m - 1 
                else: # target is on other side
                    l = m + 1
            else: # right half is sorted
                if nums[r] >= target > nums[m]: # target is within m and r
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

