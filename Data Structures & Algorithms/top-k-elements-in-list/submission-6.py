class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num]+=1

        sort = []
        for key, value in counts.items():
            sort.append([value, key])

        sort.sort()

        res = []
        for i in range(k):
            res.append(sort.pop()[1])

        return res