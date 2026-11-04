class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l + r) // 2
            days_needed = 1
            load = 0

            for weight in weights:
                if load + weight > m:
                    days_needed += 1
                    load = 0
                load += weight

            if days_needed > days:
                l = m + 1
            else:
                r = m

        return l