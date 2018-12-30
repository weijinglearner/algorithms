class Solution(object):
    '''
    2018-12-29
    tabulation dynamic programming
    '''
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        F=[None]*(len(s)+1)
        F[0]=1
        if(int(s[0])==0):
            F[1]=0
        else:
            F[1]=1

        for i in range(1,len(s)):
            currentDigit=int(s[i])
            previousDigit=int(s[i-1])
            if(previousDigit==0):
                if(currentDigit==0):
                    #...00
                    F[i+1]=0
                else:
                    #...0|2
                    F[i+1]=F[i]
            else:
                if(currentDigit==0):
                    if (previousDigit==1 or previousDigit==2):
                        #...|20
                        F[i+1]=F[i-1]
                    else:
                        #...|30
                        F[i+1]=0
                else:
                    tailTwoDigits=int(s[i-1:i+1])
                    if(tailTwoDigits<=26):
                        #...|12 or ...1|2
                        F[i+1]=F[i-1]+F[i]
                    else:
                        #...3|2
                        F[i+1]=F[i]
        return F[len(s)]
