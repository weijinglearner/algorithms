class Solution(object):
    '''
    2018-12-25
    '''
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        F=[1]*n
        pointers=[0]*len(primes)
        for i in range(1,n):
            #merge the lists 
            F[i]=min([primes[j]*F[pointers[j]] for j in range(len(primes))])
            #update pointers
            for j in range(len(primes)):
                if(F[i]==primes[j]*F[pointers[j]]):
                    pointers[j]+=1
        return F[-1]
