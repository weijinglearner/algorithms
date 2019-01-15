import collections

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        presum=[0]
        
        for num in A:
            presum.append((presum[-1]+num)%K)
            
        counter=collections.Counter(presum)
        return sum(v*(v-1)//2 for v in counter.values())
