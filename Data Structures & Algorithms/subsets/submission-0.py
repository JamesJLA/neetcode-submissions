class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q = []
        res = []

        def sub(start):
            res.append(q[:])
            for i in range(start, len(nums)):
                q.append(nums[i])
                sub(i + 1)
                q.pop()

        sub(0)
        return res