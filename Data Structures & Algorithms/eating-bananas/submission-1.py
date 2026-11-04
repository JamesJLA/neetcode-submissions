class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # so the minimum we can try is 1 and the max will be whatever the largest pile is
        l = 1
        r = max(piles)

        while l < r:
            m = (l + r) // 2 # we will try the middle one always
            hours = 0 # we need to track how long each attempt will take? or for each pile like how long it will take total with this "m"
            for pile in piles:
                hours += math.ceil(pile/ m) # math.ceil(pile / m) will return a rounded up int ex: 3/2 returns 1.something but round up? so we will add 2 hours for that run
            if hours <= h: # if that was too fast or just right
                r = m
            else:
                l = m + 1 # if that run was too slow lets try a higher number

        return r