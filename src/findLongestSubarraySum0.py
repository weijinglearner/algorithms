class Solution(object):
    def findLongestSubarraySum0(self,nums):
        prefixSum=[0]*len(nums)
        # sum(nums[i+1:j+1])=prefixSum[j]-prefixSum[i]
        # sum(nums[i+1:j+1])=0 is equal to find two index i and j
        # such that prefixSum[i]=prefixSum[j] and i!=j
        prefixSum[0]=nums[0]
        d={}
        d[prefixSum[0]]=0

        maxLen=0
        for i in range(1,len(nums)):
            prefixSum[i]=prefixSum[i-1]+nums[i]
            if(prefixSum[i] in d):
                if(i-d[prefixSum[i]]>maxLen):
                    maxLen=i-d[prefixSum[i]]
            else:
                d[prefixSum[i]]=i
        return maxLen


a=Solution()
print("Length of the longest 0 sum subarray in %s is %s"
      %([-3, 2, 3, 1, 6],
      a.findSubarray([-3, 2, 3, 1, 6])))
print("Length of the longest 0 sum subarray in %s is %s"
      %([15, -2, 2, -8, 1, 7, 10, 13],
      a.findSubarray([15, -2, 2, -8, 1, 7, 10, 13])))

