class Solution(object):
    '''2018-12-25
    '''
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num<1):
            return False

        if (num == 1):
            return True

        while (num > 1):
            ugly = False
            for p in [2, 3, 5]:
                if (num % p == 0):
                    num = num / p
                    ugly = True
                    break
            if (ugly == False):
                return False
        return True


a=Solution()
print(a.isUgly(2147483648))
