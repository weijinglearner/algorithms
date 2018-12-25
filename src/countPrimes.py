import math

class Solution(object):
    '''2018-12-15
    '''
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<=1):
            return 0
        #primeFlags[i]=True means the number i is a prime number.
        primeFlags=[True]*(n+1) 
        primeFlags[0]=False
        primeFlags[1]=False
        
        for p in range(2,int(math.sqrt(n))+1):
            if(primeFlags[p]==True):
                for multiplier in range(2,n//p+1):
                    primeFlags[p*multiplier]=False
        return sum(primeFlags[:-1])

    def test(self):
        print("n={0}, output={1}, expected={2}".format(5,self.countPrimes(5),2))
        print("n={0}, output={1}, expected={2}".format(10,self.countPrimes(10),4))
        
a=Solution()
a.test()
