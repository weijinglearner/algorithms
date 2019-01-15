class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        #presum(i)=sum_{l=0}^{i-1}A[l]
        presum=0
        
        #In d, the key is the presum, and the 
        #value is the number of indices making the presum
        d={0:1} 
        
        res=0
        for num in A:
            presum=(presum+num)%K
            
            #sum(j)-sum(i)=sum_{l=0}^{j-1}A[l]-sum_{l=0}^{i-1}A[l]
            #=sum_{l=i}^{j-1}A[l]
            if((presum-K)%K in d):
                res+=d[(presum-K)%K]
            
            #update d
            if(presum not in d):
                d[presum]=1
            else:
                d[presum]+=1
        
        return res
