class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}

        for word in strs:
            count = [0] * 26
            for i in range(len(word)):
                count[(ord(word[i]) - ord('a'))] += 1
            counts_tup = tuple(count)
            if counts_tup not in counts:
                counts[counts_tup] = []
            counts[counts_tup].append(word)
        
        return list(counts.values())

