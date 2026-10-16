class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            front = i+1
            back = len(nums)-1
            while front < back:
                if nums[front] + nums[back] + nums[i] < 0:
                    front+=1
                    continue
                if nums[front] + nums[back] + nums[i] > 0:
                    back-=1
                    continue
                if nums[front] + nums[back] + nums[i] == 0:
                    res.append([nums[front], nums[i], nums[back]])
                    front+=1
                    back-=1

                    while front < back and nums[front] == nums[front-1]:
                        front+=1
                    while front < back and nums[back] == nums[back+1]:
                        back-=1

        return res