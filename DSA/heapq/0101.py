import heapq

heap=[] #no support tuple

heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,5)
heapq.heappush(heap,2)

print("using heappush: ",heap)


#using heappop
smallest=heapq.heappop(heap)
print("smallest element using heappop: ",smallest)
print("using heappop: ",heap)
