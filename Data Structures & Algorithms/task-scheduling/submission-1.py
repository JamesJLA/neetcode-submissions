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
            time += 1 # add time each run

            if maxHeap: # if task left
                cnt = 1 + heapq.heappop(maxHeap) # run the most frequent task (negative so +1 = fewer runs left)
                if cnt: # if there is a task left not 0
                    q.append([cnt, time + n]) # runs left and the time its cooldown ends

            if q and q[0][1] == time: # front of queue has the earliest ready time 
                heapq.heappush(maxHeap, q.popleft()[0]) # puts the runs it has left back into the heap

        return time