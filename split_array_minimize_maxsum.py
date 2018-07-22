class Solution:
    def checkAcceptable(self, s, nums, m):
        total = 0
        count = 1
        # counting subarrays of sum == s or lower
        for n in nums:
            total += n
            if total>s:
                total = n
                count+=1
                # if count exceeds m, this is unacceptable
                if count>m: return False
                
        return True
        
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        largest = nums[0]
        total = 0
        
        for n in nums:
            total += n
            largest = max(largest, n)
            
        if m == 1: return total
        if m == len(nums): return largest
            
        # the ideal subarray sum is somewhere between the largest element and total sum
        # we zero in on the correct number using binary search
        lo = largest 
        hi = total
        while lo <= hi:
            s = (lo+hi)//2
            if self.checkAcceptable(s, nums, m):
#able to make <= m subarrays of sum s or lower, we want more subs so we try to lower the target sum
                hi = s-1
            else:
#able to make >m subarrays of sum s or lower, we want fewer subs so we try to raise the target sum
                lo = s+1
    
        return lo
