class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sm = 0
        count = 0
        seen = {0: 1}
        for n in nums:
            sm += n
            if sm - k in seen:
                count += seen[sm-k]
            seen[sm] = seen.get(sm, 0) + 1

        return count