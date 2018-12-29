class Solution(object):
    '''
    2018-12-29
    Backtracking method, but TLE, the time complexity is O(2^n) for 
    the worst case.
    '''
    def dfs(self,s,solution,res):
        if(len(s)==0):
            if(0<int(solution[-1])<=26):
                res[0]+=1
        elif(len(s)==1):
            if(s[0]!="0"):
                self.dfs("",solution+[s[0]],res)
        else:
            if(s[0]!="0"):
                self.dfs(s[1:],solution+[s[0]],res)
                if(1<=int(s[0:2])<=26):
                    self.dfs(s[2:],solution+[s[0:2]],res)
                
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=[0]#the number of decoding ways
        solution=[]
        self.dfs(s,solution,res)
        return res[0]
