class Solution(object):
    #provided in ascending order
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        if N==0: return 0
        elif N==1: 
            if citations[0]>0: return 1
            else: return 0
        s, e = 0, N-1
        
        ans = 1
        while s<=e:
            m = (s+e)//2
            if citations[m] >= N-m:
                e = m - 1
            else:
                s = m + 1
            
        return N-s
