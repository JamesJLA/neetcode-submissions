class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        arr = []
        for key, value in counts.items():
            arr.append([value, key])

        arr.sort()
        
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        
        return res