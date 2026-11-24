class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0

        for num in nums:
            if num == 0:
                zeros += 1
            if num == 1:
                ones += 1
            if num == 2:
                twos += 1

        i = 0
        while zeros:
            nums[i] = 0
            i += 1
            zeros -= 1

        while ones:
            nums[i] = 1
            i += 1
            ones -= 1
        
        while twos:
            nums[i] = 2
            i += 1
            twos -= 1