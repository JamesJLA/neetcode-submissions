class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)

        res = ""
        while len(heap) >= 2:
            count, char = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)

            res += char
            res += char2

            if count + 1 < 0:
                heapq.heappush(heap, (count + 1, char))
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, char2))

        if heap:
            count, char = heap[0]

            if count < -1:
                return ""
            res += char

        return res