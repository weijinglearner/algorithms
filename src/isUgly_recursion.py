class Solution(object):
    '''2018-12-25
    '''
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def helper(num):
            if(num<=0):
                return False
            if(num==1):
                return True
            
            if(num%2==0):
                return helper(num//2)
            if(num%3==0):
                return helper(num//3)
            if(num%5==0):
                return helper(num//5)
            return False
        
        return helper(num)
