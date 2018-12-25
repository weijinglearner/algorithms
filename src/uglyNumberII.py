class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        F=[0]*(n+1)#F is the list of ugly numbers
        F[0]=0
        F[1]=1
        l2=[1*2]#l2 is the list of 2*F
        l3=[1*3]#l3 is the list of 3*F
        l5=[1*5]#l5 is the list of 5*F

        cur2=0
        cur3=0
        cur5=0
        for i in range(2,n+1):
            #update F, since F is the merge of l2, l3, and l5 except for 0, and 1.
            #So we apply the merging method to update F. 
            #And l2, l3, and l5 is based on F, so the update is simutaneously, 
            #very tricky.
            F[i]=min(l2[cur2],l3[cur3],l5[cur5])

            #update l2, l3, and l5
            l2.append(F[i] * 2)
            l3.append(F[i] * 3)
            l5.append(F[i] * 5)

            #update the pointers to l2, l3, and l5
            if(F[i]==l2[cur2]):
                cur2+=1
            if(F[i]==l3[cur3]):
                cur3+=1
            if(F[i]==l5[cur5]):
                cur5+=1
        return F[n]
