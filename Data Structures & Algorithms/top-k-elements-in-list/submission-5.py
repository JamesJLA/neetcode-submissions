class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num]+=1
        
        arr = []
        for key, value in counts.items():
            arr.append([value, key])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
            