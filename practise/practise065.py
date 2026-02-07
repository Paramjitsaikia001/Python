import heapq

class solution:
    def solved(self,stones):
        heapq.heapify(stones)
        print(heapq.nlargest(stones))

s=solution()
s.solved([2,7,4,1,8,1])
