class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = len(s)
        lt = len(t)
        
        if lt>ls: return ""
        
        alphas = {}
        for c in t:
            alphas[c] = alphas.get(c, 0) + 1
            
        start, end = -1, ls
        
        l,h = 0,-1
        count = len(alphas)

        while end-start>lt-1 and h<ls-1:
            while count>0 and h<ls-1:
                h+=1
                c = s[h]
                if c in alphas:
                    x = alphas[c]
                    alphas[c] = x - 1
                    if x == 1:
                        count-=1
                        
            while count==0:
                if end-start>h-l:
                    start, end = l, h
                    
                c = s[l]
                if c in alphas:
                    x = alphas[c]
                    alphas[c] = x + 1
                    if x == 0:
                        count += 1
                l+=1
                
        if start == -1: return ""
        return s[start:end+1]
