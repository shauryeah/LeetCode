class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        heap=[]
        for x in stones:
            heap.append(-x)
        heapq.heapify(heap)
        while(len(heap)>1):
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            if(x!=y):
                heapq.heappush(heap,-abs(x-y))
        if(len(heap)==0):
            return 0
        return -heap[0]
            