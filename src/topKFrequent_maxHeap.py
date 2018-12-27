import heapq
import collections

class Solution(object):
    '''
    2018-12-27
    max heap method
    '''
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #firstly, count the frequent. 
        #The time complexity is O(n).
        numfreq=collections.defaultdict(int)
        for num in nums:
            numfreq[num]+=1
        
        #secondly, use the max heap with 
        #the size n to heapify the frequent-number tuples
        #The time complexity is O(n)
        heap=[(-1*freq,num) for num,freq in numfreq.items()]
        heapq.heapify(heap)
        
        #thirdly, pop out the top k frequent elements.
        #The time complexity is O(k*log n)
        res=[]
        while(len(res)<k):
            num=heapq.heappop(heap)[1]
            res.append(num)
        return res
