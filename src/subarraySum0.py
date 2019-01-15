class Solution(object):
    def findSubarray(self,nums):
        prefixSum=[0]*len(nums)
        # sum(nums[i+1:j+1])=prefixSum[j]-prefixSum[i]
        # sum(nums[i+1:j+1])=0 is equal to find two index i and j
        # such that prefixSum[i]=prefixSum[j] and i!=j
        prefixSum[0]=nums[0]
        d={}
        d[prefixSum[0]]=0
        for i in range(1,len(nums)):
            prefixSum[i]=prefixSum[i-1]+nums[i]
            if(prefixSum[i] in d):
                return True
            else:
                d[prefixSum[i]]=i
        return False


a=Solution()
print("There are subarray in %s such that its sum is 0,"
      " True or False? %s" % ([4, 2, -3, 1, 6],
                           a.findSubarray([4, 2, -3, 1, 6])))
print("There are subarray in %s such that its sum is 0,"
      " True or False? %s" % ([4, 2, 0, 1, 6],
                           a.findSubarray([4, 2, 0, 1, 6])))
print("There are subarray in %s such that its sum is 0,"
      " True or False? %s" % ([-3, 2, 3, 1, 6],
                           a.findSubarray([-3, 2, 3, 1, 6])))

