class Solution(object):
    '''
    2018-12-25
    '''
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        F=[0]*n
        F[0]=1
        n2=2 #the value of current node in l2
        n3=3 #the value of current node in l3
        n5=5 #the value of current node in l5

        cur2=0 #the pointer to the current node in l2
        cur3=0 #the pointer to the current node in l3
        cur5=0 #the pointer to the current node in l5
        for i in range(1,n):
            #update F
            F[i]=min(n2,n3,n5)

            #update the pointers to l2, l3, and l5
            if(F[i]==n2):
                cur2+=1
                n2=F[cur2]*2
            if(F[i]==n3):
                cur3+=1
                n3=F[cur3]*3
            if(F[i]==n5):
                cur5+=1
                n5=F[cur5]*5
        return F[-1]
