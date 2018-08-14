class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pmap = {}
        for c in p:
            if c in pmap:
                pmap[c]+=1
            else:
                pmap[c]=1
        
        S = len(s)
        P = len(p)
        
        # to keep note of number of chars missing from window
        counter = len(pmap)
        
        # window, at beginning is length 0, we must build the window
        start, end = 0, 0
        ans = []
        
        while end<S:
            # print(start, end, counter)
            if s[end] in pmap:
                pmap[s[end]] -= 1
                if pmap[s[end]] == 0: 
                    counter -= 1
                    
            # increase the size of window
            end += 1
            
            # when window has all chars of p
            while counter == 0:
                # check if valid window
                if end-start == P:
                    ans.append(start)
                    
                if s[start] in pmap:
                    pmap[s[start]] += 1
                    # only increase counter if first char in p and missing from next window
                    if pmap[s[start]] > 0:
                        counter += 1
                    
                # contract the window from the start
                start+=1
                
        return ans
