import heapq

class Solution(object):
    '''
    2018-12-27
    '''
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #firstly, count the frequent. 
        #The time complexity is O(n).
        numfreq=dict()
        for num in nums:
            if(num not in numfreq):
                numfreq[num]=1
            else:
                numfreq[num]+=1
        
        #secondly, use the min heap with 
        #the fixed size k to get the top k frequent
        #numbers. The time complexity is O(n * log k)
        heap=[]
        for num in numfreq:
            freq=numfreq[num]
            if(len(heap)<k):
                heapq.heappush(heap,(freq,num))
            else:
                if(freq>heap[0][0]):
                    heapq.heappop(heap)
                    heapq.heappush(heap,(freq,num))
        
        #thirdly, output the result from the min heap.
        #The time complexity is O(k * log k).
        res=[]
        while(heap):
            num=heapq.heappop(heap)[1]
            res.append(num)
        res.reverse()
        return res
