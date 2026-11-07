class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # so first we need a count of all the letters
        counts = Counter(tasks)
        # then we need to just take the counts for them
        # we want to store them in max heap so that the highest one is first
        # python doesnt have maxheap so we will use a minheap and store using the negation of the count
        maxHeap = [-cnt for cnt in counts.values()]
        # then we still need to heapify this List
        heapq.heapify(maxHeap)

        q = deque() # will store cnt, time + n
        time = 0
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time