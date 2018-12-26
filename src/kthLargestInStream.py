import heapq

class KthLargest(object):
    '''
    2018-12-26
    '''
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        #self.array is the min heap
        self.heap=nums
        heapq.heapify(self.heap)
        self.k=k
        while(len(self.heap)>k):
            heapq.heappop(self.heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if(len(self.heap)<self.k):
            heapq.heappush(self.heap,val)
        else:
            if(val>self.heap[0]):
                #update min heap
                heapq.heappop(self.heap)
                heapq.heappush(self.heap,val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
