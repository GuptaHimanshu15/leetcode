class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        
        """
        self.J=J
        self.S=S
        l=list(J)
        k=list(S)
        c=0
        for i in range(len(k)):
            if k[i] in l:
                c=c+1
        return c