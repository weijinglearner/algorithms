class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum=0 #presum(i)=sum_{l=0}^{i-1}nums[i]

        # key is presum, value is the number of current indices making
        # the presum.
        d = {0:1}

        res=0
        for num in nums:
            presum+=num
            if(presum-k in d):
                res+=d[presum-k]
            #update d
            if(presum not in d):
                d[presum]=1
            else:
                d[presum]+=1

        return res
